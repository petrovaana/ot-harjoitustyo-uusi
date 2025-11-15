from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists users;
    ''')

    cursor.execute('''
        drop table if exists logged_spendings;
    ''')

    cursor.execute('''
        drop table if exists income;
    ''')

    cursor.execute('''
        drop table if exists monthly_spendings;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table users (
            username text primary key,
            password text
        );
    ''')

    cursor.execute('''
        create table logged_spendings (
            username TEXT,
            amount INTEGER,
            content text,
            FOREIGN KEY(username) REFERENCES users(username)
        );
    ''')

    cursor.execute('''
        create table income (
            username TEXT,
            amount INTEGER,
            content text,
            FOREIGN KEY(username) REFERENCES users(username)
        );
    ''')

    cursor.execute('''
        create table monthly_spendings (
            username TEXT,
            amount INTEGER,
            content text,
            FOREIGN KEY(username) REFERENCES users(username)
        );
    ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()