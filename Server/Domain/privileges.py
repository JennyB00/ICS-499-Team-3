from pydantic import BaseModel

class PrivilegesBase(BaseModel):
    username: str
    send: bool
    recieve: bool
    add_user: bool
    delete_message: bool
    delete_chat: bool

class PrivilegesCreate(PrivilegesBase):
    pass

class PrivilegesPy(PrivilegesBase):
    class Config:
        orm_mode = True

class Privileges:
    
    def __init__(self, user: str, addU: bool, deleteM: bool, deleteC: bool, send=True, recieve=True) -> None:
        self.username = user
        self.send = send
        self.recieve = recieve
        self.addUser = addU
        self.deleteMessage = deleteM
        self.deleteChat = deleteC

    def getUser(self) -> str:
        return self.username

    def dict(self) -> dict:
        return {'username':self.username,
                'send':self.send,
                'recieve':self.recieve,
                'addUser':self.addUser,
                'deleteMessage':self.deleteMessage,
                'deleteChat':self.deleteChat}

    # def getFull(self) -> dict:
    #     return {"send":self.send,"recieve":self.recieve,"addUser":self.addUser,
    #     "deleteMessage":self.deleteMessage,"deleteChat":self.deleteChat}

    # def getSend(self) -> bool:
    #     return self.send

    # def setSend(self, s:bool):
    #     self.send = s

    # def getRecieve(self) -> bool:
    #     return self.recieve

    # def setRecieve(self, r:bool):
    #     self.recieve = r

    # def getAddUser(self) -> bool:
    #     return self.addUser

    # def setAddUser(self, a: bool):
    #     self.addUser = a

    # def getDeleteMessage(self) -> bool:
    #     return self.deleteMessage

    # def setDeleteMessage(self, dm: bool):
    #     self.deleteMessage = dm

    # def getDeleteChat(self) -> bool:
    #     return self.deleteChat

    # def setDeleteChat(self, dc: bool):
    #     self.deleteChat = dc