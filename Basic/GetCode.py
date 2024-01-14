import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyStock')
        self.setGeometry(300,300,300,150)

        #kiwoom login
        self.kiwoom=QAxWidget('KHOPENAPI.KHOpenAPICtrl.1')
        self.kiwoom.dynamicCall('CommConnect()')
        self.kiwoom.OnEventConnect.connect(self.event_connect)

        btn1=QPushButton('Get Code', self)
        btn1.move(190,10)
        btn1.clicked.connect(self.btn1_clicked)

        self.listWidget=QListWidget(self)
        self.listWidget.setGeometry(10,10,170,130)

    def event_connect(self, err_code):
        if err_code==0:
            self.statusBar().showMessage('Login Success')

    def btn1_clicked(self):
        ret=self.kiwoom.dynamicCall('GetCodeListByMarket(QString)',['0'])
        kospi_code_list=ret.split(';')
        kospi_code_name=[]

        for x in kospi_code_list:
            name=self.kiwoom.dynamicCall('GetMasterCodeName(QString)',[x])
            kospi_code_name.append(x+' : '+name)
        self.listWidget.addItems(kospi_code_name)


if __name__=='__main__':
    app=QApplication(sys.argv)
    myWindow=MyWindow()
    myWindow.show()
    app.exec_()
