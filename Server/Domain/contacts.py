from pydantic import BaseModel

class ContactBase(BaseModel):
    contact: str

class ContactCreate(ContactBase):
    owner_id: str

class Contact(ContactBase):
    class Condig:
        orm_mode = True
