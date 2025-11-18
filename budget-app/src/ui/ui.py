#Coursematerial, geeksforgeeks for tkinter
from ui.login_view import LoginView
from ui.create_user_view import CreateUserView
from ui.logged_in_budget_view import LoggedInView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
    
    def start(self):
        self._show_login_view()

    def _show_login_view(self):
        if self._current_view:
            self._current_view.destroy()
        
        self._current_view = LoginView(
            self._root,
            self._handle_login,
            self._show_create_user_view
        )
        self._current_view.pack()

    def _show_create_user_view(self):
        if self._current_view:
            self._current_view.destroy()
        
        self._current_view = CreateUserView(
            self._root,
            self._handle_create_user,
            self._show_login_view
        )
        self._current_view.pack()

    def _show_logged_in_view(self):
        if self._current_view:
            self._current_view.destroy()
        
        self._current_view = LoggedInView(
            self._root#Tähä vois lisätä myöhemmin ._handle_create_transaction mikä lois uuden kirjauksen budjettiin? Mut for now kunha vaa avais sen 
        )
        self._current_view.pack() 

#Muokattava vielä
    def _handle_login(self, username):
        print(f"Welcome! {username}") #Boxi ei näytä hyvält joku muu? Esim vaa ku on kirjautunu nii siel sivul suoraa
        self._show_logged_in_view()
    
    def _handle_create_user(self, username, password):
        print(f"User created {username}", password) #Joku mikä näyttäis kans boxi kans aika kauhee..
        self._show_login_view() #Vaihtaa näkymää sit itestää 


#Myöhemmin nää index.pyssa nii pyörii ku laittaa taskeihin et pyörittää sitä
#window = Tk()
#ui = UI(window)
#ui.start()
#window.mainloop()