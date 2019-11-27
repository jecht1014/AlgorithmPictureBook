from oandapyV20 import API
from oandapyV20.exceptions import V20Error
from oandapyV20.endpoints.pricing import PricingStream
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.accounts as accounts

import datetime
import pandas as pd

def load_data(path):
    with open(path) as f:
        s = f.read()
    return s.split('\n')

access_token, account_id = load_data('oanda_token.txt')

api = API(access_token=access_token, environment="practice")

params = {
  "count": 5000,
  "granularity": "H2"
}
r = instruments.InstrumentsCandles(instrument="USD_JPY", params=params)
api.request(r)
# valume:取引量、time:時間、o:開始、h:高値、l:底値、c:終値

data = []
for raw in r.response['candles']:
    data.append([raw['time'], raw['volume'], raw['mid']['o'], raw['mid']['h'], raw['mid']['l'], raw['mid']['c']])

# リストからPandas DataFrameへ変換
df = pd.DataFrame(data)
df.columns = ['Time', 'Volume', 'Open', 'High', 'Low', 'Close']
df = df.set_index('Time')

# date型を綺麗にする
df.index = pd.to_datetime(df.index)

df.to_csv('data/oanda-H2-5000.csv')