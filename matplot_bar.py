from pandas_datareader import data as fdr
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt
import mpl_finance
import matplotlib.ticker as ticker
from matplotlib import font_manager, rc
from matplotlib import style

font_name=font_manager.FontProperties(fname='c:\Windows\Fonts\malgun.ttf').get_name()
rc('font', family=font_name)
style.use('ggplot')

industry=['통신업','의료정밀','운수창고업','의약품','음식료품','전기가스업','서비스업','전기전자','종이목재','증권']
fluctuations=[1.83,1.30,1.30,1.26,1.06,0.93,0.77,0.68,0.65,0.61]

fig=plt.figure(figsize=(12,8))
ax=fig.add_subplot(111)

pos=np.arange(10)
rects=plt.bar(pos, fluctuations, align='center', width=0.5)
plt.xticks(pos, industry)

for i, rect in enumerate(rects):
    ax.text(rect.get_x()+rect.get_width()/2.0, 0.95*rect.get_height(), str(fluctuations[i])+'%', ha='center')

plt.ylabel('등락률')
plt.show()



plt.show()
