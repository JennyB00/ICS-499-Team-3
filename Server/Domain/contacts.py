from pydantic import BaseModel

class ContactBase(BaseModel):
    contact: str

class ContactCreate(ContactBase):
    pass

class Contact(ContactBase):
    id: int

    class Config:
        orm_mode = True
