from repositories.spendings_repository import spending_repository

class SpendingsService:
    def __init__(self, repo=spending_repository):
        self.repo = repo

    def get_all_spendings(self, username):
        spendings = self.repo.find_all_spendigs_by_username(username)
        return spendings

    def add_spending(self, username, amount, content):
        self.repo.add_spending(username, amount, content)

    def sum_numbers(self, username):
        spendings = self.get_all_spendings(username)
        return sum(float(x.amount) for x in spendings)