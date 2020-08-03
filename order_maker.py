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
                     "fee": [EDIT, SET_TEXT]
                     }
finish_control_list = {
    "share": [CHECK_BOX, CHECK_BOX_CLICK],
    "save_order": [BUTTON, BUTTON_CLICK]
}

class OrderMaker():
    def __init__(self, control_dict, data):
        self.control_dict = control_dict
        self.data = data
    def make_order(self):
        for control in data_control_list:
            if control in self.data:
                value = self.data[control]
                control_type = data_control_list[control][0]

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
                        wrapper.send_endter()
                    if c == BUTTON_CLICK:
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
            control_type = data_control_list[control][0]
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