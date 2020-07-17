# -*- coding:cp949 -*-
# TeraCopy ������ ��� ������ ��ü�� �����մϴ�.
import cah
import win32gui
import pywintypes
import sys

app_name = "�μ� �� ���� [������] / [�������Ʈ����-�������Ʈ����]"
app_name = "���� ���� - Windows �޸���"
app_name = "��������(�ű�)"
#TODO Ŭ���� �̸����� ��ϵ��� ����
# �θ� �������� �ڵ��� �˻��մϴ�.
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

def GetClassNN(hwnd, extra):
    if extra.get_class_name() != win32gui.GetClassName(hwnd):
        pass
    else:
        extra.add_count()
        if extra.get_hwnd() == hwnd:
            return pywintypes.FALSE




# main �Դϴ�.

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


