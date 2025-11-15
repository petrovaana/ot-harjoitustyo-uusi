from tkinter import ttk, constants, StringVar, Tk #, Tk jos kokeilen toimintaa viel

#Vaiha myöhemmin yoi handle_create_user niin et toimii oikein
class CreateUserView:
    def __init__(self, root, handle_create_user=None):
        self._root = root
        self._frame = ttk.Frame(master=self._root)
        self._handle_create_user = handle_create_user
        self._error_var = StringVar()
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
    #Jsst a heading for the registration
        heading_label = ttk.Label(master=self._frame, text="Register:", anchor="center")
        heading_label.grid(row=0, column=0, columnspan=2, sticky=(constants.W + constants.E), padx=5, pady=5)

    #Getting username from user
        username_label = ttk.Label(master=self._frame, text="Enter username:")
        self._username_entry = ttk.Entry(master=self._frame)
        username_label.grid(row=1, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)
        self._username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
    
    #Getting the password from user
        password1_label = ttk.Label(master=self._frame, text="Enter password:")
        self._password1_entry = ttk.Entry(master=self._frame, show='*')
        password1_label.grid(row=2, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)
        self._password1_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

    #Re entering password to be sure and checkups
        password2_label = ttk.Label(master=self._frame, text="Re enter password:")
        self._password2_entry = ttk.Entry(master=self._frame, show='*')
        password2_label.grid(row=3, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)
        self._password2_entry.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

    #A button for creating an account (not working yet)
        create_user_button = ttk.Button(master=self._frame, text="Create an Account", command=self._create_user)
        create_user_button.grid(row=4, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

    
    #Vielä virheellinen ei toimi niiku pitää
    def _create_user(self):
        username = self._username_entry.get()
        password = self._password1_entry.get()
        password2 = self._password2_entry.get()

        if len(username) < 3 or len(password) < 3:
            self._error_var.set("Username and password must be at least 3 characters")
            return
        elif password != password2:
            self._error_var.set("Username and password must be at least 3 characters")
            return

#Tää osa pitää muokkaa ja korjaa ongelma..
        self._error_var.set("")
        if self._handle_create_user:
            self._handle_create_user(username, password)


#Iha vaa testaamista varten luotu for now:)
window = Tk()
window.title("Register")
view = CreateUserView(window)
view.pack()
window.mainloop()