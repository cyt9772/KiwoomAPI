import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from pandas_datareader import data as fdr
import pandas as pd
import yfinance as yf
from datetime import datetime

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(600,200,1200,600)
        self.setWindowTitle('Pychart Viewer v0.1')
        self.setWindowIcon(QIcon('icon.png'))
        self.lineEdit=QLineEdit()
        self.pushBtn=QPushButton('차트그리기')
        self.pushBtn.clicked.connect(self.pushBtnClicked)

        self.fig=plt.Figure()
        self.canvas=FigureCanvas(self.fig)

        leftLayout=QVBoxLayout()
        leftLayout.addWidget(self.canvas)

        rightLayout=QVBoxLayout()
        rightLayout.addWidget(self.lineEdit)
        rightLayout.addWidget(self.pushBtn)
        rightLayout.addStretch(1)

        layout=QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(rightLayout)
        layout.setStretchFactor(leftLayout,1)
        layout.setStretchFactor(rightLayout, 0)

        self.setLayout(layout)

    def pushBtnClicked(self):
        yf.pdr_override()
        code=self.lineEdit.text()
        code=code+'.KS'
        print('Code: ',code)
        start = datetime(2020, 1, 1)
        end = datetime(2023, 12, 31)
        data = fdr.get_data_yahoo(code, start, end)
        print(data.head())
        data['MA20']=data['Close'].rolling(window=20).mean()
        data['MA60'] = data['Close'].rolling(window=60).mean()

        ax=self.fig.add_subplot(111)
        ax.plot(data.index, data['Close'], label='Close')
        ax.plot(data.index, data['MA20'], label='MA20')
        ax.plot(data.index, data['MA60'], label='MA60')
        ax.legend(loc='upper right')
        ax.grid()

        self.canvas.draw()


if __name__=='__main__':
    app=QApplication(sys.argv)
    mywindow=MyWindow()
    mywindow.show()
    app.exec_()