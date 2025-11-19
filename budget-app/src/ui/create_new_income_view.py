from tkinter import ttk, constants

class CreateIncomeView:
    def __init__(self, root):
        self._root = root
        self._frame = ttk.Frame(master=self._root)

        self._initialize()
    
    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        pass