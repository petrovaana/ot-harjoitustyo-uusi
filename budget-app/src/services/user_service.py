from repositories.user_repository import user_repository


class UserService:
    def __init__(self, repo=user_repository):
        self.repo = repo
        self._current_user = None

    def create_user(self, username, password):
        if self.repo.find_username(username):
            return False
        self.repo.add_user(username, password)
        return True

    def find_user(self, username):
        if self.repo.find_username(username):
            return True
        else:
            return False

    def login(self, username, password):
        user = self.repo.find_account(username, password)
        if not user:
            return False
        else:
            self._current_user = user[0]
            return True

    def get_current_user(self):
        return self._current_user

    def logout(self):
        self._current_user = None
