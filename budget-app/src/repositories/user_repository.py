from entities.user import User
from database_connection import get_database_connection

#A start of a user_repository for now
def get_user_by_row(row):
    return User(row["username"], row["password"]) if row else None


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

user_repository = UserRepository(get_database_connection())