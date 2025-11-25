"""Responsible for starting the whole Application"""

from tkinter import Tk
from ui.ui import UI


def main():
    """Initializes and starts the application"""
    window = Tk()
    window.title("Budget-App!")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
