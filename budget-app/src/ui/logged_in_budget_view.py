from tkinter import constants, ttk
from services.spendings_service import SpendingsService
from services.user_service import UserService
from services.income_service import IncomesService
from ui.incomes_list_view import IncomesListView
from ui.spending_list_view import SpendingsListView

class LoggedInView:
    def __init__(self, root, show_login_view, show_create_spending_view, show_create_income_view, username):
        self.ss = SpendingsService()
        self.us = UserService()
        self.cs = IncomesService()

        self._root = root
        self._show_login_view = show_login_view
        self._user = username
        self._frame = None
        self._header_frame = None

        self._show_create_spending_view = show_create_spending_view
        self._spending_section_frame = None
        self._spendings_total_frame = None
        self._spending_list_frame = None
        self._spendings_total_label = None

        self._show_create_income_view = show_create_income_view
        self._income_section_frame = None
        self._incomes_total_frame = None
        self._income_list_frame = None
        self._incomes_total_label = None

        self._buttons_frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def logout_handler(self):
        self.destroy()
        self.us.logout()
        self._show_login_view()

    def _initialize_header(self):
        header_frame = self._header_frame

        label = ttk.Label(
            master=header_frame,
            text="Welcome to Budget-App!",
            font=("Segoe UI", 16, "bold")
        )

        label.grid(row=0, column=0, sticky=constants.W, padx=5, pady=5)

        logout_button = ttk.Button(
            master=header_frame,
            text="Logout",
            command=self.logout_handler
        )

        logout_button.grid(
            row=0,
            column=1,
            sticky=constants.E,
            padx=5,
            pady=5
        )

    def _initialize_spending_list(self):
        if self._spending_list_frame:
            self._spending_list_frame.destroy()

        self._spending_list_frame = ttk.Frame(self._spending_section_frame)
        self._spending_list_frame.pack(fill=constants.X)

        spendings = self.ss.get_all_spendings(self._user)

        self._spending_list_view = SpendingsListView(
            self._spending_list_frame,
            spendings,
            self._user,
            self._handle_delete_spending
        )

        self._spending_list_view.pack()

#AI Generated code begins
    def _initialize_spendings_all(self):
        spendings = self.ss.sum_numbers(self._user)

        if not self._spendings_total_label:
            self._spendings_total_label = ttk.Label(
                master=self._spendings_total_frame,
                text=f"Total spendings: {spendings}€"
            )
            self._spendings_total_label.pack(anchor="w", padx=5, pady=5)
        else:
            self._spendings_total_label.config(
                text=f"Total spendings: {spendings}€"
            )
#AI Generated code ends

    def _initialize_income_list(self):
        if self._income_list_frame:
            self._income_list_frame.destroy()

        self._income_list_frame = ttk.Frame(self._income_section_frame)
        self._income_list_frame.pack(fill=constants.X)

        incomes = self.cs.get_all_incomes(self._user)

        self._income_list_view = IncomesListView(
            self._income_list_frame,
            incomes,
            self._user,
            self._handle_delete_income
        )

        self._income_list_view.pack()

#AI Generated code begins
    def _initialize_incomes_all(self):
        incomes = self.cs.sum_numbers(self._user)

        if not self._incomes_total_label:
            self._incomes_total_label = ttk.Label(
                master=self._incomes_total_frame,
                text=f"Total incomes: {incomes}€"
            )
            self._incomes_total_label.pack(anchor="w", padx=5, pady=5)
        else:
            self._incomes_total_label.config(
                text=f"Total incomes: {incomes}€"
            )
#AI Generated code ends

    def _handle_delete_spending(self, spending_id):
        self.ss.delete_spending(spending_id)
        self._initialize_spending_list()
        self._initialize_spendings_all()

    def _handle_delete_income(self, income_id):
        self.cs.delete_income(income_id)
        self._initialize_income_list()
        self._initialize_incomes_all()

    def _initialize_buttons(self):
        new_spending_button = ttk.Button(
            master=self._buttons_frame,
            text="Log new spending",
            command=lambda: self._show_create_spending_view(self._user)
        )

        new_income_button = ttk.Button(
            master=self._buttons_frame,
            text="Log new income",
            command=lambda: self._show_create_income_view(self._user)
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
        self._frame.pack(fill=constants.BOTH, expand=True)

        self._header_frame = ttk.Frame(self._frame)
        self._header_frame.pack(fill=constants.X)
        self._initialize_header()

        self._spending_section_frame = ttk.Frame(self._frame)
        self._spending_section_frame.pack(fill=constants.X, pady=10)

        self._spendings_total_frame = ttk.Frame(self._spending_section_frame)
        self._spendings_total_frame.pack(fill=constants.X)
        self._initialize_spendings_all()

        self._spending_list_frame = ttk.Frame(self._spending_section_frame)
        self._spending_list_frame.pack(fill=constants.X)
        self._initialize_spending_list()

        self._income_section_frame = ttk.Frame(self._frame)
        self._income_section_frame.pack(fill=constants.X, pady=10)

        self._incomes_total_frame = ttk.Frame(self._income_section_frame)
        self._incomes_total_frame.pack(fill=constants.X)
        self._initialize_incomes_all()

        self._income_list_frame = ttk.Frame(self._income_section_frame)
        self._income_list_frame.pack(fill=constants.X)
        self._initialize_income_list()

        self._buttons_frame = ttk.Frame(self._frame)
        self._buttons_frame.pack(fill=constants.X, pady=10)
        self._initialize_buttons()
