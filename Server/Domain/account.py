import random
from .contacts import Contact
from .past_chat import PastChat
from .bot import Bot
from pydantic import BaseModel


"""The user account class"""
class AccountBase(BaseModel):
    username: str
    status: str

class AccountCreate(AccountBase):
    password: str

class Account(AccountBase):
    contacts: list[Contact]
    past_chats: list[PastChat]
    bot: Bot = Bot()

    def create_account(self, password: str):
        self.password = hashlib.sha256(password.encode()).hexdigest()
        # Save the account to the database here

    def join_chat(self, chat_id: int):
        # Add the chat to the user's list of past chats and save to database here
        pass

    def delete_account(self):
        # Delete the account from the database here
        pass

    def get_past_chats(self):
        # Retrieve the user's past chats from the database and return them
        pass

    class Config:
        orm_mode = True
