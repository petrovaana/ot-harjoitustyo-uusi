"""
    This file connects incomes database and app. 
    The functions request information or log in information.
"""

from entities.incomes import Income
from database_connection import get_database_connection


class IncomesRepository:
    """
    This class is responsible for operations regarding incomes in database
    """
    def __init__(self, connection):
        """Classes constructor.
        Args:
            connection: sets the connection with database
        """
        self._connection = connection

    def find_all_incomes_by_username(self, username):
        """Requests all of the incomes by username"""
        cursor = self._connection.cursor()
        query = """
                SELECT id, amount, content, username
                FROM income
                WHERE username = ?
                """
        cursor.execute(query, (username,))
        rows = cursor.fetchall()

        return [Income(row[0], row[1], row[2], row[3]) for row in rows]

    def user_all_logged_incomes_sum(self, username):
        """Requests all of the users incomes and sums them"""
        cursor = self._connection.cursor()
        query = """
                SELECT SUM(amount)
                FROM income
                WHERE username = ?
                """
        cursor.execute(query, (username,))
        row = cursor.fetchone()[0]
        return row if row else 0

    def add_income(self, username, amount, content):
        """
            Adds a new income into database
            Uses username, amount and content
        """
        cursor = self._connection.cursor()
        query = """
                INSERT into income (username, amount, content)
                VALUES (?, ?, ?)
                """
        cursor.execute(query, (username, amount, content))
        self._connection.commit()

    def delete_all(self):
        """Deletes all logged incomes from database (used for testing)"""
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM income")
        self._connection.commit()

    def delete_one(self, id):
        """Deletes an income from database by id"""
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM income WHERE id = ?", (id,))
        self._connection.commit()

income_repository = IncomesRepository(get_database_connection())
