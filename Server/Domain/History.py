from .message import *
class History:
    def __init__(self, usernames: list):
        self.usernames = usernames
        self.messages = []

    def add_to_history(self, message: Message):
        self.messages.append(message)

    def remove_from_history(self, message: Message):
        self.messages.remove(message)

    def search_by_date(self, date) -> list:
        searchedMessages = []
        for message in self.messages:
            if message.getDate() == date:
                searchedMessages.append(message)

        return searchedMessages

    def search_by_username(self, username: str) -> list:
        searchedMessages = []
        for message in self.messages:
            if message.getUser() == username:
                searchedMessages.append(message)

        return searchedMessages

    def search_by_word(self, searchWord) -> list:
        searchedMessages = []
        for message in self.messages:
            splitMessage = message.split()
            for word in splitMessage:
                if word == searchWord:
                    searchedMessages.append(message)

        return searchedMessages
      
from pydantic import BaseModel
class HistoryBase(BaseModel):
    pass

class HistoryPy(HistoryBase):
    usernames: list[str] = []
    messages: list[MessagePy] = []
