class User:
    def __init__(self, username, usertype):
        self.username = username
        self.usertype = usertype

    def get_username(self):
        return self.username

    def get_usertype(self):
        return self.usertype