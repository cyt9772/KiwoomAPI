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
        self.setGeometry(800,400,300,150)

        textLabel=QLabel('Message: ', self)
        textLabel.move(20,20)

        self.label=QLabel("",self)
        self.label.move(80,20)
        self.label.resize(150,30)

        btn1=QPushButton('Click', self)
        btn1.move(20,60)
        btn1.clicked.connect(self.btn1_clicked)

        btn2 = QPushButton('Clear', self)
        btn2.move(140, 60)
        btn2.clicked.connect(self.btn2_clicked)

    def btn1_clicked(self):
        self.label.setText('Button was clicked')
    def btn2_clicked(self):
        self.label.clear()

if __name__=='__main__':
    app=QApplication(sys.argv)
    mywindow=MyWindow()
    mywindow.show()
    app.exec_()




