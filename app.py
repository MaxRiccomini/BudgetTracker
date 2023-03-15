import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Budget Tracker")
root.geometry("1000x600")

class CustomButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        # initialization of button using color theme-based configs
        self.config(bg="#003366", fg='#003366', font=("Arial", 14)

class CustomEntry(tk.Entry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        # initialization of entry using color theme-based configs
        self.config(bg="white")


class CustomLabel(tk.Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        # initialization of entry using color theme-based configs
        self.config(bg="#E0E0E0", fg='black', font=("Arial", 14))



root.mainloop()
