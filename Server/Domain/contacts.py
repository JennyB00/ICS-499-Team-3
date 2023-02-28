from pydantic import BaseModel

class ContactBase(BaseModel):
    contact: str

class ContactCreate(ContactBase):
    pass

class Contact(ContactBase):
    id: int
    class Condig:
        orm_mode = True
