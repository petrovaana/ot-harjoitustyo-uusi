from entities.user import User
#from database_connection import get_database_connection

#Väliaikainen vaihoehto on luoda skirja, että toimii käyttäjän luonti
#En onnistunu luoda tietokantaa vielä, joten tässä on tämän hetkinen ratkaisu
class UserRepository:
    def __init__(self):
        self.users = {}
    
    def add_user(self, username, password):
        user = User(username, password)
        self.users[username] = user
        return user
    
    def find_by_username(self, username):
        return self.users.get(username)

#class UserRepository:
    #def __init__(self, connection):
    #    self._connection = connection
    
    #def find_all(self):
    #    cursor = self._connection.cursor()
    #    cursor.execute("select * from users")
    #    rows = cursor.fetchall()
    #    return [User(row["username"], row["password"]) for row in rows]

    #def find_by_username(self, username):
    #    cursor = self._connection.cursor()
    #    cursor.execute("select * from users WHERE username = ?", (username))
    #    rows = cursor.fetchone()
    #    return [User(row["username"], row["password"]) for row in rows]

    #def create_user(self, user):
    #    cursor = self._connection.cursor()
    #    cursor.execute("INSERT into users (username, password) values (?, ?)", (user.username, user.password))
    #    self._connection.commit()
    #    return user

    #def delete_all(self):
    #    cursor = self._connection.cursor()
    #    cursor.execute("DELETE from users")
    #    self._connection.commit()

#user_repository = UserRepository(get_database_connection())