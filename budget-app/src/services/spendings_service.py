"""Contains a class for handling the logics of the spendings"""
from repositories.spendings_repository import spending_repository

class SpendingsService:
    """Application logic class for spendings"""
    def __init__(self, repo=spending_repository):
        """Constuctor of the class.
            
            Args:
                spending_repository: An object that provides SpendingsRepository class.
                    """
        self.repo = repo

    def get_all_spendings(self, username):
        """Requests all spendings based on username through spendings repository"""
        spendings = self.repo.find_all_spendings_by_username(username)
        return spendings

    def add_spending(self, username, amount, content):
        """Requests spendings repository to add a spending into database"""
        self.repo.add_spending(username, amount, content)

    def sum_numbers(self, username):
        """Requests summed up all the spendings based on username"""
        spendings = self.repo.user_all_logged_spendings_sum(username)
        return spendings
