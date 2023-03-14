from .message import Message
from .privileges import Privileges
from pydantic import BaseModel

class ChatCreate(BaseModel):
    pass

class ChatUpdate(BaseModel):
    pass

class Chat(BaseModel):
    id: int
    messages: list[Message]
    privileges: list[Privileges]
    # active: list[str] = []
    # def get_privilege(self, user:str) -> (Privileges | None):
    #     for p in self.privileges:
    #         if p.username is user:
    #             return p
    #     return None

    class Config:
        orm_mode = True
