from tkinter import ttk, constants, StringVar, Tk

class LoginView:
    def __init__(self, root):
        self._root = root
        self._frame = None
    
    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
    #Jsst a heading for the registration
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._root, text="Login with an existing username:", anchor="center")
        label.grid(row=0, column=0, columnspan=2, sticky=(constants.W + constants.E), padx=5, pady=5)

        #Login tietoje kirjaaminen:
        label_username = ttk.Label(master=self._root, text="Username:")
        entry_username = ttk.Entry(master=self._root)
        label_username.grid(row=1, column=0, padx=5, pady=5)
        entry_username.grid(row=1, column=1, padx=5, pady=5)

        label_password = ttk.Label(master=self._root, text="Password:")
        entry_password = ttk.Entry(master=self._root, show='*')
        label_password.grid(row=2, column=0, padx=5, pady=5)
        entry_password.grid(row=2, column=1, padx=5, pady=5)


#Lisäö napeille commandid et mitä tapahtuu
        button_login = ttk.Button(
            master=self._root,
            text="Login"
        )
        button_login.grid(row=3, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        label_registration = ttk.Label(master=self._root, text="No account? Please register: ", anchor="center")
        label_registration.grid(row=5, column=0, columnspan=2, sticky=(constants.W + constants.E), padx=5, pady=5)

        button_register = ttk.Button(
            master=self._root,
            text="Create an account"
        )
        button_register.grid(row=6, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
    

window = Tk()
ui = LoginView(window)
ui._initialize()

window.mainloop()