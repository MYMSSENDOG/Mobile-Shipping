import win32gui
import pywintypes
import collections
"""
# windowfinder는 사전 준비단계와 같다.
프로그램을 동작하기 위해 모든 윈도우에 대해 표적 윈도우를 찾아내고 그 자식 윈도우의 핸들을 반환할 수 있다.

WindowFinder : 현재 내 컴퓨터에 켜져있는 dlg창들 중 windowname 이 wintext인 창을 찾아낸다. 그리고 handle도 저장함 
ChildWindowFinder : 부모 hwnd의 자식에 해당하는 모든 window의 hwnd를 구한다.
GetChildWindows : 외부에서 호출하는 함수로 부모 windowname에대한 dlg hwnd와 그 자식의 hwnd리스를 반환한다.
find_targets : control finder에서 만든 딕셔너리를 이용. 

"""



#현재 내 컴퓨터에 켜져있는 dlg창들 중 windowname 이 wintext인 창을 찾아낸다. 그리고 handle도 저장함
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

# phwnd가 주어지면 그에 포함된 모든 자식의 hwnd를 구한다.
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

#windowname에 대한 부모 창을 찾아내고, 그거에 속해있는 자식의 모든 handle을 리스트형태로 반환한다.
def GetChildWindows(windowname):

    wf = WindowFinder(windowname)
    phwnd = wf.GetHwnd()

    childrenlist = ChildWindowFinder(phwnd).GetChildrenList()

    return phwnd, childrenlist

#cf에 내가 원하는 control이 EDIT의 몇 번째인지 존재한다.
#현재 childwnds가 있으므로 그것을 돌면서 클래스가 몇 번째만에 나왔는지 확인 후, 우리가 원하는 번 째의 클래스라면
#저장을 한다. 또한 이것들은 별명을 가지고 있어 "start_search"같은 이름으로 찾을 수 있다.
def find_targets(childwnds, cf):
    cntl_dict = cf.get_control_dict()
    counter_dict = collections.defaultdict(int)
    for child in childwnds:
        #ctrl_id = win32gui.GetDlgCtrlID(child)
        wnd_clas = win32gui.GetClassName(child)
        #wnd_text = win32gui.GetWindowText(child)
        #wnd_text = "".join(wnd_text.splitlines())
        #parent = win32gui.GetParent(child)

        counter_dict[wnd_clas] += 1
        cur_count = counter_dict[wnd_clas] # 몇 번 째로 나오는지 센다.
        if wnd_clas == "WindowsForms10.EDIT.app.0.13965fa_r9_ad1":#간단화 하기 위해 하드코딩 함
            wnd_clas = "EDIT"
        elif wnd_clas == "WindowsForms10.Window.b.app.0.13965fa_r9_ad1":
            wnd_clas = "BUTTON"
        if wnd_clas in cntl_dict:
            if cur_count in cntl_dict[wnd_clas]:# 해당하는 클래스의 해당하는 번호라면 저장한다.
                name = cntl_dict[wnd_clas][cur_count]#"new" = dict["BUTTON"][52]
                cntl_dict[wnd_clas][name] = child#dict["BUTTON"]["new"] = handle 이제 원하는 버튼의 핸들을 찾을 수 있다.
def GetClassNN(hwnd, extra):
    if extra.get_class_name() != win32gui.GetClassName(hwnd):
        pass
    else:
        extra.add_count()
        if extra.get_hwnd() == hwnd:
            return pywintypes.FALSE