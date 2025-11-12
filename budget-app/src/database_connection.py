#Asked copilot to explain the connection and used the course material for this
import sqlite3
from config import DATABASE_FILE_PATH


connection = sqlite3.connect(DATABASE_FILE_PATH)
connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection
