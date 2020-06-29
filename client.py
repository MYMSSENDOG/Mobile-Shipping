#! /usr/bin/python

from socket import *
from select import *
import sys
from time import ctime

HOST = '127.0.0.1'
PORT = 9999
BUFSIZE = 1024
ADDR = (HOST,PORT)
clientSocket = socket(AF_INET, SOCK_STREAM)
try:
    clientSocket.connect(ADDR)
    clientSocket.send(input().endcode())
except  Exception as e:
    print("no connections")
    sys.exit()
