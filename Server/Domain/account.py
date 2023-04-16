from enum import Enum
from .contacts import Contact
from .past_chat import PastChat
from pydantic import BaseModel

class Status(str, Enum):
    online = "online"
    offline = "offline"

"""The user account class"""
class AccountBase(BaseModel):
    username: str
    status: Status

class AccountCreate(AccountBase):
    password: str

class Account(AccountBase):
    contacts: list[Contact]
    past_chats: list[PastChat]

    class Config:
        orm_mode = True
