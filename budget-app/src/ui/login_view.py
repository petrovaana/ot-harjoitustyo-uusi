from tkinter import ttk, constants, messagebox
from services.user_service import UserService


class LoginView:
    def __init__(self, root, show_create_user_view, show_logged_in_view):
        self._root = root
        self._frame = None
        self._show_create_user_view = show_create_user_view
        self._show_logged_in_view = show_logged_in_view
        self._entry_password = None
        self._entry_username = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _login_handler(self):
        username = self._entry_username.get()
        password = self._entry_password.get()

        us = UserService()
        if us.login(username, password):
            self._show_logged_in_view(username)
        else:
            messagebox.showerror(
                "Showerror", "The username or the password was incorrect")
            return

    def _initialize_username_field(self):
        label_username = ttk.Label(master=self._frame, text="Username:")
        self._entry_username = ttk.Entry(master=self._frame)
        label_username.grid(row=1, column=0, padx=5, pady=5)
        self._entry_username.grid(row=1, column=1, padx=5, pady=5)

    def _initialize_password_field(self):
        label_password = ttk.Label(master=self._frame, text="Password:")
        self._entry_password = ttk.Entry(master=self._frame, show='*')
        label_password.grid(row=2, column=0, padx=5, pady=5)
        self._entry_password.grid(row=2, column=1, padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        # Asked AI for how to make the text in the middle
        label = ttk.Label(
            master=self._frame, text="Login with an existing username:", anchor="center")
        label.grid(row=0, column=0, columnspan=2, sticky=(
            constants.W + constants.E), padx=5, pady=5)

        self._initialize_username_field()
        self._initialize_password_field()

        button_login = ttk.Button(
            master=self._frame,
            text="Login",
            command=self._login_handler
        )

        button_login.grid(
            row=3,
            column=0,
            columnspan=2,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5
        )

        label_registration = ttk.Label(
            master=self._frame, text="No account? Please register: ", anchor="center")
        label_registration.grid(row=5, column=0, columnspan=2, sticky=(
            constants.W + constants.E), padx=5, pady=5)

        button_register = ttk.Button(
            master=self._frame,
            text="Create an account",
            command=self._show_create_user_view
        )

        button_register.grid(
            row=6,
            column=0,
            columnspan=2,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5
        )
