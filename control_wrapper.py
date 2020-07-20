import win32gui
import win32api
import win32con
import commctrl
import ctypes
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
        win32gui.SendMessage(self.hwnd, "ENTER")
