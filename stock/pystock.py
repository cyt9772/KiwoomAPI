import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyStock")
        self.setGeometry(300,300,300,150)

        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")

        btn1=QPushButton("Login",self)
        btn1.move(20,20)
        btn1.clicked.connect(self.btn1_clicked)

        btn2 = QPushButton("Check State", self)
        btn2.move(20, 70)
        btn2.clicked.connect(self.btn2_clicked)

        text_edit=QTextEdit(self)
        text_edit.setGeometry(10,60,280,80)
        text_edit.setEnabled(False)


    def btn1_clicked(self):
        ret=self.kiwoom.dynamicCall("CommConnect()")

    def btn2_clicked(self):
        if self.kiwoom.dynamicCall("GetConnectState()")==0:
            self.statusBar().showMessage("Not Connected")
        else:
            self.statusBar().showMessage("Connected")

    def event_connect(self, err_code):
        if err_code==0:
            self.text_edit.append("로그인 성공")


if __name__=="__main__":
    app=QApplication(sys.argv)
    myWindow=MyWindow()
    myWindow.show()
    app.exec_()