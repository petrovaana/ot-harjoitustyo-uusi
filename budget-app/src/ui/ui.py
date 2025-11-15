#täs määritellään et millon mikäki view näkyy
from tkinter import Tk
from login_view import LoginView
from create_user_view import CreateUserView

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

#Muokattava vielä
    def _handle_login(self, username, password):
        print("Login", username, password)
    
    def _handle_create_user(self, username, password):
        print(f"User created {username}", password)

window = Tk()
ui = UI(window)
ui.start()

window.mainloop()