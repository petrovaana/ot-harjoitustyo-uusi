import unittest
from repositories.incomes_repository import income_repository
from repositories.user_repository import user_repository
from entities.user import User

class TestIncomesRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()

        self.user_elli = User('elli', 'elli123')
        self.user_emmi = User('emmi', 'emmi123')

        income_repository.delete_all()

    def test_add_income(self):
        income_repository.add_income(self.user_elli.username, 5, "ruoka")
        incomes = income_repository.find_all_incomes_by_username(self.user_elli.username)

        self.assertEqual(len(incomes), 1)
        self.assertEqual(incomes[0].amount, 5)
        self.assertEqual(incomes[0].content, "ruoka")
        self.assertEqual(incomes[0].username, "elli")


    def test_find_all_incomes_by_username(self):
        income_repository.add_income(
            self.user_elli.username, 5, "ruoka")
        income_repository.add_income(
            self.user_elli.username, 3, "kissa")

        elli_incomes = income_repository.find_all_incomes_by_username(self.user_elli.username)

        self.assertEqual(len(elli_incomes), 2)
        self.assertEqual(elli_incomes[0].amount, 5)
        self.assertEqual(elli_incomes[1].amount, 3)
        self.assertEqual(elli_incomes[0].content, "ruoka")
        self.assertEqual(elli_incomes[1].content, "kissa")

    def test_find_all_incomes_by_username_empty(self):
        incomes = income_repository.find_all_incomes_by_username("None-existing")
        self.assertEqual(incomes, [])

    def test_user_all_logged_incomes_sum(self):
        income_repository.add_income(
            self.user_elli.username, 5, "ruoka")
        income_repository.add_income(
            self.user_elli.username, 10, "ruoka")
        income_repository.add_income(
            self.user_emmi.username, 20, "testi")
        income_repository.add_income(
            self.user_emmi.username, 20, "testi")

        all_income_elli = income_repository.user_all_logged_incomes_sum(self.user_elli.username)
        all_income_emmi = income_repository.user_all_logged_incomes_sum(self.user_emmi.username)

        self.assertEqual(all_income_elli, 15)
        self.assertEqual(all_income_emmi, 40)

    def test_user_no_logged_incomes(self):
        all_income_elli = income_repository.user_all_logged_incomes_sum(self.user_elli.username)
        self.assertEqual(all_income_elli, 0)

    def test_delete_all_logged_income(self):
        income_repository.add_income(self.user_emmi.username, 30, "Testi")
        income_repository.add_income(self.user_emmi.username, 20, "Testi")
        income_repository.add_income(self.user_elli.username, 10, "Testi")

        incomes = income_repository.user_all_logged_incomes_sum(self.user_emmi.username)
        incomes2 = income_repository.user_all_logged_incomes_sum(self.user_elli.username)

        self.assertEqual(incomes, 50)
        self.assertEqual(incomes2, 10)

        income_repository.delete_all()

        incomes = income_repository.user_all_logged_incomes_sum(self.user_emmi.username)
        incomes2 = income_repository.user_all_logged_incomes_sum(self.user_elli.username)

        self.assertEqual(incomes, 0)
        self.assertEqual(incomes2, 0)

    def test_delete_one_logged_income(self):
        income_repository.add_income(self.user_emmi.username, 30, "Testi")
        income_repository.add_income(self.user_emmi.username, 20, "Testi")

        incomes = income_repository.user_all_logged_incomes_sum(self.user_emmi.username)

        self.assertEqual(incomes, 50)

        income_repository.delete_one(1)

        incomes = income_repository.user_all_logged_incomes_sum(self.user_emmi.username)

        self.assertEqual(incomes, 20)
