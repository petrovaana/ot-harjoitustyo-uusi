"""A file that gets the connection for the database"""

import os
import sqlite3
# Have asked AI for help to figure out the database setup so might have done little
# changes to the file with it, but mostly used to understand whats going on

dirname = os.path.dirname(__file__)

def get_database_connection():
    """Gets the database connection, which is later used in the app"""
    connection = sqlite3.connect(os.path.join(
        dirname, "..", "data", "database.sqlite"))
    connection.row_factory = sqlite3.Row

    return connection
