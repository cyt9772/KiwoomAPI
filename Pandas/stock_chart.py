import yfinance as yf
import matplotlib.pyplot as plt

import datetime

start=datetime.datetime(2021,1,1)
end = datetime.datetime(2022,12,16)

#yahoo 주식정보 가져오기
ticker='005930.KS'
df=yf.download(ticker, start=start, end=end)
#print(df)

plt.plot(df['Close'])
plt.show()

# #naver 주식정보 가져오기
# #data=stock.get_market_ohlcv_by_date(fromdate="20221201",todate="20221216",ticker="005930")
# #df1=stock.get_market_ohlcv_by_date("20221201","20221216","005930")
# #data=stock.get_market_ohlcv("20221201","20221216","005930")
# print(df1)

