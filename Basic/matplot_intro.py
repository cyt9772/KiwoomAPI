from pandas_datareader import data as fdr
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(10,5))
ax1=fig.add_subplot(2,1,1)
ax2=fig.add_subplot(2,1,2)

x=np.arange(0.0, 2*np.pi, 0.1)
sin_y=np.sin(x)
cos_y=np.cos(x)

ax1.plot(x,sin_y, 'b--')
ax2.plot(x,cos_y, 'r--')

ax1.set_xlabel('x')
ax1.set_ylabel('sin(x)')

ax2.set_xlabel('x')
ax2.set_ylabel('cos(x)')

plt.show()




