import tkinter as tk
import tkinter.font
import time
from tkinter import *
import pandas as pd
import matplotlib
import json
from bar import *
from radar import *
from scroll import *

root = tk.Tk()  # create root window

sf_pro_font = tkinter.font.Font(family='SF Pro Text', size=28)

root.title("Budget Tracker")
root.geometry("800x1000")

class CustomButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        # initialization of button using theme-based configs
        self.config(bg="white", fg='black', font=sf_pro_font)

class CustomLabel(tk.Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        #initialization of label using theme-based configs
        self.config(root, font=sf_pro_font)

class CustomFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        #initiliazation of frame using theme-based configs
        self.config(bg="#E0E0E0", highlightbackground="#b0b0b0")

class CustomCheckButton(tk.Checkbutton):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        #initialization of checkbox using theme-based configs
        self.config(activebackground="black")


class PlaceholderEntry(tk.Entry):
    def __init__(self, master=None, placeholder="", color='grey', **kwargs):
        super().__init__(master, **kwargs)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self._on_focus_in)
        self.bind("<FocusOut>", self._on_focus_out)

        self._show_placeholder()

    def _on_focus_in(self, event):
        if self['fg'] == self.placeholder_color:
            self.delete(0, tk.END)
            self.config(fg=self.default_fg_color)

    def _on_focus_out(self, event):
        if not self.get():
            self._show_placeholder()

    def _show_placeholder(self):
        self.delete(0, tk.END)
        self.insert(0, self.placeholder)
        self.config(fg=self.placeholder_color)



transaction_list = CustomFrame(root, width=300, height=450)
transaction_list.config()
transaction_list.place(x=5, y=5)

total_expenses = CustomFrame(root, width=485, height=450)
total_expenses.config()
total_expenses.place(x=310, y=5)

radar_chart= CustomFrame(root, width=392.5, height=400)
radar_chart.place(x=5, y=460)

stacked_bar_chart = CustomFrame(root, width=392.5, height=400)
stacked_bar_chart.place(x=402.5, y=460)

salary_entry = PlaceholderEntry(root, placeholder="Enter Monthly: ", color="black", font=sf_pro_font)
salary_entry.config()
salary_entry.place(x=5, y=875)

new_expense = CustomButton(root, text="New Expense")
new_expense.place(x=600, y=950)

new_transaction = CustomButton(root, text="New Transaction")
new_transaction.place(x=350, y=950)

root.mainloop()
