from tkinter import constants, ttk

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
        item_frame = ttk.Frame(master=self._frame)
        label = ttk.Label(master=item_frame,
                          text=f"{income.content}: {income.amount}€")

        delete_button = ttk.Button(
            master=item_frame,
            text="Delete",
            command=lambda: self._handle_delete_income(income.id)
        )

        label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        delete_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.W
        )

        item_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for income in self._incomes:
            self._initialize_income_item(income)
