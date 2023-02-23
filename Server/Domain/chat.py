from .message import Message
from .History import *
from .privileges import *
from pydantic import BaseModel

class ChatBase(BaseModel):
    pass

class ChatCreate(ChatBase):
    pass

class Chat(ChatBase):
    id: int
    history: History = History()
    active: list[str] = []
    privileges: list[Privileges] = []

    def get_privilege(self, user:str) -> Privileges:
        for p in self.privileges:
            if p.username is user:
                return p
        return None

    class Config:
        orm_mode = True
