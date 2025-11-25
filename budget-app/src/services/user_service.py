"""Contains a  class for handling the logics of the accounts"""
from repositories.user_repository import user_repository


class UserService:
    """
    Application logic class for accounts
    """
    def __init__(self, repo=user_repository):
        """Constructor of the class.
        
            Args:
                user_repository:An object that provides UserRepository class.
                """
        self.repo = repo
        self._current_user = None

    def create_user(self, username, password):
        """Creates a user, by adding username and password through repository"""
        if self.repo.find_username(username):
            return False
        self.repo.add_user(username, password)
        return True

    def find_user(self, username):
        """Searches for a user based on a username through repository"""
        if self.repo.find_username(username):
            return True
        return False

    def login(self, username, password):
        """Requests from repository to check if account exists, if does logs in the user"""
        user = self.repo.find_account(username, password)
        if not user:
            return False
        self._current_user = user[0]
        return True

    def get_current_user(self):
        """Returns to ui level current account"""
        return self._current_user

    def logout(self):
        """Logs out an acount"""
        self._current_user = None
