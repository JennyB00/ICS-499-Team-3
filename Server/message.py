import time
class Message:
    uid = int()
    username = str()
    message = bytearray()
    messageType = str()
    date = time.time()

    def createMessage(self, messageType, message):
        self.messageType = messageType
        self.message = message
        return message

    def getMessage():
        return message

    def getUser():
        return username
