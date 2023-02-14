from socket import *
from Domain.chat import Chat
from Domain.account import Account
from Domain.privileges import Privileges
from Domain.message import Message
import sys, threading
BUFFER = 16384
HOST = "0.0.0.0"
PORT = 0
ADDR = (HOST,PORT)

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(ADDR)

chats = {} #id:obj
users = {} #username:obj


def delete_chat_message(username: str, chatID: int, message: Message):
    chat = chats.get(chatID)
    privileges = chat.getPrivilege(username)
    if privileges.deleteMessage:
        return chat.deleteMessage(message)
    else:
        return False