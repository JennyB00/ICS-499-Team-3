from .bot import Bot
class Contacts:
    def __init__(self) -> None:
        self.users = []

    def add(self, User: str):
        self.users.append(User)

    def remove(self, User: str):
        self.users.remove(User)

    def getUsers(self) -> list:
        return self.users

    def invite(self, userEmail: str):
        result = False
        # send invite, if successful set result to True

        return result
