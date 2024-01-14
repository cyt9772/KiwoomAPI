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

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle('Widget Test')
        self.setGeometry(800,200,300,300)

        self.groupBox=QGroupBox('검색옵션')
        checkBox1=QCheckBox('상한가')
        checkBox2 = QCheckBox('하한가')
        checkBox3 = QCheckBox('시가총액 상위')
        checkBox4 = QCheckBox('시가총액 하위')
        checkBox5 = QCheckBox('회전율 상위')
        checkBox6 = QCheckBox('대량거래 상위')
        checkBox7 = QCheckBox('환산주가 상위')
        checkBox8 = QCheckBox('외국인한도소진상위')
        checkBox9 = QCheckBox('투자자별순위')

        self.tableWidget=QTableWidget(10,5)
        self.tableWidget.setHorizontalHeaderLabels(['종목코도','종목명','현재가','등락률','거래량'])
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()


        self.leftInnerLayout=QVBoxLayout()
        self.leftInnerLayout.addWidget(checkBox1)
        self.leftInnerLayout.addWidget(checkBox2)
        self.leftInnerLayout.addWidget(checkBox3)
        self.leftInnerLayout.addWidget(checkBox4)
        self.leftInnerLayout.addWidget(checkBox5)
        self.leftInnerLayout.addWidget(checkBox6)
        self.leftInnerLayout.addWidget(checkBox7)
        self.leftInnerLayout.addWidget(checkBox8)
        self.leftInnerLayout.addWidget(checkBox9)

        self.groupBox.setLayout(self.leftInnerLayout)

        self.leftLayout=QVBoxLayout()
        self.leftLayout.addWidget(self.groupBox)

        self.rightLayout=QVBoxLayout()
        self.rightLayout.addWidget(self.tableWidget)

        self.layout=QHBoxLayout()
        self.layout.addLayout(self.leftLayout)
        self.layout.addLayout(self.rightLayout)

        self.setLayout(self.layout)

if __name__=='__main__':
    app=QApplication(sys.argv)
    mywindow=MyWindow()
    mywindow.show()
    app.exec_()




