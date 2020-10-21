from socket import *
import threading
import win32gui
import pywintypes
import control_finder
import json
import order_maker
import window_finder
import time
#db 연결 미리
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
                main_control_dict = maincf.get_control_dict()#위에서 쓸 컨트롤의 위치를 찾아 딕셔너리에 저장을 했다. 그것을 여기서 쓰려고 호출
                starter = order_maker.NewWindow(main_control_dict)#실제 작업이 이루어지는 창을 키는 클래스
                starter.new_window_start()

                time.sleep(5)


                order_dlg = "오더접수(신규)"
                hwnd, childwnds = window_finder.GetChildWindows(order_dlg)#아까와 다른점은 부모hwnd의 자식들 중에서만 검사를 함
                cf = control_finder.OrderControl_Finder()#몇번에 뭐가 있는지 정의한 dictionary
                window_finder.find_targets(childwnds, cf)#그것들을 다 찾아낸다.
                control_dict = cf.get_control_dict()#딕셔너리 리턴받는다.
                win32gui.SetForegroundWindow(hwnd)#guia를 실행하기 위해 오더접수 창을 가장 윗단으로 한다.
                om = order_maker.OrderMaker(control_dict, data)#수신한 데이터로 접수 한다.
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