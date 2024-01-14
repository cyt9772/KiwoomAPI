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
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        btn1=QPushButton('닫기', self)
        btn1.move(20,20)
        # btn1.clicked.connect(QCoreApplication.instance().quit)
        btn1.clicked.connect(app.quit)

if __name__=='__main__':
    app=QApplication(sys.argv)
    mywindow=MyWindow()
    mywindow.show()
    app.exec_()




