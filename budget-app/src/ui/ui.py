from ui.login_view import LoginView
from ui.create_user_view import CreateUserView
from ui.logged_in_budget_view import LoggedInView
from ui.create_new_spending_view import CreateSpendingView
from services.user_service import UserService
#from ui.create_new_income_view import CreateIncomeView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
        self._us = UserService()

    def start(self):
        self._show_login_view()

    def _show_login_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = LoginView(
            self._root,
            self._show_create_user_view,
            self._show_logged_in_view
        )
        self._current_view.pack()

    def _show_create_user_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = CreateUserView(
            self._root,
            self._show_login_view
        )
        self._current_view.pack()

    def _show_logged_in_view(self, username):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = LoggedInView(
            self._root,
            self._show_login_view,
            self._show_create_spending_view,
            username
        )
        self._current_view.pack()

    def _show_create_spending_view(self, username):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = CreateSpendingView(
            self._root,
            self._show_logged_in_view,
            username
        )
        self._current_view.pack()