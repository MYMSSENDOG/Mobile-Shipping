# -*- coding:cp949 -*-
# TeraCopy ������ ��� ������ ��ü�� �����մϴ�.
import cah
import win32gui
import pywintypes
import sys
import control_finder
import json
import control_wrapper
from collections import defaultdict


app_name = "MEmu"


# TODO Ŭ���� �̸����� ��ϵ��� ����
# �θ� �������� �ڵ��� �˻��մϴ�.
def pos(x, y):
    return x|y<<16
class WindowFinder:
    def __init__(self, windowname):
        self.count = 0
        try:
            win32gui.EnumWindows(self.__EnumWindowsHandler, windowname)
        except pywintypes.error as e:
            pass

    def __EnumWindowsHandler(self, hwnd, extra):
        wintext = win32gui.GetWindowText(hwnd)
        if app_name == wintext:
            self.__hwnd = hwnd
            return pywintypes.FALSE

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
    _hwnd = fd.GetHwnd()

    return _hwnd


def GetClassNN(hwnd, extra):
    if extra.get_class_name() != win32gui.GetClassName(hwnd):
        pass
    else:
        extra.add_count()
        if extra.get_hwnd() == hwnd:
            return pywintypes.FALSE


def find_targets(childwnds, cf):
    cntl_dict = cf.get_control_dict()
    counter_dict = defaultdict(int)

    for child in childwnds:
        # ctrl_id = win32gui.GetDlgCtrlID(child)
        wnd_clas = win32gui.GetClassName(child)
        wnd_text = win32gui.GetWindowText(child)
        # wnd_text = "".join(wnd_text.splitlines())
        # parent = win32gui.GetParent(child)

        counter_dict[wnd_clas] += 1
        cur_count = counter_dict[wnd_clas]
        if wnd_clas == "WindowsForms10.EDIT.app.0.13965fa_r9_ad1":
            wnd_clas = "edit"
        elif wnd_clas == "WindowsForms10.Window.b.app.0.13965fa_r9_ad1":
            wnd_clas = "button"
        if wnd_clas in cntl_dict:
            if cur_count in cntl_dict[wnd_clas]:
                name = cntl_dict[wnd_clas][cur_count]
                cntl_dict[wnd_clas][name] = child


# main �Դϴ�.

hwnd = GetChildWindows(app_name)



print(hwnd)
