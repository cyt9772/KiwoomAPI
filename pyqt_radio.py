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

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle('Widget Test')
        self.setGeometry(800,200,300,300)

        gBox=QGroupBox('시간단위', self)
        gBox.move(10,10)
        gBox.resize(280,80)

        self.radio1=QRadioButton('일봉',self)
        self.radio1.move(20,20)
        self.radio1.clicked.connect(self.radioButtonClicked)

        self.radio2 = QRadioButton('주봉', self)
        self.radio2.move(20, 40)
        self.radio2.clicked.connect(self.radioButtonClicked)

        self.radio3 = QRadioButton('월봉', self)
        self.radio3.move(20, 60)
        self.radio3.clicked.connect(self.radioButtonClicked)

        self.statusBar=QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def radioButtonClicked(self):
        msg=""
        if self.radio1.isChecked():
            msg='일봉'
        elif self.radio2.isChecked():
            msg='주봉'
        else:
            msg='월봉'
        self.statusBar.showMessage(msg+' selected')

if __name__=='__main__':
    app=QApplication(sys.argv)
    mywindow=MyWindow()
    mywindow.show()
    app.exec_()




