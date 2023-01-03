from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *


TR_REQ_TIME_INTERVAL=0.2

class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()
        self._create_kiwoom_instance()
        self._set_signal_slots()

    def _create_kiwoom_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")

    def _set_signal_slots(self):
        self.OnEventConnect.connect(self._event_connect)
        self.OnReceiveTrData.connect(self._receive_tr_data)
        self.OnReceiveChejanData.connect(self._receive_chejan_data)

    def comm_connect(self):
        self.dynamicCall("CommConnect()")
        self.login_event_loop=QEventLoop()
        self.login_event_loop.exec_()

    def _event_connect(self,err_code):
        if err_code==0:
            print("connected")
        else:
            print("disconnected")

        self.login_event_loop.exit()

    def get_code_list_by_market(self,market):
        code_list=self.dynamicCall("GetCodeListByMarket(QString)", market)
        code_list=code_list.split(';')
        return code_list[:-1]

    def get_master_code_name(self,code):
        code_name=self.dynamicCall("GetMasterCodeName(QString)", code)
        return code_name

    def get_connect_state(self):
        ret=self.dynamicCall("GetConnectState()")
        return ret

    def set_input_value(self, id, value):
        self.dynamicCall("SetInputValue(QString, QString)", id, value)

    #호출 후 서버에서 event줄때까지 대기하고 있어야 함.
    #
    def comm_rq_data(self, rqname, trcode, next, screen_no):
        self.dynamicCall("CommRqData(QString, QString, int, QString)", rqname, trcode, next, screen_no)
        self.tr_event_loop=QEventLoop()
        self.tr_event_loop.exec_()

    def _comm_get_data(self, code, real_type, field_name, index, item_name):
        ret=self.dynamicCall("CommGetData(QString, QString, QString, int, QString)",code, real_type, field_name, index, item_name)
        return ret.strip()

    def _get_repeat_cnt(self, trcode, rqname):
        ret=self.dynamicCall("GetRepeatCnt(QString, QString)", trcode, rqname)
        return ret

    def _receive_tr_data(self, screen_no, rqname, trcode, record_name, next, unused1, unused2, unused3, unused4):
        if next==2:
            self.remained_data=True
        else:
            self.remained_data=False

        if rqname=="opt10081_req":
            self._opt10081(rqname,trcode)

        if rqname=="opw00001_req":
            self._opw00001(rqname, trcode)

        try:
            self.tr_event_loop.exit()
        except AttributeError:
            pass

    def _opt10081(self, rqname, trcode):
        data_cnt=self._get_repeat_cnt(trcode, rqname)

        for i in range(data_cnt):
            date=self._comm_get_data(trcode, "", rqname, i, "일자")
            open = self._comm_get_data(trcode, "", rqname, i, "시가")
            high = self._comm_get_data(trcode, "", rqname, i, "고가")
            low = self._comm_get_data(trcode, "", rqname, i, "저가")
            close = self._comm_get_data(trcode, "", rqname, i, "현재가")
            volume = self._comm_get_data(trcode, "", rqname, i, "거래량")

            #Database 처리
            self.ohlcv['date'].append(date)
            self.ohlcv['open'].append(int(open))
            self.ohlcv['high'].append(int(high))
            self.ohlcv['low'].append(int(low))
            self.ohlcv['close'].append(int(close))
            self.ohlcv['volume'].append(int(volume))

    def _opw00001(self, rqname, trcode):
        self.d2_deposit=self._comm_get_data(trcode, "", rqname, 0, "d+2추정예수금")
        self.d2_deposit=Kiwoom.change_format(self.d2_deposit)

    def send_order(self, rqname, screen_no, acc_no, order_type, code, quantity, price, hoga, order_no):
        self.dynamicCall("SendOrder(QString, QString, QString, int, QString, int, int, QString, QString)",
                         [rqname, screen_no, acc_no, order_type, code, quantity, price, hoga, order_no])

    def get_chejan_data(self, fid):
        ret=self.dynamicCall("GetChejanData(int)", fid)
        return ret

    """
    9203: 주문번호, 302: 종목명, 900: 주문수량, 901: 주문가격, 902: 미체결수량, 904:원주문번호, 905:주문번호,
    908: 주문/체결시간, 909: 체결번호, 910: 체결가, 911:체결량, 10: 현재가, 체결가, 실시간종가
    """
    def _receive_chejan_data(self, gubun, item_cnt, fid_list):
        print(gubun)
        print(self.get_chejan_data(9203))
        print(self.get_chejan_data(302))
        print(self.get_chejan_data(900))
        print(self.get_chejan_data(901))

    def get_login_info(self, tag):
        ret=self.dynamicCall("GetLoginInfo(QString)", tag)
        return ret

    @staticmethod
    def change_format(data):
        strip_data = data.lstrip('-0')

        if strip_data == '' or strip_data == '.00':
            strip_data = '0'

        try:
            format_data = format(int(strip_data), '-d')
        except:
            format_data = format(float(strip_data))

        if data.startswith('-'):
            format_data = '-' + format_data

        return format_data