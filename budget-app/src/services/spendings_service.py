from repositories.spendings_repository import spending_repository

class SpendingsService:
    def __init__(self, repo=spending_repository):
        self.repo = repo

    def get_all_spendings(self, username):
        spendings = self.repo.find_all_spendings_by_username(username)
        return spendings

    def add_spending(self, username, amount, content):
        self.repo.add_spending(username, amount, content)

    def sum_numbers(self, username):
        spendings = self.repo.user_all_logged_spendings_sum(username)
        return spendings