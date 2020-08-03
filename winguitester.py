# -*- coding:cp949 -*-
# TeraCopy ������ ��� ������ ��ü�� �����մϴ�.
import cah

import win32gui
import pywintypes
import sys
import control_finder
import json
import control_wrapper
import order_maker
from collections import defaultdict
import window_finder
app_name = "�μ� �� ���� [������] / [�������Ʈ����-�������Ʈ����]"
app_name = "���� ���� - Windows �޸���"
app_name = "��������(�ű�)"
#TODO Ŭ���� �̸����� ��ϵ��� ����
# �θ� �������� �ڵ��� �˻��մϴ�.
"""
class WindowFinder:
    def __init__(self, windowname):
        self.count = 0
        try:
            win32gui.EnumWindows(self.__EnumWindowsHandler, windowname)
        except pywintypes.error as e:
            pass
    def __EnumWindowsHandler(self, hwnd, extra):
        wintext = win32gui.GetWindowText(hwnd)
        if app_name in win32gui.GetWindowText(hwnd):
            self.__hwnd = hwnd
            return pywintypes.FALSE
        if wintext.find(extra) != -1:
            self.__hwnd = hwnd
            return pywintypes.FALSE  # FALSE�� ���ܸ� �߻���ŵ�ϴ�.

    def GetHwnd(self):
        return self.__hwnd

    __hwnd = 0


# �ڽ� �������� �ڵ� ����Ʈ�� �˻��մϴ�.
class ChildWindowFinder:
    def __init__(self, parentwnd):
        try:
            win32gui.EnumChildWindows(parentwnd, self.__EnumChildWindowsHandler, None)
        except pywintypes.error as e:
            if e[0] == 0:
                pass

    def __EnumChildWindowsHandler(self, hwnd, extra):
        self.__childwnds.append(hwnd)

    def GetChildrenList(self):
        return self.__childwnds

    __childwnds = []


# windowname�� ���� �������� ��� �ڽ� ������ ����Ʈ�� ����.
def GetChildWindows(windowname):
    # TeraCopy�� window handle�� �˻��Ѵ�.
    fd = WindowFinder(windowname)
    teracopyhwnd = fd.GetHwnd()
    # Teracopy�� ��� child window handle�� �˻��Ѵ�.
    childrenlist = ChildWindowFinder(teracopyhwnd).GetChildrenList()

    return teracopyhwnd, childrenlist
"""
def GetClassNN(hwnd, extra):
    if extra.get_class_name() != win32gui.GetClassName(hwnd):
        pass
    else:
        extra.add_count()
        if extra.get_hwnd() == hwnd:
            return pywintypes.FALSE




# main �Դϴ�.

hwnd, childwnds = window_finder.GetChildWindows(app_name)
cf = control_finder.OrderControl_Finder()
window_finder.find_targets(childwnds, cf)
control_dict = cf.get_control_dict()
####### �ӽ� ������. ���� ������ �κ�
"""
��� �ϴºκ�
��ſ��� ������ �޾Ƽ� ���� ����ŷ �ϴ� Ŭ���� ����

"""
data = {"cstm_buyer" : "�ٻ�",
        "cstm_detail" : "�ڽ��ϳ�",
        "start_dong" : "��õ�� ���ﵿ",
        "start_pnumber": "02-307-2567",
        "start_name" : "�츮��",
        "dest_name" : "���",
        "payment": "2",
        "car" : "2",
        "fee" : "50000"
        }
om = order_maker.OrderMaker(control_dict, data)
om.make_order()
om.finalyze()
#jdata = json.dumps(data)
#print(hwnd)

#car = control_dict["button"]["car"]
#fee = control_dict["button"]["fee"]
#start_dong = control_dict["edit"]["start_dong"]
#buyer = control_dict["edit"]["cstm_buyer"]





#######
"""
for child in childwnds:

    wnd_clas = win32gui.GetClassName(child)
    wnd_text = win32gui.GetWindowText(child)
    wnd_text = "".join(wnd_text.splitlines())
    parent = win32gui.GetParent(child)
    print("%08d %08d %s %s" %(child, parent,wnd_clas, wnd_text,))
    
#����â�� ������ ��� ������ �ؾߵɵ�
for c in control_dict:
    for a in control_dict[c]:
        if str(type(a)) == "<class 'str'>":
            print(a," = ", control_dict[c][a], win32gui.GetClassName(control_dict[c][a]))

encoded_data = json.load(jdata)
for i, e in encoded_data.items():
    for dict in control_dict:
        if i not in control_dict[dict]:
            continue
        else:
            target_hwnd = control_dict[dict][i]
"""



#print("%X %s" % (hwnd, win32gui.GetWindowText(hwnd)))

#print("HWND     CtlrID        Class               Window Text")
#print("===========================================")
#print(len(childwnds))
"""
for child in childwnds:
    ctrl_id = win32gui.GetDlgCtrlID(child)
    wnd_clas = win32gui.GetClassName(child)
    wnd_text = win32gui.GetWindowText(child)
    wnd_text = "".join(wnd_text.splitlines())
    parent = win32gui.GetParent(child)


    c = cah.Cah(child)
    try:
        win32gui.EnumChildWindows(hwnd, GetClassNN, c)
    except pywintypes.error as e:
        exit(0)

    print ("%08X %6d        %s         %s   %d" % (child, ctrl_id, wnd_clas + str(c.get_count()),wnd_text, parent))
win32gui.PostMessage(cb,513,0,0)
win32gui.PostMessage(cb,514,0,0)
"""