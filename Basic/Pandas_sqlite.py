from pandas_datareader import data as fdr
import pandas as pd
import yfinance as yf
from datetime import datetime
import sqlite3


yf.pdr_override()

start = datetime(2020, 1, 1)
end = datetime(2023, 12, 31)
data=fdr.get_data_yahoo('005930.KS', start, end)

con=sqlite3.connect('./kospi.db')
data.to_sql('005930', con, if_exists='replace')

cmd="SELECT * from '005930'"
readed_df=pd.read_sql(cmd, con, index_col='Date')
readed_df.index=pd.to_datetime(readed_df.index)
print(readed_df.head(20))