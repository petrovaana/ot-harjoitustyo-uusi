"""Contains a class that represents a single income"""

class Income:
    """
        Initializes a new income entry.

        Attributes:
            username: describes who's income is in question
            amount: describes amoun of income
            content: describes the content of income
        """
    def __init__(self, amount, content, username=None):
        """
        Classes constructor that creates a new income

        Arggs:
            username: text that describes the user of an income
            amount: float that describes the amount of an income
            content: text that describes the content of an income
        """
        self.username = username
        self.amount = amount
        self.content = content
