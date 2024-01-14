from pandas_datareader import data as fdr
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt

yf.pdr_override()
start=datetime(2020,1,1)
end=datetime(2023,12,31)

lg=fdr.get_data_yahoo('066570.KS', start, end)
sam=fdr.get_data_yahoo('005930.KS', start, end)

plt.plot(lg.index, lg['Close'], label='LG Electronics')
plt.plot(sam.index, sam['Close'], label='Samsung Electronics')

plt.legend(loc='upper left')
plt.show()


