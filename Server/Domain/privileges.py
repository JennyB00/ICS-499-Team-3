from pydantic import BaseModel

class PrivilegesBase(BaseModel):
    username: str
    send: bool
    recieve: bool
    add_user: bool
    delete_message: bool
    delete_chat: bool

class PrivilegesCreate(PrivilegesBase):
    chat_id: int

class Privileges(PrivilegesBase):
    class Config:
        orm_mode = True