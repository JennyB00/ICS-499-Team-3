import hashlib
import random
from .contacts import Contact
from .past_chat import PastChat
from .bot import Bot
from pydantic import BaseModel


"""The user account class"""
class AccountBase(BaseModel):
    username: str
    status: str

class AccountCreate(AccountBase):
    password: str

class Account(AccountBase):
    contacts: list[Contact]
    past_chats: list[PastChat]
    bot: Bot = Bot()
    # def login(self) -> None:
    #     self.status = "online"
    # def logout(self) -> None:
    #     self.status = "online"
    # def online(self) -> bool:
    #     return self.status == "online"
    class Config:
        orm_mode = True


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
        
    # def join_chat(self, chat: Chat):
        # check if ID is equal to any chat ID in database of txt
        # if chatID == something:
        #    print ("Successfullly joined Chat!")
        # else:
        #   print("Chat joining was unsucessfful")

        
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