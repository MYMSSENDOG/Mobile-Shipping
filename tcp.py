from socket import *
import json
import threading
import win32gui
import pywintypes
import control_finder
import json
import order_maker
import window_finder
import time

class Server(threading.Thread):
    def __init__(self, socket):
        super().__init__()
        self.s_socket = socket
    def run(self):
        global index
        self.c_socket, addr = self.s_socket.accept()
        print(addr[0], addr[1], "연결")
        index += 1
        create_thread(self.s_socket)
        t = threading.Thread(target = self.c_recv)
        t.daemon = True
        t.start()
        #self.join(t)

    def c_recv(self):
        print("c_recv",self.c_socket)
        while True:
            try:
                data = json.loads(self.c_socket.recv(1024))
                print(data)
                # 메인창 정보를 얻어와 오더접수 띄울 준비
                main_app_name = "인성 퀵 서비스 [윤덕순] / [노원스마트물류-노원스마트물류]"
                main_hwnd, main_childwnds = window_finder.GetChildWindows(main_app_name)
                maincf = control_finder.MainDlgControlFinder()
                window_finder.find_targets(main_childwnds, maincf)
                main_control_dict = maincf.get_control_dict()
                starter = order_maker.NewWindow(main_control_dict)
                starter.new_window_start()

                time.sleep(5)


                order_dlg = "오더접수(신규)"
                hwnd, childwnds = window_finder.GetChildWindows(order_dlg)
                cf = control_finder.OrderControl_Finder()
                window_finder.find_targets(childwnds, cf)
                control_dict = cf.get_control_dict()
                win32gui.SetForegroundWindow(hwnd)
                om = order_maker.OrderMaker(control_dict, data)
                om.make_order()
                om.finalyze()





            except:
                self.c_socket.close()
                print(self.c_socket,  "closed")
                break
        self.c_socket.close()
def create_thread(s_socket):
    global index
    t.append(Server(s_socket))
    #t[index].deamon = True
    t[index].start()

t = []
index = 0
HOST = ""
PORT = 9999
BUfSIZE = 1024
s_socket = (AF_INET, SOCK_STREAM)

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((HOST,PORT))
print("bind")
server_socket.listen(2000)
print("listen")

create_thread(server_socket)
#server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)