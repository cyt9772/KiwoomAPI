import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #kiwoom login
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")

        #open API+ event
        self.kiwoom.OnEventConnect.connect(self.event_connect)

        self.setWindowTitle("종목 코드")
        self.setGeometry(300,300,300,150)


        btn1=QPushButton("종목코드 얻기",self)
        btn1.move(190,10)
        btn1.clicked.connect(self.btn1_clicked)

        self.listWidget=QListWidget(self)
        self.listWidget.setGeometry(10,10,170,130)

        # btn2 = QPushButton("Check State", self)
        # btn2.move(20, 70)
        # btn2.clicked.connect(self.btn2_clicked)

        # self.text_edit=QTextEdit(self)
        # self.text_edit.setGeometry(10,60,280,80)

    def btn1_clicked(self):
        ret=self.kiwoom.dynamicCall("GetCodeListByMarket(QString)",["0"]) #0 - 장내, 10-코스닥, 8-etf
        kospi_code_list=ret.split(';')
        kospi_code_name_list=[]

        for x in kospi_code_list:
            name = self.kiwoom.dynamicCall("GetMasterCodeName(QString)",[x])
            kospi_code_name_list.append(x+" : "+name)

        self.listWidget.addItems(kospi_code_name_list)

    # def btn1_clicked(self):
    #     ret=self.kiwoom.dynamicCall("CommConnect()")
    #
    # def btn2_clicked(self):
    #     if self.kiwoom.dynamicCall("GetConnectState()")==0:
    #         self.statusBar().showMessage("Not Connected")
    #     else:
    #         self.statusBar().showMessage("Connected")
    #
    def event_connect(self, err_code):
        if err_code==0:
            self.statusBar().showMessage("로그인 성공")


if __name__=="__main__":
    app=QApplication(sys.argv)
    myWindow=MyWindow()
    myWindow.show()
    app.exec_()