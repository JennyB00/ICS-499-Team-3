from socket import *
import sys, threading
BUFFER = 16384
HOST = "0.0.0.0"
PORT = 0
ADDR = (HOST,PORT)

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(ADDR)