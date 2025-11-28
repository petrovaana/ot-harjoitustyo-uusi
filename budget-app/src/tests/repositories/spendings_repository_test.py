import unittest
from repositories.spendings_repository import spending_repository
from repositories.user_repository import user_repository
from entities.user import User

class TestSpengingsRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        spending_repository.delete_all()

        self.user_esimerkki = User('esimerkki', 'esimerkki123')
        self.user_olio = User('olio', 'olio123')


    def test_add_spending(self):
        spending_repository.add_spending(self.user_esimerkki.username, 5, "ruoka")
        spends = spending_repository.find_all_spendings_by_username(self.user_esimerkki.username)

        self.assertEqual(len(spends), 1)
        self.assertEqual(spends[0].amount, 5)
        self.assertEqual(spends[0].content, "ruoka")
        self.assertEqual(spends[0].username, "esimerkki")

    def test_find_all_spendings_by_username(self):
        spending_repository.add_spending(
            self.user_esimerkki.username, 5, "ruoka")
        spending_repository.add_spending(
            self.user_esimerkki.username, 3, "kissa")

        spendings_esim = spending_repository.find_all_spendings_by_username(self.user_esimerkki.username)

        self.assertEqual(len(spendings_esim), 2)
        self.assertEqual(spendings_esim[0].amount, 5)
        self.assertEqual(spendings_esim[1].amount, 3)
        self.assertEqual(spendings_esim[0].content, "ruoka")
        self.assertEqual(spendings_esim[1].content, "kissa")

    def test_find_all_spendings_based_on_name_empty(self):
        speending = spending_repository.find_all_spendings_by_username("None-existing")
        self.assertEqual(speending, [])

    def test_user_all_logged_spendings_sum(self):
        spending_repository.add_spending(
            self.user_olio.username, 5, "ruoka")
        spending_repository.add_spending(
            self.user_olio.username, 10, "ruoka")
        spending_repository.add_spending(
            self.user_esimerkki.username, 20, "testi")
        spending_repository.add_spending(
            self.user_esimerkki.username, 20, "testi")

        all_spending_olio = spending_repository.user_all_logged_spendings_sum(self.user_olio.username)
        all_spending_esim = spending_repository.user_all_logged_spendings_sum(self.user_esimerkki.username)

        self.assertEqual(all_spending_olio, 15)
        self.assertEqual(all_spending_esim, 40)

    def test_user_no_logged_spendings(self):
        all_spending_olio = spending_repository.user_all_logged_spendings_sum(self.user_olio.username)
        self.assertEqual(all_spending_olio, 0)

    def test_delete_all_logged_spending(self):
        spending_repository.add_spending(self.user_esimerkki.username, 30, "Testi")
        spending_repository.add_spending(self.user_esimerkki.username, 20, "Testi")
        spending_repository.add_spending(self.user_olio.username, 10, "Testi")

        spendings = spending_repository.user_all_logged_spendings_sum(self.user_esimerkki.username)
        spendings2 = spending_repository.user_all_logged_spendings_sum(self.user_olio.username)

        self.assertEqual(spendings, 50)
        self.assertEqual(spendings2, 10)

        spending_repository.delete_all()

        spendings = spending_repository.user_all_logged_spendings_sum(self.user_esimerkki.username)
        spendings2 = spending_repository.user_all_logged_spendings_sum(self.user_olio.username)

        self.assertEqual(spendings, 0)
        self.assertEqual(spendings2, 0)

    def test_delete_one_logged_spending(self):
        spending_repository.add_spending(self.user_esimerkki.username, 30, "Testi")
        spending_repository.add_spending(self.user_esimerkki.username, 20, "Testi")

        spendings = spending_repository.user_all_logged_spendings_sum(self.user_esimerkki.username)

        self.assertEqual(spendings, 50)

        spending_repository.delete_one(1)

        spendings = spending_repository.user_all_logged_spendings_sum(self.user_esimerkki.username)

        self.assertEqual(spendings, 20)
