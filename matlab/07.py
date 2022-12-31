import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import datetime

tick_SS="005930.KS"
tick_LG="066570.KS"

start=datetime.datetime(2021,1,1)
end = datetime.datetime(2022,12,16)

df_SS=yf.download(tick_SS,start=start,end=end)
df_LG=yf.download(tick_LG,start=start,end=end)

plt.plot(df_SS.index, df_SS['Close'], label='Samsung Electronics')
plt.plot(df_LG.index, df_LG['Close'], label='LG Electronics')

plt.legend(loc='upper left')

plt.show()