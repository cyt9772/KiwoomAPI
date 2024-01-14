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

colors=['gold','yellowgreen','lightcoral','lightskyblue','red']
labels=['삼성전자','SK하이닉스','LG전자','네이버','카카오']
ratio=[50,20,10,10,10]
explode=(0.0,0.1,0.0,0.0,0.0)

plt.pie(ratio, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.show()
