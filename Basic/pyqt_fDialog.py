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

        self.pushButton=QPushButton('File Open')
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.label=QLabel()

        layout=QVBoxLayout()
        layout.addWidget(self.pushButton)
        layout.addWidget(self.label)

        self.setLayout(layout)
    def pushButtonClicked(self):
        fname=QFileDialog.getOpenFileName(self)
        self.label.setText(fname[0])

if __name__=='__main__':
    app=QApplication(sys.argv)
    mywindow=MyWindow()
    mywindow.show()
    app.exec_()




