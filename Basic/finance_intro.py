from pandas_datareader import data as fdr
import pandas
import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt


yf.pdr_override()

start=datetime(2020,1,1)
end=datetime(2023,12,31)

gs=fdr.get_data_yahoo('AAPL', start, end)
# aapl=web.get_data_yahoo('AAPL', start, end)
print(gs.info())

gs['ma5']=gs['Close'].rolling(window=5).mean()
gs['ma20']=gs['Close'].rolling(window=20).mean()
gs['ma120']=gs['Close'].rolling(window=120).mean()

plt.plot(gs.index, gs['Close'], label='Close')
plt.plot(gs.index,gs['ma5'], label='ma5')
plt.plot(gs.index,gs['ma20'], label='ma20')
plt.plot(gs.index,gs['ma120'], label='ma120')

plt.legend()
plt.show()

