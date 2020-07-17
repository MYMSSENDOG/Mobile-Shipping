class Cah:
    def __init__(self, hwnd):
        self.__hwnd = hwnd
        self.__count = 0
        self.__class_name = ""
    def get_class_name(self):
        return self.__class_name
    def get_count(self):
        return self.__count
    def get_hwnd(self):
        return self.__hwnd