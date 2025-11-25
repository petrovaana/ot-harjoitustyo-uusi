"""Contains a class that represents a single account"""

class User:
    """
        Initializes a new account.

        Attributes:
            username: describes the name of a user
            password: describes the password of a user
        """
    def __init__(self, username, password):
        """Classes constructor that creates a new user

        Arggs:
            username: text that describes the name of a user
            password: text that describes the password of the account
        """
        self.username = username
        self.password = password
