import win32gui
import win32api
import win32con
import commctrl
import ctypes
import time
"""
WM_KEYDOWN = 256
WM_KEYUP = 257
"""
from win32con import PAGE_READWRITE, MEM_COMMIT, MEM_RESERVE, MEM_RELEASE, PROCESS_ALL_ACCESS

GetWindowThreadProcessId = ctypes.windll.user32.GetWindowThreadProcessId
VirtualAllocEx = ctypes.windll.kernel32.VirtualAllocEx
VirtualFreeEx = ctypes.windll.kernel32.VirtualFreeEx
OpenProcess = ctypes.windll.kernel32.OpenProcess
WriteProcessMemory = ctypes.windll.kernel32.WriteProcessMemory
ReadProcessMemory = ctypes.windll.kernel32.ReadProcessMemory

class Edit(object):
    def __init__(self, hwnd):
        self.hwnd = hwnd
    def set_text(self, text):
        win32gui.SendMessage(self.hwnd, win32con.WM_SETTEXT, None, text)
    def send_endter(self):
        win32gui.PostMessage(self.hwnd, win32con.WM_KEYDOWN, 0x0D, 0)
        win32gui.PostMessage(self.hwnd, win32con.WM_KEYUP, 0x0D, 0)
class Button(object):
    def __init__(self, hwnd):
        self.hwnd = hwnd
    def click(self):
        win32gui.SendMessage(self.hwnd, win32con.BM_CLICK,0,0)
        #win32gui.SendMessage(self.hwnd, win32con.BM_CLICK, 0, 0)

class RadioGroup(object):
    def __init__(self, hwnd):
        self.hwnd = hwnd
    def select(self, n):
        n = int(n)
        x = 19 + 50 * n
        y = 11
        pos = self.makeParam(x,y)
        win32gui.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN, 1, pos)
        win32gui.SendMessage(self.hwnd, win32con.WM_LBUTTONUP, 1, pos)

    def makeParam(self, x, y):
        return ((y << 16) | (x & 0xFFFF))

class CheckBox(object):
    def __init__(self, hwnd):
        self.hwnd = hwnd
    def check(self):
        pass
class Control(object):
    def __init__(self, hwnd):
        self.hwnd = hwnd
    def send_enter(self):
        win32gui.SetForegroundWindow(self.hwnd)
        win32api.keybd_event(0x0D, 0, 0, 0)
    def double_enter(self):
        win32gui.SetForegroundWindow(self.hwnd)
        win32api.keybd_event(0x0D, 0, 0, 0)
        time.sleep(1)
        win32api.keybd_event(0x0D, 0, 0, 0)
    def post_enter(self):
        win32gui.PostMessage(self.hwnd, win32con.WM_KEYDOWN, 0x0D, 0)
        win32gui.PostMessage(self.hwnd, win32con.WM_KEYUP, 0x0D, 0)

"""
win32gui.PostMessage(fee, 513, 1, makep(16,17))
... win32gui.PostMessage(fee, 514, 1, makep(16,17))
win32con.py
WM_LBUTTONDOWN = 513
WM_LBUTTONUP = 514
"""