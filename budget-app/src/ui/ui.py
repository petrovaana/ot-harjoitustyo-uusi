#täs määritellään et millon mikäki view näkyy
from tkinter import Tk
from create_user_view import CreateUserView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
    
    def start(self):
        self._show_login_view()
    
    def create_user_view(self):
        self._current_view = CreateUserView(
            self._root,
            #self.handle_create_user #en oo varma viel miten siis yhistää
        )

    def _show_login_view(self):
        pass

    def budget_view(self):
        pass


window = Tk()
ui = UI(window)
ui.start()

window.mainloop()