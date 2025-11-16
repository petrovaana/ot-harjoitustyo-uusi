import tkinter as tk
from tkinter import Tk, constants, ttk

class LoggedInView:
    def __init__(self, root):
        self._root = root
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = tk.Label(master=self._frame, text="Welcome to Budget-App!", font=("Segoe UI", 16, "bold"))
        label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)

#Menojen laatikko
        box_spendings = tk.Frame(self._frame, bg="white", bd=2, relief="solid", width=100, height=70)
        box_spendings.grid(row=1, column=0, padx=10, pady=10)

        box_spendings_text = tk.Label(box_spendings, text="The box where all the users spendings will be", bg="white")
        box_spendings_text.pack(padx=10, pady=10)

#Tulojen laatikko
        box_incomes = tk.Frame(self._frame, bg="white", bd=2, relief="solid", width=100, height=70)
        box_incomes.grid(row=1, column=4, padx=10, pady=10)

        box_incomes_text = tk.Label(box_incomes, text="The box where all the users incomes will be", bg="white")
        box_incomes_text.pack(padx=10, pady=10)

#Kuukausittaisten menojen laatikko:
        box_monthly_spendings = tk.Frame(self._frame, bg="white", bd=2, relief="solid", width=100, height=70)
        box_monthly_spendings.grid(row=2, column=0, padx=10, pady=10)

        box_monthly_spendings_text = tk.Label(box_monthly_spendings, text="The box where all the users monthly spendings will be", bg="white")
        box_monthly_spendings_text.pack(padx=10, pady=10)

    
window = tk.Tk()
window.title("Logged in Tests")
view = LoggedInView(window)
view.pack()
window.mainloop()
    
    #nappi mis voi lisätä menoja
    #yleisesti määrittäminen esim näytön koko
    #Miten kaikki näkyy siinä? (menojen määrä täs kuussa, 
    #tulojen määrä täs kuus, en tiiä jotai kategorioit? esim pakolliset?)