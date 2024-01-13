from pandas_datareader import data as fdr
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt
# import mpl_finance
import matplotlib.ticker as ticker
from matplotlib import font_manager, rc
from matplotlib import style
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

#table과 pandas를 데이터 교환하는 방법

kospi_top5={
    'code':['005930','015760','005380','090430','012330'],
    'name':['삼성전자','한국전력','현대차','아모레퍼시픽','현대모비스'],
    'cprice':['1,269,000','60,100','132,000','414,500','243,500']
}

column_idx_lookup={'code':0, 'name':1, 'cprice':2}

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.df=pd.DataFrame(kospi_top5)
        self.df.columns = ['종목코드', '종목명', '종가']
        print(self.df)
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle('Widget Test')
        self.setGeometry(800,200,300,300)

        self.table=QTableWidget(self)
        self.table.resize(290,290)

        self.table.setRowCount(len(self.df))
        self.table.setColumnCount(len(self.df.columns))

        for i in range(len(self.df)):
            for j in range(len(self.df.columns)):
                item=QTableWidgetItem(str(self.df.iloc[i,j]))
                self.table.setItem(i,j,item)

        # self.setTableWidgetData()

    def setTableWidgetData(self):
        column_headers=['종목코드','종목명','종가']
        self.tableWidget.setHorizontalHeaderLabels(column_headers)

        for k,v in kospi_top5.items():
            col=column_idx_lookup[k]
            for row, val in enumerate(v):
                item=QTableWidgetItem(val)
                if col==2:
                    item.setTextAlignment(Qt.AlignVCenter|Qt.AlignRight)

                self.tableWidget.setItem(row, col, item)

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()


if __name__=='__main__':
    app=QApplication(sys.argv)
    mywindow=MyWindow()
    mywindow.show()
    app.exec_()




