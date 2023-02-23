from datetime import datetime
from enum import Enum
from pydantic import BaseModel

class Type(str, Enum):
    string = 'str'

class MessageBase(BaseModel):
    username: str
    date: datetime
    type: Type
    message: bytes

class MessageCreate(MessageBase):
    pass

class Message(MessageBase):
    class Config:
        orm_mode = True
        allow_mutation = False