import unittest
from repositories.spendings_repository import spending_repository
from repositories.user_repository import user_repository
from entities.user import User

class TestSpengingsRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()

        self.user_esimerkki = User('esimerkki', 'esimerkki123')
        self.user_olio = User('olio', 'olio123')

        spending_repository.delete_all()

    def test_add_spending(self):
        spending_repository.add_spending(self.user_esimerkki.username, 5, "ruoka")
        spends = spending_repository.find_all_spendings_by_username(self.user_esimerkki.username)

        self.assertEqual(len(spends), 1)
        self.assertEqual(spends[0].amount, 5)

    def test_find_all_spendings_by_username(self):
        spending_repository.add_spending(
            self.user_esimerkki.username, 5, "ruoka")
        spending_repository.add_spending(
            self.user_olio.username, 3, "kissa")

        spendings_esim = spending_repository.find_all_spendings_by_username(self.user_esimerkki.username)
        spendings_olio = spending_repository.find_all_spendings_by_username(self.user_olio.username)

        self.assertEqual(len(spendings_esim), 1)
        self.assertEqual(len(spendings_olio), 1)
        self.assertEqual(spendings_esim[0].amount, 5)
        self.assertEqual(spendings_olio[0].amount, 3)

    def test_user_all_logged_spendings_sum(self):
        spending_repository.add_spending(
            self.user_olio.username, 5, "ruoka")
        spending_repository.add_spending(
            self.user_esimerkki.username, 10, "ruoka")

        all_spent_esim = spending_repository.user_all_logged_spendings_sum(self.user_esimerkki.username)

        self.assertEqual(all_spent_esim, 10)
