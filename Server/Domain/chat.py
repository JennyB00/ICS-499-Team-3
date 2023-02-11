from .Domain.account import Account
from .message import Message
from .History import History

class Chat:
    def __init__(self, uid: int, userID: str):
        self.uid = uid
        self.userID = userID
        self.history = History([userID])
        self.activeMembers = [userID]

    def join(self, user: Account):
        self.activeMembers.append(user)

    def leave(self, user):
        self.activeMembers.remove(user)

    def sendMessage(self, message: Message) -> bool:
        self.history.add_to_history(message)
        return True

    def loadHistory(self) -> History:
        return self.history

    def getID(self) -> int:
        return self.uid

    def addUser(self, username):
        self.activeMembers.append(username)

    #not sure if this should stay since join method does the same thing basically

    #Deletes itself, perhaps wrong scope, gets deleted not deletes self
    def delete(self) -> bool:
        pass

    def deleteMessage(self, message) -> bool:
        self.history.remove_from_history(message)
        return True
