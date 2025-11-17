from entities.user import User
from entities.spendings import Spendings
from database_connection import get_database_connection

#Tää on non-sense tällä hetkellä koitin vaan ymmärtää logiikkaa
#ja toiminnallisuutta, eli ei mitään virallista tai ees mun koodia
#Vertailin et mitä repossa ees tapahtuu!
class SpendingsRepository:
    def __init__(self, file_path):
        self._file_path = file_path
    
    def find_all(self):
        return self._read()

    def find_by_username(self, username):
        spendings = self.find_all()

        user_spendings = filter(lambda spending: spending.user and spending.user.username == username, spendings)

        return list(user_spendings)
    
    def get_all(self):
        pass
    
    def create(self, spending):
        spendings = self.find_all()

        spendings.append(spending)