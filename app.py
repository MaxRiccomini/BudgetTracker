import tkinter as tk
import tkinter.font
import time
import datetime
from tkinter import *
from tkinter import ttk

import pandas as pd
import matplotlib
import json


root = tk.Tk()  # create root window

sf_pro_font = tkinter.font.Font(family='SF Pro Text', size=28)
current_date = datetime.date.today()
current_date.strftime("%m%d%y")
print(current_date)

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
        self.config(font=sf_pro_font, bg="#E0E0E0")

class CustomFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        #initiliazation of frame using theme-based configs
        self.config(bg="#E0E0E0", highlightbackground="#b0b0b0")

class CustomCheckButton(tk.Checkbutton):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, font=sf_pro_font, **kwargs)

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

date_list = []
expense_list = []
expense_type_list = []
transaction_list = []
transaction_type_list = []
options = ["Mortgage/Rent", "Car", "Food", "Entertainment"]
transaction_options = ["Checking", "Savings"]
selected_option = tk.StringVar(value=options[0])


# opens pop up for new transaction
def open_new_expense():
    expense_win = Toplevel(root)
    expense_win.config(bg="#E0E0E0")
    expense_win.geometry("600x400")
    expense_win.title("New Expense")
    CustomLabel(expense_win, text="New Expense").place(x=185, y=10)
    new_expense_amount = PlaceholderEntry(expense_win, placeholder="Amount Here:", color="black", font=sf_pro_font)
    new_expense_amount.place(x=5, y=75)


    def save_expense():
        expense_amount = new_expense_amount.get()
        expense_type = selected_option.get()
        expense = expense_amount
        expense_type_list.append(expense_type)
        expense_list.append(expense)
        date_list.append(current_date)
        expense_win.destroy()

    done_button = CustomButton(expense_win, text="Done", command= lambda: save_expense())
    done_button.place(x=265, y=350)

    custom_dropDown = ttk.Combobox(expense_win, value=options, font=sf_pro_font)
    custom_dropDown.place(x=5, y=175)


def open_new_transaction():
    transaction_win = Toplevel(root)
    transaction_win.config(bg="#E0E0E0")
    transaction_win.geometry("600x400")
    transaction_win.title("New Expense")
    CustomLabel(transaction_win, text="New Expense").place(x=185, y=10)
    new_transaction = PlaceholderEntry(transaction_win, placeholder="Amount Here:", color="black", font=sf_pro_font)
    new_transaction.place(x=5, y=75)

    def save_transaction():
        transaction_amount = new_transaction.get()
        transaction = transaction_amount
        transaction_list.append(transaction)

        print(transaction_list)
        transaction_win.destroy()

    done_button = CustomButton(transaction_win, text="Done", command=lambda: save_transaction())
    done_button.place(x=265, y=350)



# Main UI

transaction_list_frame = CustomFrame(root, width=300, height=450)
transaction_list_frame.place(x=5, y=5)

#new_transaction_label = CustomLabel(root, text="Transactions")
#new_transaction_label.place(x=60, y=10)

total_expenses = CustomFrame(root, width=485, height=450)
total_expenses.place(x=310, y=5)

radar_chart= CustomFrame(root, width=392.5, height=400)
radar_chart.place(x=5, y=460)

stacked_bar_chart = CustomFrame(root, width=392.5, height=400)
stacked_bar_chart.place(x=402.5, y=460)

monthly_entry = PlaceholderEntry(root, placeholder="Enter Monthly: ", color="black", font=sf_pro_font)
monthly_entry.place(x=5, y=875)

new_expense = CustomButton(root, text="New Expense", command= lambda: open_new_expense())
new_expense.place(x=600, y=950)

new_transaction_btn = CustomButton(root, text="New Transaction", command= lambda: open_new_transaction())
new_transaction_btn.place(x=350, y=950)

monthly_button = CustomButton(root, text="Enter")
monthly_button.place(x=377.5, y=877.5)


def scrolllistbox(event):
    lst3.yview_scroll(int(-4 * (event.delta / 120)), "units")
    lst2.yview_scroll(int(-4 * (event.delta / 120)), "units")
    lst1.yview_scroll(int(-4 * (event.delta / 120)), "units")


scrollbar = Scrollbar(root)
# scrollbar.pack(side=RIGHT, fill=Y)


def def_listbox1():
    listbox = Listbox(transaction_list_frame)
    listbox.insert(END, *expense_type_list)
    listbox.grid(row=0, column=0)
    listbox.config(width=11, height=26, font=sf_pro_font)
    return listbox


def def_listbox2():
    listbox = Listbox(transaction_list_frame)
    listbox.insert(END, *expense_list)
    listbox.grid(row=0, column=1)
    listbox.config(width=11, height=26, font=sf_pro_font)
    return listbox


def def_listbox3():
    listbox = Listbox(transaction_list_frame)
    listbox.insert(END, *date_list)
    listbox.grid(row=0, column=2)
    listbox.config(width=11, height=26, font=sf_pro_font)
    return listbox


# frame1.pack(expand=0, fill="both")

lst1 = def_listbox1()
lst2 = def_listbox2()
lst3 = def_listbox3()

lst1.config(yscrollcommand=scrollbar.set)
lst1.bind("<MouseWheel>", scrolllistbox)
lst2.config(yscrollcommand=scrollbar.set)
lst2.bind("<MouseWheel>", scrolllistbox)
lst3.config(yscrollcommand=scrollbar.set)
lst3.bind("<MouseWheel>", scrolllistbox)

root.mainloop()
