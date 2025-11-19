#Coursematerial, geeksforgeeks for tkinter
import tkinter as tk
from tkinter import constants, ttk

class LoggedInView:
    def __init__(self, root, handle_show_new_spending_view, handle_show_new_income_view, username):
        self._root = root
        self._handle_show_new_spending_view = handle_show_new_spending_view
        self._handle_show_new_income_view = handle_show_new_income_view
        self._frame = ttk.Frame(master=self._root)
        self._username = username

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()

#sama homma jakaa eri funktioihin ja initializes vast määritellä frame?
    def _initialize(self):
        label = tk.Label(master=self._frame, text="Welcome to Budget-App!", font=("Segoe UI", 16, "bold"))
        label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)

#Menojen laatikko
        box_spendings = tk.Frame(self._frame, bg="white", bd=2, relief="solid", width=100, height=70)#muokkaa koot koska en tiiä minkä kokosii ois hyvät
        box_spendings.grid(row=1, column=0, padx=10, pady=10)

        box_spendings_text = tk.Label(box_spendings, text="The box where all the users spendings will be", bg="white")
        box_spendings_text.pack(padx=10, pady=10)

#Tulojen laatikko
        box_incomes = tk.Frame(self._frame, bg="white", bd=2, relief="solid", width=100, height=70)
        box_incomes.grid(row=1, column=4, padx=10, pady=10)

        box_incomes_text = tk.Label(box_incomes, text="The box where all the users incomes will be", bg="white")
        box_incomes_text.pack(padx=10, pady=10)

#Nappi millä luoda uus transaction
        new_spending_button = ttk.Button(master=self._frame, text="Log in new spending", command=self._handle_show_new_spending_view)
        new_spending_button.grid(row=4, column=0, columnspan=2,  padx=5, pady=5)

#Lisätty näkyviin, mutta toiminta ei viel oo kunnossa (seuraavaan sprinttiin vast)
        new_income_button = ttk.Button(master=self._frame, text="Log in new income", command=self._handle_show_new_income_view)
        new_income_button.grid(row=4, column=3, columnspan=2,  padx=5, pady=5)
