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

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle('Widget Test')
        self.setGeometry(800,200,300,300)

        self.textEdit=QTextEdit(self)
        self.textEdit.resize(280,250)
        self.textEdit.move(10,10)

        self.pushButton=QPushButton('저장',self)
        self.pushButton.resize(280,25)
        self.pushButton.move(10,270)

if __name__=='__main__':
    app=QApplication(sys.argv)
    mywindow=MyWindow()
    mywindow.show()
    app.exec_()




