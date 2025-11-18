#from entities.user import User
from repositories.user_repository import user_repository

class UserService:
    def __init__(self, repo=user_repository):
        self.repo = repo

#tää tarkistaa et onks nimi jo käytös (find_username) ja sit callaa add_userin 
    def create_user(self, username, password):
        if self.repo.find_username(username, password):
            return False
        self.repo.add_user(username, password)

#Tarkistaa loginin et ois oikeet username ja salasana 
    def login(self, username, password):
        if not self.repo.find_account(username, password):
            return False
        return True
