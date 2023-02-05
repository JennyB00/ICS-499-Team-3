class Contacts:
    users = list()

    def add(self, User):
        self.users.append(User)

    def remove(self, User):
        self.users.remove(User)

    def getUsers(self):
        return self.users

    def invite(self, user):
        result = False
        # send invite, if successful set result to True

        return result
