"""
    This file connects spendings database and app. 
    The functions request information or log in information.
"""

from entities.spendings import Spendings
from database_connection import get_database_connection


class SpendingsRepository:
    """
    This class is responsible for operations regarding spendings in database
    """
    def __init__(self, connection):
        """Classes constructor.
        Args:
            connection: sets the connection with database
        """
        self._connection = connection

    def find_all_spendings_by_username(self, username):
        """Requests all of the spendings by username"""
        cursor = self._connection.cursor()
        query = """
                SELECT amount, content, username
                FROM logged_spendings
                WHERE username = ?
                """
        cursor.execute(query, (username,))
        rows = cursor.fetchall()

        return [Spendings(row[0], row[1], row[2]) for row in rows]

    def user_all_logged_spendings_sum(self, username):
        """Requests all of the users spendings and sums them"""
        cursor = self._connection.cursor()
        query = """
                SELECT SUM(amount)
                FROM logged_spendings
                WHERE username = ?
                """
        cursor.execute(query, (username,))
        row = cursor.fetchone()[0]
        return row if row else 0

    def add_spending(self, username, amount, content):
        """
            Adds a new spending into database
            Uses username, amount and content
        """
        cursor = self._connection.cursor()
        query = """
                INSERT into logged_spendings (username, amount, content)
                VALUES (?, ?, ?)
                """
        cursor.execute(query, (username, amount, content))
        self._connection.commit()

    def delete_all(self):
        """Deletes all logged spendings from database (used for testing)"""
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM logged_spendings")
        self._connection.commit()


spending_repository = SpendingsRepository(get_database_connection())
