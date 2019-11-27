import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from oandapyV20 import API
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.accounts as accounts

import numpy as np
import requests
import pandas as pd
from selenium import webdriver
import time
import schedule

def load_data(path):
    with open(path) as f:
        s = f.read()
    return s.split('\n')

oanda_access_token, oanda_account_id = load_data('oanda_token')
school_id, school_pass = load_data('school_id.txt')
line_access_token = load_data('line_access_token.txt')


def job():
    def school_login():
        driver = webdriver.Chrome('chromedriver')
        driver.get('https://authsvr.u-shizuoka-ken.ac.jp:4343/')
        time.sleep(2)
        search_box = driver.find_element_by_name('name')
        search_box.send_keys(school_id)
        search_box = driver.find_element_by_name('pass')
        search_box.send_keys(school_pass)
        search = driver.find_element_by_name('f_loginbtn')
        search.click()
        time.sleep(2)
        driver.quit()

    school_login()

    class LSTM(nn.Module):
        def __init__(self, input_dim, hidden_dim, output_dim):
            super(LSTM, self).__init__()
            self.hidden_dim = hidden_dim

            self.lstm = nn.LSTM(input_dim, hidden_dim, batch_first = True)
            self.linear = nn.Linear(hidden_dim, output_dim)
            self.sigmoid = nn.Sigmoid()
            self.hidden = None

        def init_hidden(self, batch_size):
            return (torch.zeros(1, batch_size, self.hidden_dim).to(device), torch.zeros(1, batch_size, self.hidden_dim).to(device))

        def forward(self, inputs):
            lstm_out, self.hidden = self.lstm(inputs, self.hidden)
            linear_out = self.linear(self.hidden[0])
            output = self.sigmoid(linear_out)
            return output

    api = API(access_token=oanda_access_token, environment="practice")

    params = {
    "count": 31,
    "granularity": "D"
    }
    r = instruments.InstrumentsCandles(instrument="USD_JPY", params=params)
    api.request(r)
    data = []
    for raw in r.response['candles']:
        data.append([raw['time'], raw['volume'], raw['mid']['o'], raw['mid']['h'], raw['mid']['l'], raw['mid']['c']])
    df = pd.DataFrame(data)
    df.columns = ['Time', 'Volume', 'Open', 'High', 'Low', 'Close']
    df = df.set_index('Time')
    # date型を綺麗にする
    df.index = pd.to_datetime(df.index)

    idx = ['Open', 'High', 'Low', 'Close']
    window = 30
    input_dim = 4
    hidden_dim = 32
    output_dim = 1
    batch_size = 64
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    df = df[idx].astype(float).diff()[1:]
    data = pd.read_csv('data/oanda-D-5000.csv')
    data = data[idx].diff()[1:]
    max_value = data[idx].max().max()
    min_value = data[idx].min().min()
    df[idx] = ((df[idx] - min_value) / (max_value - min_value))
    data = df[idx].values

    model_path = 'result/diff_seikika_and_0_or_1/model/model0090.pth'
    model = LSTM(input_dim, hidden_dim, output_dim).float().to(device)
    model.load_state_dict(torch.load(model_path))
    with torch.no_grad():
        data = torch.Tensor(data).to(device)
        data = data.reshape(1, 30, 4)
        model.hidden = model.init_hidden(len(data))
        output = model(data).item()

    line_url = "https://notify-api.line.me/api/notify"
    payload = {'message': '{0}'.format(output)}
    headers = {'Authorization': 'Bearer ' + line_access_token}
    r = requests.post(line_url, headers=headers, params=payload)

def main():
    schedule.every().day.at('21:59').do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

main()