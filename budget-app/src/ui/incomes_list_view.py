from tkinter import constants
import tkinter as tk

class IncomesListView:
    def __init__(self, root, incomes, user, handle_delete_income):
        self._root = root
        self._incomes = incomes
        self._user = user

        self._handle_delete_income = handle_delete_income
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_income_item(self, income):
        item_frame = tk.Frame(
            master=self._frame,
            bg="#b5c99a"
            )

        label = tk.Label(
            master=item_frame,
            text=f"{income.content}: {income.amount}€",
            bg="#c8d5b9"
            )

        delete_button = tk.Button(
            master=item_frame,
            text="Delete",
            command=lambda: self._handle_delete_income(income.id),
            bg="#718355"
        )

        label.grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
            sticky=constants.W
            )

        delete_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.W
        )

        item_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = tk.Frame(master=self._root, bg="#c8d5b9")

        for income in self._incomes:
            self._initialize_income_item(income)
