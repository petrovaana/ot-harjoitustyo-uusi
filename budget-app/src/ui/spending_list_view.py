from tkinter import constants, ttk

class SpendingsListView:
    def __init__(self, root, spendings, user, handle_delete_spending):
        self._root = root
        self._spendings = spendings
        self._user = user
        self._handle_delete_spending = handle_delete_spending

        self._frame = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_spending_item(self, spending):
        item_frame = ttk.Frame(master=self._frame)
        label = ttk.Label(master=item_frame,
                          text=f"{spending.content}: {spending.amount}€")

        delete_button = ttk.Button(
            master=item_frame,
            text="Delete",
            command=lambda: self._handle_delete_spending(spending.id)
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
        self._frame = ttk.Frame(master=self._root)

        for spending in self._spendings:
            self._initialize_spending_item(spending)
