import time
class Message:

    def __init__(self, user: str, messageType: str, message:bytearray, date=time.time()):
        self.uid = 10
        self.username = user
        self.messageType = messageType
        self.message = message
        self.date = date

    def getMessage(self) -> bytearray:
        return self.message

    def getMessageType(self) -> str:
        return self.messageType

    def getUser(self) -> str:
        return self.username

    def getDate(self):
        return self.date