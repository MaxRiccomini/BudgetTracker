import tkinter as tk
import tkinter.font
import time
from tkinter import *
from tkinter import ttk
import numpy as np
import pandas as pd
import matplotlib
from matplotlib import pyplot
import json

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

budgets = ['700.00',
           '300.00',
           '400.00',
           '500.00'
           ]

categories = ['Mortgage/Rent',
              'Car',
              'Food',
              'Entertainment',
              'Entertainment',
              'Food',
              'Food',
              'Food',
              'Car',
              'Mortgage/Rent'
              ]

costs = ['20.74',
         '15.57',
         '40.11',
         '49.97',
         '112.48',
         '45.17',
         '17.76',
         '147.84',
         '420.69',
         '11.68'
         ]

dates = ['3/11/2023',
         '3/13/2023',
         '3/17/2023',
         '3/24/2023',
         '3/24/2023',
         '3/24/2023',
         '3/25/2023',
         '3/27/2023',
         '3/27/2023',
         '3/29/2023'
         ]

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

        # initialization of label using theme-based configs
        self.config(font=sf_pro_font, bg="#E0E0E0")


class CustomFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        # initiliazation of frame using theme-based configs
        self.config(bg="#E0E0E0", highlightbackground="#b0b0b0")


class CustomCheckButton(tk.Checkbutton):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, font=sf_pro_font, **kwargs)

        # initialization of checkbox using theme-based configs
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


expense_list = []
transaction_list = []
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
        expense = "Amount: " + expense_amount + ", Type: " + expense_type
        expense_list.append(expense)
        print(expense_list)
        expense_win.destroy()

    done_button = CustomButton(expense_win, text="Done", command=lambda: save_expense())
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
        transaction = "Amount: " + transaction_amount
        expense_list.append(transaction)
        print(transaction_list)
        transaction_win.destroy()

    done_button = CustomButton(transaction_win, text="Done", command=lambda: save_transaction())
    done_button.place(x=265, y=350)


# Main UI

transaction_list_frame = CustomFrame(root, width=300, height=450)
transaction_list_frame.place(x=5, y=5)

new_transaction_label = CustomLabel(root, text="Transactions")
new_transaction_label.place(x=60, y=10)

total_expenses = CustomFrame(root, width=485, height=450)
total_expenses.place(x=310, y=5)

radar_chart = CustomFrame(root, width=392.5, height=400)
radar_chart.place(x=5, y=460)

stacked_bar_chart = CustomFrame(root, width=392.5, height=400)
stacked_bar_chart.place(x=402.5, y=460)

monthly_entry = PlaceholderEntry(root, placeholder="Enter Monthly: ", color="black", font=sf_pro_font)
monthly_entry.place(x=5, y=875)

new_expense = CustomButton(root, text="New Expense", command=lambda: open_new_expense())
new_expense.place(x=600, y=950)

new_transaction_btn = CustomButton(root, text="New Transaction", command=lambda: open_new_transaction())
new_transaction_btn.place(x=350, y=950)

monthly_button = CustomButton(root, text="Enter")
monthly_button.place(x=377.5, y=877.5)

# BAR CHART BEGINS HERE

f = Figure(figsize=(4, 4), dpi=100)
ax = f.add_subplot(111)

width = .7

rects1 = ax.bar("Mortgage/Rent", float(budgets[0]), width)
rects2 = ax.bar("Car", float(budgets[1]), width)
rects3 = ax.bar("Food", float(budgets[2]), width)
rects4 = ax.bar("Entertainment", float(budgets[3]), width)

canvas = FigureCanvasTkAgg(f, master=root)
canvas.draw()
canvas.get_tk_widget().place(x=402.5, y=460)


# RADAR CHART BEGINS HERE
def _invert(x, limits):
    return limits[1] - (x - limits[0])


def _scale_data(data, ranges):
    for d, (y1, y2) in zip(data[1:], ranges[1:]):
        assert (y1 <= d <= y2) or (y2 <= d <= y1)
    x1, x2 = ranges[0]
    d = data[0]
    if x1 > x2:
        d = _invert(d, (x1, x2))
        x1, x2 = x2, x1
    sdata = [d]
    for d, (y1, y2) in zip(data[1:], ranges[1:]):
        if y1 > y2:
            d = _invert(d, (y1, y2))
            y1, y2 = y2, y1
        sdata.append((d - y1) / (y2 - y1)
                     * (x2 - x1) + x1)
    return sdata


class ComplexRadar():
    def __init__(self, fig, variables, ranges,
                 n_ordinate_levels=6):
        angles = np.arange(0, 360, 360. / len(variables))

        axes = [fig.add_axes([0.1, 0.1, 0.9, 0.9], polar=True,
                             label="axes{}".format(i))
                for i in range(len(variables))]
        l, text = axes[0].set_thetagrids(angles,
                                         labels=variables)
        [txt.set_rotation(angle - 90) for txt, angle
         in zip(text, angles)]
        for ax in axes[1:]:
            ax.patch.set_visible(False)
            ax.grid("off")
            ax.xaxis.set_visible(False)
        for i, ax in enumerate(axes):
            grid = np.linspace(*ranges[i],
                               num=n_ordinate_levels)
            gridlabel = ["{}".format(round(x, 2))
                         for x in grid]
            if ranges[i][0] > ranges[i][1]:
                grid = grid[::-1]
            gridlabel[0] = ""
            ax.set_rgrids(grid, labels=gridlabel,
                          angle=angles[i])
            ax.set_ylim(*ranges[i])
        self.angle = np.deg2rad(np.r_[angles, angles[0]])
        self.ranges = ranges
        self.ax = axes[0]


    def plot(self, data, *args, **kw):
        sdata = _scale_data(data, self.ranges)
        self.ax.plot(self.angle, np.r_[sdata, sdata[0]], *args, **kw)

    def fill(self, data, *args, **kw):
        sdata = _scale_data(data, self.ranges)
        self.ax.fill(self.angle, np.r_[sdata, sdata[0]], *args, **kw)


if __name__ == "__main__":
    variables = ('Mortgage/Rent',
                 'Car',
                 'Food',
                 'Entertainment',)
    data = (190, 140, 100,
            150)
    ranges = [(1, 700), (1, 300), (1, 400),
              (1, 500)]

    fig1 = Figure(figsize=(4, 4))
    radar = ComplexRadar(fig1, variables, ranges)
    radar.plot(data)
    radar.fill(data, alpha=1)

    canvas = FigureCanvasTkAgg(fig1, master=root)
    canvas.draw()
    canvas.get_tk_widget().place(x=5, y=460)

root.mainloop()
