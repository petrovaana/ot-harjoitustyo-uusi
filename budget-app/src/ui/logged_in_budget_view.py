from tkinter import Tk, constants, ttk

class LoggedInView:
    def __init__(self, root):
        self._root = root
        self._frame = None

    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._root, text="Welcome to Budget-App!")
        label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)
    
    #nappi mis voi lisätä menoja
    #yleisesti määrittäminen esim näytön koko
    #Miten kaikki näkyy siinä? (menojen määrä täs kuussa, 
    #tulojen määrä täs kuus, en tiiä jotai kategorioit? esim pakolliset?)