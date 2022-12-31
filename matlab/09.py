import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import datetime

tick="005930.KS"

start=datetime.datetime(2021,1,1)
end = datetime.datetime(2022,12,16)

df=yf.download(tick,start=start,end=end)

fig=plt.figure(figsize=(12,8)) #가로, 세로 크기

top_axes=plt.subplot2grid((4,4),(0,0), rowspan=3,colspan=4)
bottom_axes=plt.subplot2grid((4,4),(3,0), rowspan=1,colspan=4)

bottom_axes.get_yaxis().get_major_formatter().set_scientific(False) #큰 값이 발생할때 지수형태 표시하지 않음

top_axes.plot(df.index, df['Close'], label='Close')
bottom_axes.plot(df.index, df['Volume'])
plt.tight_layout()

plt.show()