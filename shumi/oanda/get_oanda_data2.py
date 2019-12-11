from oandapyV20 import API
from oandapyV20.exceptions import V20Error
from oandapyV20.endpoints.pricing import PricingStream
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.accounts as accounts

import datetime
import pandas as pd

COUNT = 5000        # 一度に取得するデータ数(max:5000)
NB_ITR = 10          # count * NB_ITR 分データを取得
GRANULARITY = "H1"
INSTRUMENT = "USD_JPY"

def get_candles(instrument="USD_JPY", params=None):
    """
        足データを取得してDataFrameに変換
    """
    instruments_candles = instruments.InstrumentsCandles(instrument=instrument, params=params)
 
    api.request(instruments_candles)
    response = instruments_candles.response

    data = []
    for raw in response['candles']:
        data.append([raw['time'], raw['volume'], raw['bid']['o'], raw['bid']['h'], raw['bid']['l'], raw['bid']['c']])
 
    df = pd.DataFrame(data)
    df.columns = ['Time', 'Volume', 'Open', 'High', 'Low', 'Close']
 
    return df

def load_data(path):
    with open(path) as f:
        s = f.read()
    return s.split('\n')

access_token, account_id = load_data('oanda_token.txt')
api = API(access_token=access_token, environment="practice")

params = {
    "granularity": GRANULARITY,
    "count": COUNT,
    "price": "B",
}
 
# 足データの取得
candles = None
for i in range(NB_ITR):
    new_candles = get_candles(instrument=INSTRUMENT, params=params)
    params["to"] = new_candles["Time"].iloc[0]
    print(params["to"])
    candles = pd.concat([new_candles, candles])
df = candles.set_index('Time')

# date型を綺麗にする
df.index = pd.to_datetime(df.index)

df.to_csv('data/oanda-{0}-{1}.csv'.format(GRANULARITY, COUNT*NB_ITR))