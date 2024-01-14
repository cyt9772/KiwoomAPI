import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Account Info.')
        self.setGeometry(300,300,300,150)

        #kiwoom login
        self.kiwoom=QAxWidget('KHOPENAPI.KHOpenAPICtrl.1')
        self.kiwoom.dynamicCall('CommConnect()')
        self.kiwoom.OnEventConnect.connect(self.event_connect)

        btn1=QPushButton('Get Account', self)
        btn1.move(190,20)
        btn1.clicked.connect(self.btn1_clicked)

        self.text_edit=QTextEdit(self)
        self.text_edit.setGeometry(10,60,280,80)

    def event_connect(self, err_code):
        if err_code==0:
            self.text_edit.append('Login Success')

    def btn1_clicked(self):
        account_num=self.kiwoom.dynamicCall('GetLoginInfo(QString)',['ACCNO'])
        account_count=self.kiwoom.dynamicCall('GetLoginInfo(QString)',['ACCOUNT_CNT'])
        self.text_edit.append('Total Account: ' +account_count.strip())
        self.text_edit.append('Account: ' + account_num.rstrip(';'))


if __name__=='__main__':
    app=QApplication(sys.argv)
    myWindow=MyWindow()
    myWindow.show()
    app.exec_()
