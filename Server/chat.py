class Chat:
    def create_chat(self, userID) -> Chat:
        self.userID = userID
        self.history = History(userID)
        self.activeMembers = User[]
        return self

    def join(self, user):
        self.activeMembers.append(user)

    def leave(self, user):
        self.activeMembers.remove(user)

    def send_message(self, message) -> bool:
        self.history.add_to_history(message)
        return True

    def load_history(self) -> History:
        return self.history

    def get_ID(self) -> int:
        return self.userID

    def add_user(self, username):
        self.activeMembers.append(username)

    #not sure if this should stay since join method does the same thing basically

    def delete(self) -> bool:
    #not sure what the purpose of this method is supposed to be

    def delete_message(self, message) -> bool:
        self.history.remove_from_history(message)
        return True
