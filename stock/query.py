import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyStock")
        self.setGeometry(300,300,300,150)

        # Kiwoom login
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")

        #OpenAPI+ Event
        self.kiwoom.OnEventConnect.connect(self.event_connect)
        self.kiwoom.OnReceiveTrData.connect(self.receive_trdata)

        self.label=QLabel('종목코드: ', self)
        self.label.move(20,20)

        self.code_edit=QLineEdit(self)
        self.code_edit.move(80,20)
        self.code_edit.setText("039490")



        btn1=QPushButton("조회",self)
        btn1.move(190,20)
        btn1.clicked.connect(self.btn1_clicked)


        self.text_edit=QTextEdit(self)
        self.text_edit.setGeometry(10,60,280,80)
        self.text_edit.setEnabled(False)

        # self.kiwoom.OnEventConnect.connect(self.event_connect)


    def btn1_clicked(self):
        code = self.code_edit.text()
        self.text_edit.append("종목코드: "+ code)

        # Set Input value
        self.kiwoom.dynamicCall("SetInputValue(QString, QString", "종목코드", code)

        #commRqData
        self.kiwoom.dynamicCall("CommRqData(QString, QString, int, QString)","opt10001_req", "opt10001",0,"0101")

    def receive_trdata(self, screen_no, rqname,trcode, recordname, prev_next, data_len,err_code, msg1, msg2):
        if rqname =="opt10001_req":
            name = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "",rqname,0,"종목명")
            volume = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "거래량")

            self.text_edit.append("종목명: "+name.strip())
            self.text_edit.append("거래량: " + volume.strip())

    # def btn2_clicked(self):
    #     if self.kiwoom.dynamicCall("GetConnectState()")==0:
    #         self.statusBar().showMessage("Not Connected")
    #     else:
    #         self.statusBar().showMessage("Connected")
    #
    def event_connect(self, err_code):
        if err_code==0:
            self.text_edit.append("로그인 성공")


if __name__=="__main__":
    app=QApplication(sys.argv)
    myWindow=MyWindow()
    myWindow.show()
    app.exec_()