from .message import *
from pydantic import BaseModel
class HistoryBase(BaseModel):
    pass

class History(HistoryBase):
    usernames: list[str] = []
    messages: list[Message] = []

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