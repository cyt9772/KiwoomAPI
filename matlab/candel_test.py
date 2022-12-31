import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import datetime
import mpl_finance as mp

tick="005930.KS"

start=datetime.datetime(2022,12,1)
end = datetime.datetime(2022,12,16)

df=yf.download(tick,start=start,end=end)
df=df[df['Volume']>0]

fig=plt.figure(figsize=(12,8))
ax=fig.add_subplot(111)

mp.candlestick2_ochl(ax, df['Open'], df['High'], df['Low'], df['Close'], width=0.5, colorup='r', colordown='b')
plt.show()