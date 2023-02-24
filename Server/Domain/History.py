from .message import *
from pydantic import BaseModel
class HistoryBase(BaseModel):
    usernames: list[str] = []
    messages: list[Message] = []

class History(HistoryBase):
    def add_message(self, m: Message):
        self.messages.append(m)
        user = m.username
        if not (user in self.usernames):
            self.usernames.append(user)

    def search_by_date(self, date: datetime) -> list[Message]:
        searched_messages = []
        for message in self.messages:
            if message.date == date:
                searched_messages.append(message)

        return searched_messages

    def search_by_username(self, username: str) -> list[Message]:
        searched_messages = []
        for message in self.messages:
            if message.username == username:
                searched_messages.append(message)

        return searched_messages

    def search_by_word(self, search_word: str) -> list[Message]:
        searched_messages = []
        for message in self.messages:
            if message.type is Type.string:
                split_message = str(message.message).split()
                for word in split_message:
                    if word == search_word:
                        searched_messages.append(message)

        return searched_messages

    class Config:
        orm_mode = True