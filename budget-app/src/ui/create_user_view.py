#Coursematerial, geeksforgeeks for tkinter
from tkinter import ttk, constants, messagebox
from services.user_service import UserService

class CreateUserView:
    def __init__(self, root, handle_create_user, handle_show_login_view):
        self._root = root
        self._frame = ttk.Frame(master=self._root)
        self._handle_create_user = handle_create_user
        self._handle_show_login_view = handle_show_login_view

        self._username_entry = None
        self._password1_entry = None
        self._password2_entry = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()

#Vois jakaa selkeempiin osiin et näkyy mitä tapahtuu --> luettavampaa koodia + frame alustaa vast täs? Tarkista guidesta
    def _initialize(self):

        heading_label = ttk.Label(master=self._frame, text="Register:", anchor="center")
        heading_label.grid(row=0, column=0, columnspan=2, sticky=(constants.W + constants.E), padx=5, pady=5)

        username_label = ttk.Label(master=self._frame, text="Enter username:")
        self._username_entry = ttk.Entry(master=self._frame)
        username_label.grid(row=1, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)
        self._username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        password1_label = ttk.Label(master=self._frame, text="Enter password:")
        self._password1_entry = ttk.Entry(master=self._frame, show='*')
        password1_label.grid(row=2, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)
        self._password1_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        password2_label = ttk.Label(master=self._frame, text="Re enter password:")
        self._password2_entry = ttk.Entry(master=self._frame, show='*')
        password2_label.grid(row=3, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)
        self._password2_entry.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        create_user_button = ttk.Button(master=self._frame, text="Create an Account", command=self._create_user_handler)
        create_user_button.grid(row=4, column=1, columnspan=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        back_to_login_button = ttk.Button(master=self._frame, text="Back To Login", command=self._handle_show_login_view)
        back_to_login_button.grid(row=4, column=0, columnspan=1, sticky=(constants.E, constants.W), padx=5, pady=5)


    def _create_user_handler(self):
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
            messagebox.showerror("showerror","Passwords dont match")
            return 

        us = UserService()
        if not us.create_user(username, password):
            messagebox.showerror("showerror","Username already exists")
        else:
            self._handle_create_user(username, password)