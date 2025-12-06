from tkinter import constants, messagebox
from services.user_service import UserService
import tkinter as tk


class CreateUserView:
    def __init__(self, root, show_login_view):
        self._root = root
        self._frame = None

        self._show_login_view = show_login_view

        self._username_entry = None
        self._password1_entry = None
        self._password2_entry = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def create_user_handler(self):
        username = self._username_entry.get()
        password = self._password1_entry.get()
        password2 = self._password2_entry.get()

        if len(username) < 3:
            messagebox.showerror("showerror", "Username too short")
            return

        if len(password) < 8:
            messagebox.showerror("showerror", "Password too short")
            return

        if password != password2:
            messagebox.showerror("showerror", "Passwords dont match")
            return

        us = UserService()
        if us.find_user(username):
            messagebox.showerror("showerror", "Username already exists")
            return

        us.create_user(username, password)
        self._show_login_view()

    def _initialize_register_label(self):
        heading_label = tk.Label(
            master=self._frame,
            text="Register:",
            anchor="center",
            bg="#c8d5b9"
            )

        heading_label.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky=(constants.W + constants.E),
            padx=5,
            pady=5
        )

    def _initialize_username_field(self):
        username_label = tk.Label(
            master=self._frame,
            text="Enter username:",
            bg="#c8d5b9"
            )

        self._username_entry = tk.Entry(
            master=self._frame,
            bg="#e9f5db"
            )

        username_label.grid(
            row=1,
            column=0,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5
            )

        self._username_entry.grid(
            row=1,
            column=1,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5
            )

    def _initialize_password1_field(self):
        password1_label = tk.Label(
            master=self._frame,
            text="Enter password:",
            bg="#c8d5b9"
            )

        self._password1_entry = tk.Entry(
            master=self._frame,
            show='*',
            bg="#e9f5db"
            )

        password1_label.grid(
            row=2,
            column=0,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5
            )

        self._password1_entry.grid(
            row=2,
            column=1,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5
            )

    def _initialize_password2_field(self):
        password2_label = tk.Label(
            master=self._frame,
            text="Re enter password:",
            bg="#c8d5b9"
            )

        self._password2_entry = tk.Entry(
            master=self._frame,
            show='*',
            bg="#e9f5db"
            )

        password2_label.grid(
            row=3,
            column=0,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5
            )

        self._password2_entry.grid(
            row=3,
            column=1,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5
            )

    def _initialize_buttons(self):
        create_user_button = tk.Button(
            master=self._frame,
            text="Create",
            command=self.create_user_handler,
            bg="#718355"
        )

        create_user_button.grid(
            row=4,
            column=1,
            columnspan=1,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5
        )

        back_to_login_button = tk.Button(
            master=self._frame,
            text="Back To Login",
            command=self._show_login_view,
            bg="#718355"
        )

        back_to_login_button.grid(
            row=4,
            column=0,
            columnspan=1,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5
        )

    def _initialize(self):
        self._frame = tk.Frame(master=self._root, bg="#b5c99a")

        self._initialize_register_label()

        self._initialize_username_field()
        self._initialize_password1_field()
        self._initialize_password2_field()

        self._initialize_buttons()
