from pandas_datareader import data as fdr
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt
import mpl_finance
import matplotlib.ticker as ticker

yf.pdr_override()
start=datetime(2023,12,1)
end=datetime(2023,12,31)

sk_hynix=fdr.get_data_yahoo('000660.KS', start, end)
sk_hynix=sk_hynix[sk_hynix['Volume']>0]

day_list=[]
name_list=[]

for i, day in enumerate(sk_hynix.index):
    if day.dayofweek==0: #monday
        day_list.append(i)
        name_list.append(day.strftime('%Y-%m-%d'+'(Mon)'))


fig=plt.figure(figsize=(12,8))

ax=fig.add_subplot(111)
ax.xaxis.set_major_locator(ticker.FixedLocator(day_list))
ax.xaxis.set_major_formatter(ticker.FixedFormatter(name_list))
mpl_finance.candlestick2_ohlc(ax, sk_hynix['Open'],sk_hynix['High'],sk_hynix['Low'],sk_hynix['Close'], width=0.5, colorup='r', colordown='b')
plt.show()
