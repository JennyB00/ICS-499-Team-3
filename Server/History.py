class History:
    def __init__(self, usernames):
        self.usernames = usernames
        self.messages = Message[]

    def add_to_history(self, message):
        self.messages.append(message)

    def remove_from_history(self, message):
        self.messages.remove(message)

    def search_by_date(self, date) -> Message[]:
        searchedMessages = Message[]
        for message in self.messages:
            if message.getDate() == date:
                searchedMessages.append(message)

        return searchedMessages

    def search_by_username(self, username) -> Message[]:
        searchedMessages = Message[]
        for message in self.messages:
            if message.getUser() == username:
                searchedMessages.append(message)

        return searchedMessages

    def search_by_word(self, searchWord) -> Message[]:
        searchedMessages = Message[]
        for message in self.messages:
            splitMessage = message.split()
            for word in splitMessage:
                if word == searchWord:
                    searchedMessages.append(message)

        return searchedMessages
      
