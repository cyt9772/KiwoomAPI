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
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class LogInDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

        self.id=None
        self.passwd=None
    def setupUI(self):
        self.setGeometry(1100,200,300,100)
        self.setWindowTitle('Sign In')
        self.setWindowIcon(QIcon('icon.png'))

        label1=QLabel('ID: ')
        label2=QLabel('Password: ')

        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()

        self.pushButton1=QPushButton('Sign In')
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        layout=QGridLayout()
        layout.addWidget(label1, 0,0)
        layout.addWidget(self.lineEdit1, 0,1)
        layout.addWidget(self.pushButton1, 0,2)
        layout.addWidget(label2, 1,0)
        layout.addWidget(self.lineEdit2,1,1)

        self.setLayout(layout)

    def pushButtonClicked(self):
        self.id=self.lineEdit1.text()
        self.passwd=self.lineEdit2.text()
        self.close()


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle('PyStock v0.1')
        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(800,200,300,300)

        self.pushButton=QPushButton('Sign In')
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.label=QLabel()

        layout=QVBoxLayout()
        layout.addWidget(self.pushButton)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def pushButtonClicked(self):
        dlg=LogInDialog()
        dlg.exec_()
        id=dlg.id
        passwd=dlg.passwd
        self.label.setText('id: %s, Passwd: %s'%(id, passwd))

if __name__=='__main__':
    app=QApplication(sys.argv)
    mywindow=MyWindow()
    mywindow.show()
    app.exec_()




