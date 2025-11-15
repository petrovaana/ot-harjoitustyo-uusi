from entities.user import User
from entities.spendings import Spendings
from database_connection import get_database_connection

class SpendingsRepository:
    def __init__(self, file_path):
        self._file_path = file_path
    
    def find_all(self):
        return self._read()

    def find_by_username(self, username):
        spendings = self.find_all()

        user_spendings = filter(lambda spending: spending.user and spending.user.username == username, spendings)

        return list(user_spendings)
    
    def create(self, spending):
        spendings = self.find_all()

        spendings.append(spending)