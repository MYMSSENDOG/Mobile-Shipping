"""
지불자 41

고객
----------------
검색      37      버튼 WindowsForms10.Window.b.app.0.13965fa_r9_ad1169
고객명     29
적요      32

출발지
----------------
검색      27      버튼 WindowsForms10.Window.b.app.0.13965fa_r9_ad1152
고객명      26
전화      28
동명      25
도착지
----------------
검색      19      버튼 WindowsForms10.Window.b.app.0.13965fa_r9_ad1129
고객      18
전화      20
동명      17

요금
----------------
요금 (선불 착불 신용 송금 수금 카드) WindowsForms10.Window.b.app.0.13965fa_r9_ad174
차량 (오토 다마 밴 라보 트럭 지하)   WindowsForms10.Window.b.app.0.13965fa_r9_ad173

기본요금    8

접수 저장 버튼 WindowsForms10.Window.b.app.0.13965fa_r9_ad14
"""
class OrderControl_Finder:

    #오더 접수 신규 창 뿐만 아니라 기본창도 추가 할 것

    def __init__(self):
        self.__init_dict1()
        pass
    def __init_dict1(self):
        self.controls_dict = {}
        self.edit_dict = {}
        self.btn_radio_dict = {}

        self.controls_dict["EDIT"] = self.edit_dict

        self.controls_dict["BUTTON"] = self.btn_radio_dict

        self.edit_dict[41] = "cstm_buyer"
        self.edit_dict[37] = "cstm_search"
        self.edit_dict[29] = "cstm_name"
        self.edit_dict[32] = "cstm_detail"

        self.edit_dict[25] = "start_dong"
        self.edit_dict[26] = "start_name"
        self.edit_dict[27] = "start_search"
        self.edit_dict[28] = "start_pnumber"

        self.edit_dict[17] = "dest_dong"
        self.edit_dict[18] = "dest_name"
        self.edit_dict[19] = "dest_search"
        self.edit_dict[20] = "dest_pnumber"

        self.edit_dict[8] = "fee"

        self.btn_radio_dict[14] = "save_order_btnr"
        self.btn_radio_dict[1] = "close_btn"

        self.btn_radio_dict[73] = "payment"
        self.btn_radio_dict[72] = "car"

    def get_control_dict(self):
        return self.controls_dict

class CustomerConfirmControlFinder:
    def __init__(self):
        self.__init_dict1()
    def __init_dict1(self):
        self.controls_dict = {}
        self.edit_dict = {}
        self.btn_radio_dict = {}

        self.controls_dict["EDIT"] = self.edit_dict

        self.controls_dict["BUTTON"] = self.btn_radio_dict

        self.btn_radio_dict[12] = "adress_list"
    def get_control_dict(self):
        return self.controls_dict
