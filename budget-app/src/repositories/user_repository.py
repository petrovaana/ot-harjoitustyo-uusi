"""
    This file connects users database and app. 
    The functions request account information.
"""

from entities.user import User
from database_connection import get_database_connection


class UserRepository:
    """
    This class is responsible for operations regarding users in databaes.
    """
    def __init__(self, connection):
        """Constructor of a class
            Args:
                connection: Creates a connection to database
        """
        self._connection = connection

    def find_all(self):
        """Searches for all accounts (used for testing)"""
        cursor = self._connection.cursor()
        cursor.execute("select * from users")
        rows = cursor.fetchall()
        return list(User(row["username"], row["password"]) for row in rows)

    def find_username(self, username):
        """Checks if a username exists in database"""
        cursor = self._connection.cursor()
        cursor.execute("select 1 from users WHERE username = ?", (username,))
        row = cursor.fetchone()
        return row is not None

    def find_account(self, username, password):
        """Requests username and password from database"""
        cursor = self._connection.cursor()
        cursor.execute(
            "select * from users WHERE username = ? and password = ?", (username, password))
        row = cursor.fetchone()
        if row:
            return (row["username"], row["password"])
        return None

    def add_user(self, username, password):
        """Adds a user in database by adding username and password"""
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT into users (username, password) values (?, ?)", (username, password))
        self._connection.commit()

    def delete_all(self):
        """Deletes all of the database information (Used for testing)"""
        cursor = self._connection.cursor()
        cursor.execute("DELETE from users")
        self._connection.commit()

user_repository = UserRepository(get_database_connection())
