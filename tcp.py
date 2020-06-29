from socket import *
import threading
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
                get_data = self.c_socket.recv(1024)
                print(get_data.decode("utf-8"))
            except:
                self.c_socket.close()
                print(self.c_socket,  "closed")
                break

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
server_socket.listen(1)
print("listen")

create_thread(server_socket)
#server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)