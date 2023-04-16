from pydantic import BaseModel

class PastChatBase(BaseModel):
    past_chat_id: int

class PastChatCreate(PastChatBase):
    pass

class PastChat(PastChatBase):
    id: int
    
    class Config:
        orm_mode = True
