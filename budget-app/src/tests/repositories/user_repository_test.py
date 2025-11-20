import unittest
from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_esimerkki = User('esimerkki', 'esimerkki123')
        self.user_olio = User('olio', 'olio123')

    def test_create(self):
        user_repository.add_user(
            self.user_esimerkki.username, self.user_esimerkki.password)
        users = user_repository.find_all()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, self.user_esimerkki.username)

    def test_find_all(self):
        user_repository.add_user(
            self.user_esimerkki.username, self.user_esimerkki.password)
        user_repository.add_user(
            self.user_olio.username, self.user_olio.password)

        users = user_repository.find_all()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].username, self.user_esimerkki.username)
        self.assertEqual(users[1].username, self.user_olio.username)

    def test_find_username(self):
        user_repository.add_user(
            self.user_esimerkki.username, self.user_esimerkki.password)
        exists = user_repository.find_username(self.user_esimerkki.username)

        self.assertTrue(exists)

    def test_find_account(self):
        user_repository.add_user(
            self.user_esimerkki.username, self.user_esimerkki.password)
        user = user_repository.find_account(
            self.user_esimerkki.username, self.user_esimerkki.password)

        self.assertEqual(user[0], self.user_esimerkki.username)

    def test_find_nonexisting_username(self):
        exists = user_repository.find_username(self.user_esimerkki.username)

        self.assertFalse(exists)

    def test_delete_all(self):
        user_repository.add_user(
            self.user_esimerkki.username, self.user_esimerkki.password)
        user_repository.add_user(
            self.user_olio.username, self.user_olio.password)

        user_repository.delete_all()
        users = user_repository.find_all()

        self.assertEqual(len(users), 0)

# Tää ois uus testi testaa tätä sit jos coverage toimii
    def test_find_nonexisting_account(self):
        user_repository.add_user(
            self.user_esimerkki.username, self.user_esimerkki.password)
        user = user_repository.find_account(
            self.user_olio.username, self.user_olio.password)

        self.assertEqual(user, None)
