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
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._root, text="Login with an existing username:")
        label.grid(row=0, column=0, columnspan=2)

        #Login tietoje kirjaaminen:
        label_username = ttk.Label(master=self._root, text="Username:")
        entry_username = ttk.Entry(master=self._root)
        label_username.grid(row=1, column=0)
        entry_username.grid(row=1, column=1)

        label_password = ttk.Label(master=self._root, text="Password:")
        entry_password = ttk.Entry(master=self._root)
        label_password.grid(row=2, column=0)
        entry_password.grid(row=2, column=1)


#Lisäö napeille commandid et mitä tapahtuu
        button_login = ttk.Button(
            master=self._root,
            text="Login"
        )
        button_login.grid(row=3, column=1)

        label_registration = ttk.Label(master=self._root, text="Or register: ")
        label_registration.grid(row=4, column=0)

        button_register = ttk.Button(
            master=self._root,
            text="Register"
        )
        button_register.grid(row=4, column=1)
    

window = Tk()
ui = LoginView(window)
ui._initialize()

window.mainloop()