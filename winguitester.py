# -*- coding:cp949 -*-
# TeraCopy 내부의 모든 윈도우 객체를 나열합니다.
import cah
import win32gui
import pywintypes
import sys

app_name = "인성 퀵 서비스 [윤덕순] / [노원스마트물류-노원스마트물류]"
app_name = "제목 없음 - Windows 메모장"
app_name = "오더접수(신규)"
#TODO 클래스 이름으로 우니도우 조작
# 부모 윈도우의 핸들을 검사합니다.
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
            return pywintypes.FALSE  # FALSE는 예외를 발생시킵니다.

    def GetHwnd(self):
        return self.__hwnd

    __hwnd = 0


# 자식 윈도우의 핸들 리스트를 검사합니다.
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


# windowname을 가진 윈도우의 모든 자식 윈도우 리스트를 얻어낸다.
def GetChildWindows(windowname):
    # TeraCopy의 window handle을 검사한다.
    fd = WindowFinder(windowname)
    teracopyhwnd = fd.GetHwnd()
    # Teracopy의 모든 child window handle을 검색한다.
    childrenlist = ChildWindowFinder(teracopyhwnd).GetChildrenList()

    return teracopyhwnd, childrenlist

def GetClassNN(hwnd, extra):
    if extra.get_class_name() != win32gui.GetClassName(hwnd):
        pass
    else:
        extra.add_count()
        if extra.get_hwnd() == hwnd:
            return pywintypes.FALSE




# main 입니다.

hwnd, childwnds = GetChildWindows(app_name)
print("%X %s" % (hwnd, win32gui.GetWindowText(hwnd)))

print("HWND     CtlrID        Class               Window Text")
print("===========================================")
print(len(childwnds))
print(hwnd)
for child in childwnds:
    ctrl_id = win32gui.GetDlgCtrlID(child)
    wnd_clas = win32gui.GetClassName(child)
    wnd_text = win32gui.GetWindowText(child)
    wnd_text = "".join(wnd_text.splitlines())
    c = cah.Cah(child)
    try:
        win32gui.EnumChildWindows(hwnd, GetClassNN, c)
    except pywintypes.error as e:
        exit(0)

    print ("%08X %6d        %s         %s   " % (child, ctrl_id, wnd_clas + str(c.get_count()),wnd_text))


