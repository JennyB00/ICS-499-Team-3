from socket import *
HOST = "0.0.0.0"
PORT = 0
ADDR = (HOST,PORT)

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(ADDR)

