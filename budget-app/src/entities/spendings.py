"""Contains a class that represents a single spending"""

class Spendings:
    """
        Initializes a new income entry.

        Attributes:
            username: describes who's income is in question
            amount: describes amoun of income
            content: describes the content of income
        """
    def __init__(self, amount, content, username):
        """
        Classes constructor that creates a new spengin

        Arggs:
            username: text that describes the user of an spending
            amount: float that describes the amount of an spending
            content: text that describes the content of an spending
        """
        self.username = username
        self.amount = amount
        self.content = content
