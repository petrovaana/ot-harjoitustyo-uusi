import tkinter as tk
from tkinter import constants, ttk
from services.spendings_service import SpendingsService
from services.user_service import UserService

class SpendingsListView:
    def __init__(self, root, spendings, user):
        self._root = root
        self._spendings = spendings
        self._frame = None
        self._user = user

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_spending_item(self, spending):
        item_frame = ttk.Frame(master=self._frame)
        label = ttk.Label(master=item_frame, text=f"{spending.content} {spending.amount}")

        label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for spending in self._spendings:
            self._initialize_spending_item(spending)

class LoggedInView:
    def __init__(self, root, show_login_view, show_create_spending_view, username):
        self.ss = SpendingsService()
        self.us = UserService()

        self._show_create_spending_view = show_create_spending_view
        self._root = root
        self._frame = None
        self._show_login_view = show_login_view
        self._user = username

        self._spending_list_frame = None
        self._spending_list_view = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout_handler(self):
        self.us.logout()
        self._show_login_view()

    def _initialize_header(self):
        label = tk.Label(master=self._frame, text="Welcome to Budget-App!", font=("Segoe UI", 16, "bold"))
        label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)

        logout_button = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._logout_handler
        )
        logout_button.grid(row=0, column=2, sticky=constants.E, padx=5, pady=5)

    def _initialize_spending_list(self, user):
        if self._spending_list_view:
            self._spending_list_view.destroy()

        spendings = self.ss.get_all_spendings(user)

        self._spending_list_view = SpendingsListView(
            self._spending_list_frame,
            spendings,
            user
        )
        #self._spending_list_view.grid(row=0, column=0, sticky="ew")

    def _initialize_buttons(self):
        new_spending_button = ttk.Button(
            master=self._frame,
            text="Log in new spending",
            command=lambda: self._show_create_spending_view(self._user)
        )

        new_income_button = ttk.Button(
            master=self._frame,
            text="Log in new income"
        )

        new_spending_button.grid(
            row=4,
            column=0,
            padx=5,
            pady=5
        )

        new_income_button.grid(
            row=4,
            column=1,
            padx=5,
            pady=5
        )

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._spending_list_frame = ttk.Frame(master=self._frame)
        self._spending_list_frame.pack()

        self._initialize_header()
        self._initialize_spending_list(self._user)
        self._initialize_buttons()