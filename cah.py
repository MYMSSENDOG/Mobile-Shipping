import win32gui
class Cah:# class and handle
    def __init__(self, hwnd):
        self.__hwnd = hwnd
        self.__count = 0
        self.__class_name = win32gui.GetClassName(self.__hwnd)
        self.__id = win32gui.GetDlgCtrlID(hwnd)
    def get_class_name(self):
        return self.__class_name
    def get_count(self):
        return self.__count
    def get_hwnd(self):
        return self.__hwnd
    def get_id(self):
        """
        if self.__id == 0:
        raise error
            """
        return self.__id
    def add_count(self):
        self.__count += 1
