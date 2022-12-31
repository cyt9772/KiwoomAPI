import yfinance as yf
import matplotlib.pyplot as plt

import datetime

start=datetime.datetime(2019,1,1)
end = datetime.datetime(2022,12,16)

#yahoo 주식정보 가져오기
ticker='005930.KS'
ss=yf.download(ticker, start=start, end=end)

ma5=ss['Close'].rolling(window=5).mean()
ma20=ss['Close'].rolling(window=20).mean()
ma60=ss['Close'].rolling(window=60).mean()
ma120=ss['Close'].rolling(window=120).mean()


ss['MA5']=ma5
ss['MA20']=ma20
ss['MA60']=ma60
ss['MA120']=ma120

plt.plot(ss.index, ss['Close'],label='Close')
plt.plot(ss.index, ss['MA5'],label='MA5')
plt.plot(ss.index, ss['MA20'],label='MA20')
plt.plot(ss.index, ss['MA60'],label='MA60')
plt.plot(ss.index, ss['MA120'],label='MA120')

plt.legend(loc="best")
plt.grid()
plt.show()

