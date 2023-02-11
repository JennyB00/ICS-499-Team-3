class Privileges:

    def __init__(self, addU: bool, deleteM: bool, deleteC: bool, send=True, recieve=True) -> None:
        self.send = send
        self.recieve = recieve
        self.addUser = addU
        self.deleteMessage = deleteM
        self.deleteChat = deleteC


    def getFull(self) -> dict:
        return {"send":self.send,"recieve":self.recieve,"addUser":self.addUser,
        "deleteMessage":self.deleteMessage,"deleteChat":self.deleteChat}

    def getSend(self) -> bool:
        return self.send

    def setSend(self, s:bool):
        self.send = s

    def getRecieve(self) -> bool:
        return self.recieve

    def setRecieve(self, r:bool):
        self.recieve = r

    def getAddUser(self) -> bool:
        return self.addUser

    def setAddUser(self, a: bool):
        self.addUser = a

    def getDeleteMessage(self) -> bool:
        return self.deleteMessage

    def setDeleteMessage(self, dm: bool):
        self.deleteMessage = dm

    def getDeleteChat(self) -> bool:
        return self.deleteChat

    def setDeleteChat(self, dc: bool):
        self.deleteChat = dc