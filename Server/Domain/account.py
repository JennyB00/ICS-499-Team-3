import hashlib
import random
from chat import Chat
from contacts import Contacts
from bot import Bot

"""The user account class"""
class Account:
    def __init__(self, user: str, passwrd: str, status: str = "online") -> None:
        self.username = user
        self.password = passwrd
        self.status = status
        self.pastChatIDs = []
        self.contacts = Contacts()
        self.bot = Bot()


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

    def addChat(self, chatID: str):
        self.pastChatIDs.append(chatID)
    # def createChat(self):
    #     chat = Chat(self.username)
    #     id = chat.getID()
    #     self.pastChatIDs.append(id)
    #     return id

    # def deleteChat(self, chat):
    #     self.pastChats.remove(chat)
    #     #System call to delete obj
    
    def joinChat(self,chat: Chat):
        # check if ID is equal to any chat ID in database of txt
        # if chatID == something:
        #    print ("Successfullly joined Chat!")
        # else:
        #   print("Chat joining was unsucessfful")

        #this should probably be moved into the if statement
        chat.join(self.username)

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
