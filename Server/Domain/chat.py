from message import Message
from History import History
from privileges import Privileges

class Chat:
    uid = 0
    def __init__(self, userID: str):
        self.uid = uid
        uid = uid + 1
        self.history = History([userID])
        self.activeMembers = []
        self.privileges = [Privileges]
        self.privileges.append(Privileges(userID, True, True, True))

    def join(self, user: str):
        self.activeMembers.append(user)

    def leave(self, user: str):
        self.activeMembers.remove(user)

    def sendMessage(self, message: Message) -> bool:
        self.history.add_to_history(message)
        return True

    def loadHistory(self) -> History:
        return self.history

    def getID(self) -> int:
        return self.uid

    def deleteMessage(self, message) -> bool:
        self.history.remove_from_history(message)
        return True

    def getPrivilege(self, user:str) -> Privileges:
        for p in self.privileges:
            if p.username is user:
                return p
        return None

    def getPrivileges(self):
        return self.privileges
