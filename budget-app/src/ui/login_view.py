#Used course material (TkInter guide) and Geeks for geeks
from tkinter import ttk, constants, messagebox
from services.user_service import UserService

#muuta framen alustus vasti initializes?
class LoginView:
    def __init__(self, root, handle_login, handle_show_create_user_view):
        self._root = root
        self._frame = ttk.Frame(master=self._root)
        self._handle_login = handle_login
        self._handle_show_create_user_view = handle_show_create_user_view
        self._entry_password = None
        self._entry_username = None

        self._initialize()
    
    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()
    
#Jakaa myös fiksummin --> luettavampaa koodia +frame täs
    def _initialize(self):
        label = ttk.Label(master=self._frame, text="Login with an existing username:", anchor="center")#Asked AI for how to make the text in the middle
        label.grid(row=0, column=0, columnspan=2, sticky=(constants.W + constants.E), padx=5, pady=5) 

        label_username = ttk.Label(master=self._frame, text="Username:")
        self._entry_username = ttk.Entry(master=self._frame)
        label_username.grid(row=1, column=0, padx=5, pady=5)
        self._entry_username.grid(row=1, column=1, padx=5, pady=5)

        label_password = ttk.Label(master=self._frame, text="Password:")
        self._entry_password = ttk.Entry(master=self._frame, show='*')
        label_password.grid(row=2, column=0, padx=5, pady=5)
        self._entry_password.grid(row=2, column=1, padx=5, pady=5)

        button_login = ttk.Button(
            master=self._frame,
            text="Login",
            command=self._login_handler
        )
        button_login.grid(row=3, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        label_registration = ttk.Label(master=self._frame, text="No account? Please register: ", anchor="center")
        label_registration.grid(row=5, column=0, columnspan=2, sticky=(constants.W + constants.E), padx=5, pady=5)

        button_register = ttk.Button(
            master=self._frame,
            text="Create an account",
            command=self._handle_show_create_user_view
        )
        button_register.grid(row=6, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)


    def _login_handler(self):
        username = self._entry_username.get()
        password = self._entry_password.get()
        
        us = UserService()
        if us.login(username, password):
            self._handle_login(username)
        
        else:
            messagebox.showerror("Showerror", "The username or the password was incorrect") #Geeksforgeeks