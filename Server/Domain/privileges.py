from pydantic import BaseModel

class PrivilegesBase(BaseModel):
    username: str
    send: bool
    receive: bool
    add_user: bool
    delete_message: bool
    delete_chat: bool

class PrivilegesCreate(PrivilegesBase):
    pass

class Privileges(PrivilegesBase):
    id: int
    class Config:
        orm_mode = True