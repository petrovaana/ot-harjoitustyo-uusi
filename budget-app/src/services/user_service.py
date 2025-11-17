from entities.user import User
from repositories.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.repo = UserRepository()
    
    def create_user(self, username, password):
        if self.repo.find_by_username(username):
            return False
        else:
            self.repo.add_user(username, password)
            return True
    
    #def user_check(self, username, password, password2):
    #    if self.repo.find_by_username(username):
    #        raise ValueError("Username already exists")
    #    
    #    if password != password2:
    #        raise ValueError("Passwords do not match")
    #    
    #    if len(password) < 8:
    #        raise ValueError("Password needs to be at least 8 characters")