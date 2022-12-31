import yfinance as yf
import matplotlib.pyplot as plt

from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA, GOOG

import datetime

start=datetime.datetime(2019,1,1)
end = datetime.datetime(2022,12,16)

#yahoo 주식정보 가져오기
ticker='005930.KS'
df=yf.download(ticker, start=start, end=end)


class SmaCross(Strategy):
    n1=20
    n2=60

    def init(self):
        price = df['Close'].values
        self.ma1=self.I(SMA,price,self.n1)
        self.ma2 = self.I(SMA, price, self.n2)
    def next(self):
        if crossover(self.ma1, self.ma2):
            self.buy()
        elif crossover(self.ma2, self.ma1):
            self.sell()

bt = Backtest(GOOG, SmaCross, cash=10000, commission=.002, exclusive_orders=True)
output=bt.run()
bt.plot()

# from backtesting import Backtest, Strategy
# from backtesting.lib import crossover
#
# from backtesting.test import SMA, GOOG
#
# class SmaCross(Strategy):
#     n1 = 10
#     n2 = 20
#
#     def init(self):
#         close = self.data.Close
#         self.sma1 = self.I(SMA, close, self.n1)
#         self.sma2 = self.I(SMA, close, self.n2)
#
#     def next(self):
#         if crossover(self.sma1, self.sma2):
#             self.buy()
#         elif crossover(self.sma2, self.sma1):
#             self.sell()
#
#
# bt = Backtest(GOOG, SmaCross,
#               cash=10000, commission=.002,
#               exclusive_orders=True)
#
# output = bt.run()
# bt.plot()
