class Contacts:
    def __init__(self) -> None:
        self.__users = []

    def add(self, user: str):
        self.__users.append(user)

    def remove(self, user: str):
        self.__users.remove(user)

    def get_users(self) -> list[str]:
        return self.__users.copy()

    def invite(self, userEmail: str):
        result = False
        # send invite, if successful set result to True

        return result

from pydantic import BaseModel
class ContactBase(BaseModel):
    contact: str

class ContactCreate(ContactBase):
    owner: str

class ContactPy(ContactBase):
    class Condig:
        orm_mode = True
