#Aattelin et tänne vois lisätä kaikki menoihin liittyvät luokat

class SpendingsLogged:
    def __init__(self, username=None, amount, content):
        self.username = username
        self.amount = amount
        self.content = content

class MonthlySpendings:
    def __init__(self, username=None, amount, content):
        self.username = username
        self.amount = amount
        self.content = content

class Income:
    def __init__(self, username=None, amount, content):
        self.username = username
        self.amount = amount
        self.content = content