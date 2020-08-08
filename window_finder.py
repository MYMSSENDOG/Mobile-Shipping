import win32gui
import pywintypes
import collections


class WindowFinder:
    def __init__(self, windowname):
        self.count = 0
        try:
            win32gui.EnumWindows(self.__EnumWindowsHandler, windowname)
        except pywintypes.error as e:
            pass
    def __EnumWindowsHandler(self, hwnd, extra):
        wintext = win32gui.GetWindowText(hwnd)
        if extra in win32gui.GetWindowText(hwnd):
            self.__hwnd = hwnd
            return pywintypes.FALSE
        if wintext.find(extra) != -1:
            self.__hwnd = hwnd
            return pywintypes.FALSE  # FALSE는 예외를 발생시킵니다.

    def GetHwnd(self):
        return self.__hwnd

    __hwnd = 0

class ChildWindowFinder:
    def __init__(self, parentwnd):
        self.__childwnds = []
        try:
            win32gui.EnumChildWindows(parentwnd, self.__EnumChildWindowsHandler, None)
        except pywintypes.error as e:
            if e[0] == 0:
                pass

    def __EnumChildWindowsHandler(self, hwnd, extra):

        self.__childwnds.append(hwnd)

    def GetChildrenList(self):
        return self.__childwnds


def GetChildWindows(windowname):

    wf = WindowFinder(windowname)
    phwnd = wf.GetHwnd()

    childrenlist = ChildWindowFinder(phwnd).GetChildrenList()

    return phwnd, childrenlist

def find_targets(childwnds, cf):
    cntl_dict = cf.get_control_dict()
    counter_dict = collections.defaultdict(int)
    for child in childwnds:
        #ctrl_id = win32gui.GetDlgCtrlID(child)
        wnd_clas = win32gui.GetClassName(child)
        wnd_text = win32gui.GetWindowText(child)
        #wnd_text = "".join(wnd_text.splitlines())
        #parent = win32gui.GetParent(child)

        counter_dict[wnd_clas] += 1
        cur_count = counter_dict[wnd_clas]
        if wnd_clas == "WindowsForms10.EDIT.app.0.13965fa_r9_ad1":
            wnd_clas = "EDIT"
        elif wnd_clas == "WindowsForms10.Window.b.app.0.13965fa_r9_ad1":
            wnd_clas = "BUTTON"
        if wnd_clas in cntl_dict:
            if cur_count in cntl_dict[wnd_clas]:
                name = cntl_dict[wnd_clas][cur_count]
                cntl_dict[wnd_clas][name] = child
def GetClassNN(hwnd, extra):
    if extra.get_class_name() != win32gui.GetClassName(hwnd):
        pass
    else:
        extra.add_count()
        if extra.get_hwnd() == hwnd:
            return pywintypes.FALSE