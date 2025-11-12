import sqlite3
from config import DATABASE_FILE_PATH

def initialize():
    conn = sqlite3.connect(DATABASE_FILE_PATH)
    cursor = conn.cursor()


    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL
                   )
                   ''')
    
    conn.commit()
    conn.close()


if __name__=="__main__":
    initialize()