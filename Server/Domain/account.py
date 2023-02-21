import hashlib
import random
from .chat import Chat
from .contacts import *
from .bot import *

"""The user account class"""
class Account:
    def __init__(self, user: str, passwrd: str, status: str = "online") -> None:
        self.username = user
        self.password = passwrd
        self.status = status
        self.pastChatIDs = []
        self.contacts = Contacts()
        self.bot = Bot()

    def get_username(self) -> str:
        return self.username

    def get_password(self) -> str:
        return self.password

    def get_chats(self) -> list[str]:
        return self.pastChatIDs.copy()

    def add_chat(self, chatID: str):
        self.pastChatIDs.append(chatID)

    def delete_chat(self, chatID: str):
        self.pastChatIDs.remove(chatID)

    def get_contacts(self) -> Contacts:
        return self.contacts

    def get_bot(self) -> Bot:
        return self.bot

    #Sets the account status to online
    def login(self):
        self.status = "online"
        # username = input("Enter Username: ")
        # password = input("Enter password: ")
        # auth = password.encode()
        # auth_hash = hashlib.md5(auth).hexdigest()
        # with open("loginDetails.txt", "r") as f:
        #     stored_username, stored_password = f.read().split("\n")
        # f.close()
        # if username == stored_username and auth_hash == stored_password:
        #     print("Logged in Successfully!")
        # else:
        #     print("Login failed! \n")

    def logout(self):
        self.status = "offline"

    def getStatus(self) -> str:
        return self.status

    
    def join_chat(self, chat: Chat):
        # check if ID is equal to any chat ID in database of txt
        # if chatID == something:
        #    print ("Successfullly joined Chat!")
        # else:
        #   print("Chat joining was unsucessfful")

        chat.join(self.username)
        
    # account creation and password hashing
    # def createAccount():
    #     username = input("Enter a username: ")
    #     password = input("Enter password: ")
    #     confirm_password = input("Confirm password: ")
    #     if confirm_password == password:
    #         enc = confirm_password.encode()
    #         hash1 = hashlib.md5(enc).hexdigest()
    #         with open("loginDetails.txt", 'a') as f:
    #             f.write(username + "\n")
    #             f.write(hash1)
    #         f.close()
    #         print("Account creation successful!")
    #     else:
    #         print("Passwords did not match! \n")
    # login
    # courrently only works for one user and you'll have to keep deleting info in txt


    # def getPastChats(self) -> list:
    #     return self.pastChatIDs

    # # don't know what to do with these yet    
    # def getContacts(self) -> Contacts:
    #      return self.contacts
    

    # while 1:
    #     # simple login system screen
    #     print("********** Login System **********")
    #     print("1.Create Account")
    #     print("2.Login")
    #     print("3.Exit")
    #     ch = int(input("Enter your choice: "))
    #     if ch == 1:
    #         createAccount()
    #     elif ch == 2:
    #         login()
    #     elif ch == 3:
    #         break
    #     else:
    #         print("Wrong Choice!")

from pydantic import BaseModel

class AccountBase(BaseModel):
    username: str
    contacts: list[ContactPy] = []

class AccountCreate(AccountBase):
    password: str

class AccountPy(AccountBase):
    status: str
    past_chat_ids: list[str] = []
    bot: BotPy = BotPy()
    class Config:
        orm_mode = True
        