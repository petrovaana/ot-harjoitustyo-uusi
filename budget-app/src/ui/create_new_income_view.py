from tkinter import constants, messagebox
import tkinter as tk
from services.user_service import UserService
from services.income_service import IncomesService


class CreateIncomeView:
    """class that creates a view for creating a new income
            Attributes:
                root: Tkinter main frame
                show_logged_in_view: callback function, returns back to logged in view
                username: user to identify who created the income
    """
    def __init__(self, root, show_logged_in_view, username):
        self._root = root
        self._frame = None
        self._show_logged_in_view = show_logged_in_view

        self.us = UserService()
        self.cs = IncomesService()

        self._entry_amount = None
        self._entry_content = None

        self._user = username

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def submit_spending(self):
        amount = self._entry_amount.get()
        content = self._entry_content.get()

        if float(amount) <= 0:
            messagebox.showerror("showerror", "Amount added wrong")
            return

        if len(content) <= 0:
            messagebox.showerror("showerror", "Need to add content")
            return

        else:
            self.cs.add_income(self._user, amount, content)
            self._show_logged_in_view(self._user)

    def _initialize_income_label(self):
        label = tk.Label(
            master=self._frame,
            text="Log in a new income:",
            anchor="center",
            bg="#c8d5b9"
            )

        label.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky=(constants.W + constants.E),
            padx=5,
            pady=5
            )

    def _initialize_amount_field(self):
        amount_label = tk.Label(
            master=self._frame,
            text="Amount: ",
            bg="#c8d5b9"
            )

        self._entry_amount = tk.Entry(
            master=self._frame,
            bg="#e9f5db"
            )

        amount_label.grid(
            row=1,
            column=0,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5
            )

        self._entry_amount.grid(
            row=1,
            sticky=(constants.E, constants.W),
            column=1,
            padx=5,
            pady=5
            )

    def _initialize_content_field(self):
        content_label = tk.Label(
            master=self._frame,
            text="Content: ",
            bg="#c8d5b9"
            )

        self._entry_content = tk.Entry(
            master=self._frame,
            bg="#e9f5db"
            )

        content_label.grid(
            row=2,
            column=0,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5
            )

        self._entry_content.grid(
            row=2,
            column=1,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5
            )

    def _initialize_submit_button(self):
        submit_button = tk.Button(
            master=self._frame,
            text="Submit",
            command=self.submit_spending,
            bg="#718355"
        )

        submit_button.grid(
            row=3,
            column=0,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5
        )

    def _initialize(self):
        self._frame = tk.Frame(master=self._root, bg="#b5c99a")
        self._initialize_income_label()
        self._initialize_amount_field()
        self._initialize_content_field()
        self._initialize_submit_button()
