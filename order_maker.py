"""
지불자 41

고객
----------------
맨위검색   41
검색      37      버튼 WindowsForms10.Window.b.app.0.13965fa_r9_ad1169
고객명    29
고객전화   31
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
        self.edit_dict[17] = "dest_dong"
        self.edit_dict[18] = "dest_name"
        self.edit_dict[19] = "dest_search"
        self.edit_dict[20] = "dest_pnumber"
"""
from control_wrapper import *
import window_finder
import time
import control_finder

import json
#10이전까지 행동을 정의
#10부터는 클래스를 정의
SET_TEXT =              -1
PRESS_ENTER =           0
NEW_WINDOW =            1
NEW_WINDOW_ENTER =      2 # now only dong finding window
NEW_WINDOW_DOUBLE_ENTER = 3
NEW_WINDOW_CLICK =      4
BUTTON_CLICK =          5
RADIO_BUTTON_SELECT =   6
CHECK_BOX_CLICK =       7
EDIT =                  10
BUTTON =                11
RADIO_BUTTON =          12
CHECK_BOX =             13

#각각의 컨트롤에 대해, 만약 그 컨트롤에 대한 명령을 받으면 어떻게 처리해야하는지 딕셔너리 + 리스트로 구현
data_control_list = {"cstm_buyer": [EDIT, SET_TEXT, PRESS_ENTER],
                     "cstm_search": [EDIT, SET_TEXT, PRESS_ENTER],
                     "cstm_name": [EDIT, SET_TEXT],
                     "cstm_detail": [EDIT, SET_TEXT],
                     "start_search": [EDIT, SET_TEXT, PRESS_ENTER],
                     "start_name": [EDIT, SET_TEXT, PRESS_ENTER],
                     "start_dong": [EDIT, SET_TEXT, PRESS_ENTER, NEW_WINDOW, NEW_WINDOW_DOUBLE_ENTER],
                     "start_pnumber": [EDIT, SET_TEXT],
                     "dest_search": [EDIT, SET_TEXT],
                     "dest_name": [EDIT, SET_TEXT, PRESS_ENTER],
                     "dest_dong": [EDIT, SET_TEXT, PRESS_ENTER, NEW_WINDOW, NEW_WINDOW_DOUBLE_ENTER],
                     "dest_pnumber": [EDIT, SET_TEXT],
                     "payment": [RADIO_BUTTON, RADIO_BUTTON_SELECT],
                     "car": [RADIO_BUTTON, RADIO_BUTTON_SELECT],
                     "fee": [EDIT, SET_TEXT],
                     "deliver": [RADIO_BUTTON, RADIO_BUTTON_SELECT],
                     #"day": [RADIO_BUTTON, RADIO_BUTTON_SELECT]
                     }
#위에것이 할 수도 있고 안할 수도 있는 거라면 이건 화물 접수를 하기위해 반드시 해야하는 마무리 작업
finish_control_list = {
    "share": [CHECK_BOX, CHECK_BOX_CLICK],
    "save": [BUTTON, BUTTON_CLICK],
    "close": [BUTTON, BUTTON_CLICK]
}
#메인 dlg에서 실제 작업을 할 dlg를 키는 작업을 하는 클래스
class NewWindow:
    def __init__(self, control_dict):
        self.control_dict = control_dict

    def new_window_start(self):
        wrapper = Button(self.control_dict["BUTTON"]["new"])
        wrapper.click()
    #지금은 쓰이지 않음
    main_dlg_control_list = {
        "new": [BUTTON, BUTTON_CLICK]
    }
class OrderMaker():
    def __init__(self, control_dict, data):
        self.control_dict = control_dict
        self.data = data
    #받은 데이터는 "start_name" : "금천구" 이런식으로 되어 있다. 이를 data_control_list에서 찾아
    def make_order(self):
        for control in data_control_list:
            if control in self.data:
                value = self.data[control]
                control_type = data_control_list[control][0]

                #데이터에서 받은 컨트롤의 클래스에 따라 컨트롤을 래핑해주고 컨트롤에 따라 정해진 명령을 수행함
                if control_type == EDIT:
                    hwnd = self.control_dict["EDIT"][control]
                    wrapper = Edit(hwnd)
                else:
                    hwnd = self.control_dict["BUTTON"][control]
                    if control_type == BUTTON:
                        wrapper = Button(hwnd)
                    elif control_type == RADIO_BUTTON:
                        wrapper = RadioGroup(hwnd)
                    elif control_type == CHECK_BOX:
                        wrapper = CheckBox(hwnd)
                for c in data_control_list[control][1:]:
                    if c == SET_TEXT:
                        wrapper.set_text(value)
                    if c == PRESS_ENTER:
                        if control == "cstm_buyer" or control == "start_name" or control == "dest_name":
                            wrapper.send_enter()
                        else:
                            wrapper.post_enter()

                    if c == BUTTON_CLICK:
                        if control == "close":
                            time.sleep(10)
                        wrapper.click()
                    if c == RADIO_BUTTON_SELECT:
                        wrapper.select(value)
                    if c ==CHECK_BOX_CLICK:
                        wrapper.check()
                    if c == NEW_WINDOW:
                        time.sleep(3)
                        new_window_hwnd, childwnds = window_finder.GetChildWindows("고객확인(New)")
                        #cf = control_finder.CustomerConfirmControlFinder()
                        #window_finder.find_targets(childwnds, cf)
                        #new_window_control_dict = cf.get_control_dict()
                        new_window_wrapper = Control(new_window_hwnd)
                    if c == NEW_WINDOW_ENTER:
                        new_window_wrapper.send_enter()
                    if c == NEW_WINDOW_DOUBLE_ENTER:
                        new_window_wrapper.double_enter()
                time.sleep(0.5)
    def finalyze(self):
        for control in finish_control_list:
            if "test" in self.data:
                if control == "save":
                    continue
            else:
                if control == "close":
                    continue

            control_type = finish_control_list[control][0]
            if control_type == EDIT:
                hwnd = self.control_dict["EDIT"][control]
                wrapper = Edit(hwnd)
            else:
                hwnd = self.control_dict["BUTTON"][control]
                if control_type == BUTTON:
                    wrapper = Button(hwnd)
                elif control_type == RADIO_BUTTON:
                    wrapper = RadioGroup(hwnd)
                elif control_type == CHECK_BOX:
                    wrapper = CheckBox(hwnd)
            for c in finish_control_list[control][1:]:
                if c == CHECK_BOX_CLICK:
                    wrapper.check()
                if c == BUTTON_CLICK:
                    wrapper.click()