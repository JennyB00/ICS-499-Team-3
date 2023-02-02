import hashlib
import random

class account:
    username = str()
    password = str()
    status = str()
    pastChats = list()
    privileges = list ()
    contacts =  list ()

    # account creation and password hashing
    def createAccount():
        username = input("Enter a username: ")
        password = input("Enter password: ")
        confirm_password = input("Confirm password: ")
        if confirm_password == password:
            enc = confirm_password.encode()
            hash1 = hashlib.md5(enc).hexdigest()
            with open("loginDetails.txt", 'a') as f:
                f.write(username + "\n")
                f.write(hash1)
            f.close()
            print("Account creation successful!")
        else:
            print("Passwords did not match! \n")
    # login
    # courrently only works for one user and you'll have to keep deleting info in txt
    def login():
        username = input("Enter Username: ")
        password = input("Enter password: ")
        auth = password.encode()
        auth_hash = hashlib.md5(auth).hexdigest()
        with open("loginDetails.txt", "r") as f:
            stored_username, stored_password = f.read().split("\n")
        f.close()
        if username == stored_username and auth_hash == stored_password:
            print("Logged in Successfully!")
        else:
            print("Login failed! \n")

    

    def createChat():
        #generating a random number between 0 and 100
        chatId = random.randint(0,100)
        # some code to check if a chat with that ID already exists
        return chatId
    
    def joinChat(self,chatId):
        # check if ID is equal to any chat ID in database of txt
        # if chatID == something:
        #    print ("Successfullly joined Chat!")
        # else:
        #   print("Chat joining was unsucessfful")
        return None


    # don't know what to do with these yet    
    def loadContacts(contacts):
         return contacts
    
    # don't know what to do with these yet
    def loadPrivileges(privileges):
        return privileges

    while 1:
        # simple login system screen
        print("********** Login System **********")
        print("1.Create Account")
        print("2.Login")
        print("3.Exit")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            createAccount()
        elif ch == 2:
            login()
        elif ch == 3:
            break
        else:
            print("Wrong Choice!")
