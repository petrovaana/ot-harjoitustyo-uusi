#Asked help from copilot to explain the coursematerial on how to connect database so the Database_file and the idea was explained by it, but the code for creating the table was mine
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
