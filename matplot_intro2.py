from pandas_datareader import data as fdr
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt

yf.pdr_override()
start=datetime(2020,1,1)
end=datetime(2023,12,31)

sk_hynix=fdr.get_data_yahoo('000660.KS', start, end)

fig=plt.figure(figsize=(12,8))
top_axes=plt.subplot2grid((4,4),(0,0), rowspan=3, colspan=4)
bottom_axes=plt.subplot2grid((4,4),(3,0), rowspan=1, colspan=4)
bottom_axes.get_yaxis().get_major_formatter().set_scientific(False)

top_axes.plot(sk_hynix.index, sk_hynix['Close'], label='Close')
bottom_axes.plot(sk_hynix.index, sk_hynix['Volume'])

plt.tight_layout()
plt.show()
