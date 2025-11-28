"""Contains a class for handling the logics of the incomes"""

from repositories.incomes_repository import income_repository

class IncomesService:
    """Application logic class for incomes"""
    def __init__(self, repo=income_repository):
        """Constuctor of the class.
            
            Args:
                income_repository: An object that provides IncomesRepository class.
                    """
        self.repo = repo

    def get_all_incomes(self, username):
        """Requests all incomes based on username through incomes repository"""
        incomes = self.repo.find_all_incomes_by_username(username)
        return incomes

    def add_income(self, username, amount, content):
        """Requests income repository to add a income into database"""
        self.repo.add_income(username, amount, content)

    def sum_numbers(self, username):
        """Requests summed up all the incomes based on username"""
        incomes = self.repo.user_all_logged_incomes_sum(username)
        return incomes

    def delete_income(self, id):
        """Requests repository layer to delete an income based on id"""
        self.repo.delete_one(id)
