from tkinter import ttk, constants, messagebox
from services.user_service import UserService
from services.income_service import IncomesService


class CreateIncomeView:
    def __init__(self, root, show_logged_in_view, username):
        self._root = root
        self._show_logged_in_view = show_logged_in_view
        self.us = UserService()
        self.cs = IncomesService()
        self._frame = ttk.Frame(master=self._root)

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

    def _initialize_entryfields(self):
        amount_label = ttk.Label(master=self._frame, text="Amount: ")
        self._entry_amount = ttk.Entry(master=self._frame)
        amount_label.grid(row=1, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        self._entry_amount.grid(row=1, sticky=(
            constants.E, constants.W), column=1, padx=5, pady=5)

        content_label = ttk.Label(master=self._frame, text="Content: ")
        self._entry_content = ttk.Entry(master=self._frame)
        content_label.grid(row=2, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        self._entry_content.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

    def _initialize(self):
        label = ttk.Label(master=self._frame,
                          text="Log in a new income:", anchor="center")
        label.grid(row=0, column=0, columnspan=2, sticky=(
            constants.W + constants.E), padx=5, pady=5)

        self._initialize_entryfields()

        submit_button = ttk.Button(
            master=self._frame,
            text="Submit",
            command=self.submit_spending
        )

        submit_button.grid(
            row=3,
            column=0,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5
        )
