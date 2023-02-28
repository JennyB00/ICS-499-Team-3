from datetime import datetime
from enum import Enum
from pydantic import BaseModel

class MessageBase(BaseModel):
    username: str
    date: datetime
    type: str = "str"
    message: bytes

class MessageCreate(MessageBase):
    pass

class Message(MessageBase):
    id: int
    class Config:
        orm_mode = True
        allow_mutation = False