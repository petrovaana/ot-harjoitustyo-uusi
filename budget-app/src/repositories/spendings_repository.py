from entities.spendings import Spendings
from database_connection import get_database_connection


class SpendingsRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all_spendings_by_username(self, username):
        cursor = self._connection.cursor()
        cursor.execute(
            "select amount, content, username from logged_spendings WHERE username = ?", (username,))
        rows = cursor.fetchall()

        return [Spendings(row[0], row[1], row[2]) for row in rows]

    def user_all_logged_spendings_sum(self, username):
        cursor = self._connection.cursor()
        cursor.execute(
            "select SUM(amount) from logged_spendings WHERE username = ?", (username,))
        row = cursor.fetchone()[0]
        return row if row else 0

    def add_spending(self, username, amount, content):
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT into logged_spendings (username, amount, content) values (?, ?, ?)", (username, amount, content))
        self._connection.commit()

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM logged_spendings")
        self._connection.commit()


spending_repository = SpendingsRepository(get_database_connection())
