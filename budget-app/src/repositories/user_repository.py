from entities.user import User
from database_connection import get_database_connection

class UserRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute("select * from users")
        rows = cursor.fetchall()
        return list(User(row["username"], row["password"]) for row in rows)

    #Tätä käytetään user_services ku tarkistetaan onko käyttäjä olemassa jo
    def find_username(self, username):
        cursor = self._connection.cursor()
        cursor.execute("select 1 from users WHERE username = ?", (username,))
        row = cursor.fetchone()
        return row is not None

    #Käytetään login tarkistukses
    def find_account(self, username, password):
        cursor = self._connection.cursor()
        cursor.execute("select * from users WHERE username = ? and password = ?", (username, password))
        row = cursor.fetchone()
        if row:
            return User(row["username"], row["password"])
        return None

    def add_user(self, username, password):
        cursor = self._connection.cursor()
        cursor.execute("INSERT into users (username, password) values (?, ?)", (username, password))
        self._connection.commit()

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE from users")
        self._connection.commit()

user_repository = UserRepository(get_database_connection())