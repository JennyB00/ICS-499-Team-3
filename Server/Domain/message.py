import time
from datetime import datetime
class Message:

    def __init__(self, user: str, messageType: str, message:bytearray, date=time.time()):
        #self.id = id
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

from pydantic import BaseModel
class MessageBase(BaseModel):
    username: str
    date: datetime
    type: str
    message: bytes

class MessageCreate(MessageBase):
    pass

class MessagePy(MessageBase):
    class Config:
        orm_mode = True