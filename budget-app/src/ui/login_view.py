from tkinter import constants, messagebox
from services.user_service import UserService
import tkinter as tk

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

    def login_handler(self):
        username = self._entry_username.get()
        password = self._entry_password.get()

        us = UserService()
        if us.login(username, password):
            self._show_logged_in_view(username)
        else:
            messagebox.showerror(
                "Showerror", "The username or the password was incorrect")
            return

    def _initialize_login_label(self):
        # Asked AI for how to make the text in the middle
        label = tk.Label(
            master=self._frame,
            text="Login with an existing username:",
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

    def _initialize_username_field(self):
        label_username = tk.Label(
            master=self._frame,
            text="Username:",
            bg="#c8d5b9"
            )

        self._entry_username = tk.Entry(
            master=self._frame,
            bg="#e9f5db"
            )

        label_username.grid(
            row=1,
            column=0,
            padx=5,
            pady=5
            )

        self._entry_username.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
            )

    def _initialize_password_field(self):
        label_password = tk.Label(
            master=self._frame,
            text="Password:",
            bg="#c8d5b9"
            )

        self._entry_password = tk.Entry(
            master=self._frame,
            show='*',
            bg="#e9f5db"
            )

        label_password.grid(
            row=2,
            column=0,
            padx=5,
            pady=5
            )

        self._entry_password.grid(
            row=2,
            column=1,
            padx=5,
            pady=5
            )

    def _initialize_buttons(self):
        button_login = tk.Button(
            master=self._frame,
            text="Login",
            command=self.login_handler,
            bg="#718355"
        )

        button_login.grid(
            row=3,
            column=0,
            columnspan=2,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5
        )

        button_register = tk.Button(
            master=self._frame,
            text="Create an account",
            command=self._show_create_user_view,
            bg="#718355"
        )

        button_register.grid(
            row=6,
            column=0,
            columnspan=2,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5
        )

    def _initialize_register_label(self):
        label_registration = tk.Label(
            master=self._frame,
            text="No account? Please register: ",
            anchor="center",
            bg="#c8d5b9"
            )

        label_registration.grid(
            row=5,
            column=0,
            columnspan=2,
            sticky=(constants.W + constants.E),
            padx=5,
            pady=5
            )

    def _initialize(self):
        self._frame = tk.Frame(master=self._root, bg="#b5c99a")

        self._initialize_login_label()

        self._initialize_username_field()
        self._initialize_password_field()

        self._initialize_buttons()

        self._initialize_register_label()
