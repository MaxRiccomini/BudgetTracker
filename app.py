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
import datetime

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

budgets = ['700.00',
           '300.00',
           '400.00',
           '500.00'
           ]

# create root window and set window icon
root = tk.Tk()
root.iconbitmap("app_resources/icon.ico")

sf_pro_font = tkinter.font.Font(family='app_resources/SF Pro Text', size=28)
sf_pro_font_mini = tkinter.font.Font(family='app_resources/SF Pro Text', size=14)

current_date = datetime.date.today()
formatted_date = datetime.date.today().strftime("%m%d%y")

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
expense_type_list = []
expense_date_list = []

transaction_list = []
transaction_type_list = []
transaction_date_list = []
options = ["Mortgage/Rent", "Car", "Food", "Entertainment"]

selected_option = tk.StringVar(value=options[0])


def def_listbox1():
    listbox = Listbox(None)
    listbox.insert(END, *transaction_type_list)
    listbox.place(x=5, y=60)
    return listbox


def def_listbox2():
    listbox = Listbox(None)
    listbox.insert(END, *transaction_list)
    listbox.place(x=100, y=60)
    return listbox


def def_listbox3():
    listbox = Listbox(None)
    listbox.insert(END, *transaction_date_list)
    listbox.place(x=195, y=60)
    return listbox


def def_listbox4():
    listbox = Listbox(None)
    listbox.insert(END, *expense_type_list)
    listbox.place(x=450, y=60)
    return listbox


def def_listbox5():
    listbox = Listbox(None)
    listbox.insert(END, *expense_list)
    listbox.place(x=535, y=60)
    return listbox


def def_listbox6():
    listbox = Listbox(None)
    listbox.insert(END, *expense_date_list)
    listbox.place(x=630, y=60)
    return listbox


lst1 = def_listbox1()
lst2 = def_listbox2()
lst3 = def_listbox3()
lst4 = def_listbox4()
lst5 = def_listbox5()
lst6 = def_listbox6()

mortgageTotal = 0
carTotal = 0
foodTotal = 0
entertainTotal = 0


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
        global mortgageTotal, carTotal, foodTotal, entertainTotal
        expense_amount = new_expense_amount.get()
        expense_type = custom_dropDown.get()
        expense_list.append(expense_amount)
        expense_date_list.append(current_date)
        expense_type_list.append(expense_type)
        if custom_dropDown.get() == "Mortgage/Rent":
            mortgageTotal += float(expense_amount)
        elif custom_dropDown.get() == "Car":
            carTotal += float(expense_amount)
        elif custom_dropDown.get() == "Food":
            foodTotal += float(expense_amount)
        else:
            entertainTotal += int(expense_amount)

        # update things
        def_listbox4()
        def_listbox5()
        def_listbox6()

        data = (float(mortgageTotal), float(carTotal), float(foodTotal),
                float(entertainTotal))
        radar.plot(data)
        radar.fill(data, alpha=1)
        canvas = FigureCanvasTkAgg(fig1, master=root)
        canvas.draw()
        canvas.get_tk_widget().place(x=5, y=460)

        f = Figure(figsize=(4, 4), dpi=100)
        ax = f.add_subplot(111)

        width = .1

        rects1 = ax.bar("Mortgage/Rent", float(mortgageTotal), width)
        rects2 = ax.bar('    ', float(budgets[0]), width)
        rects3 = ax.bar("Car", float(carTotal), width)
        rects4 = ax.bar('   ', float(budgets[1]), width)
        rects5 = ax.bar("Food", float(foodTotal), width)
        rects6 = ax.bar('  ', float(budgets[2]), width)
        rects7 = ax.bar("Entertainment", float(entertainTotal), width)
        rects8 = ax.bar(' ', float(budgets[3]), width)

        canvas = FigureCanvasTkAgg(f, master=root)
        canvas.draw()
        canvas.get_tk_widget().place(x=402.5, y=460)

        totalLabel = CustomLabel(root, text="Totals")
        totalLabel.place(x=345, y=250)

        mortgageTotalLabel = CustomLabel(root, text="Mortgage")
        mortgageTotalLabel.place(x=45, y=320)
        mortgageTotalLabelData = CustomLabel(root, text=mortgageTotal)
        mortgageTotalLabelData.place(x=45, y=370)

        carTotalLabel = CustomLabel(root, text="Car")
        carTotalLabel.place(x=230, y=320)
        carTotalLabelData = CustomLabel(root, text=carTotal)
        carTotalLabelData.place(x=230, y=370)

        foodTotalLabel = CustomLabel(root, text="Food")
        foodTotalLabel.place(x=330, y=320)
        foodTotalLabelData = CustomLabel(root, text=foodTotal)
        foodTotalLabelData.place(x=330, y=370)

        entertainTotalLabel = CustomLabel(root, text="Entertainment")
        entertainTotalLabel.place(x=470, y=320)
        entertainTotalLabelData = CustomLabel(root, text=entertainTotal)
        entertainTotalLabelData.place(x=470, y=370)

        not_configured_graphs.destroy()
        not_configured_e_list.destroy()

        expense_win.destroy()

    done_button = CustomButton(expense_win, text="Done", command=lambda: save_expense())
    done_button.place(x=265, y=350)

    custom_dropDown = ttk.Combobox(expense_win, value=options, font=sf_pro_font_mini)
    custom_dropDown.place(x=5, y=175)


transaction_options = ["Checking", "Savings"]
selected_transaction_option = tk.StringVar(value=transaction_options[0])


def open_new_transaction():
    transaction_win = Toplevel(root)
    transaction_win.config(bg="#E0E0E0")
    transaction_win.geometry("600x400")
    transaction_win.title("New Transaction")
    CustomLabel(transaction_win, text="New Transaction").place(x=185, y=10)
    new_transaction = PlaceholderEntry(transaction_win, placeholder="Amount Here:", color="black", font=sf_pro_font)
    new_transaction.place(x=5, y=75)

    def new_transaction_category():
        new_category_win = Toplevel(transaction_win)
        new_category_win.config(bg="#E0E0E0")
        new_category_win.geometry("400x200")
        new_category_win.title("New Category")
        new_category_entry = tk.Entry(new_category_win, font=sf_pro_font)
        new_category_entry.place(x=10, y=5)
        options.append(new_category_entry.get())
        custom_dropDown.options = transaction_options
        new_category_button = CustomButton(new_category_win, text="Done")

    def populate_category_dropdown(df=None):
        transaction_options = custom_dropDown.options
        for option in df['Category'].unique():
            if option not in transaction_options:
                transaction_options.append(option)

    new_transaction_cat = CustomButton(transaction_win, text="New Account", font=sf_pro_font_mini,
                                       command=lambda: new_transaction_category())
    new_transaction_cat.place(x=5, y=215)

    custom_dropDown = ttk.Combobox(transaction_win, value=transaction_options, font=sf_pro_font_mini, state="readonly")
    custom_dropDown.place(x=5, y=175)

    def save_transaction():
        transaction_amount = new_transaction.get()
        transaction_type = custom_dropDown.get()
        transaction_list.append(transaction_amount)
        transaction_date_list.append(current_date)
        transaction_type_list.append(transaction_type)
        print(transaction_list)
        def_listbox1()
        def_listbox2()
        def_listbox3()
        not_configured_t_list.destroy()
        transaction_win.destroy()

    done_button = CustomButton(transaction_win, text="Done", command=lambda: save_transaction())
    done_button.place(x=265, y=350)


monthly_entry = tk.Entry(root, font=sf_pro_font)
monthly_entry.place(x=5, y=875)

# Main UI

transaction_list_frame = CustomFrame(root, width=350, height=450)
transaction_list_frame.place(x=0, y=5)

new_transaction_label = CustomLabel(root, text="Transactions")
new_transaction_label.place(x=60, y=10)

total_expenses = CustomFrame(root, width=450, height=450)
total_expenses.place(x=310, y=5)

new_expenses_label = CustomLabel(total_expenses, text="Expenses")
new_expenses_label.place(x=200, y=10)

radar_chart = CustomFrame(root, width=392.5, height=400)
radar_chart.place(x=5, y=460)

stacked_bar_chart = CustomFrame(root, width=392.5, height=400)
stacked_bar_chart.place(x=402.5, y=460)

not_configured_graphs = CustomLabel(root, text="Not Configured  -  Add an Expense")
not_configured_graphs.place(x=100, y=700)

not_configured_e_list = CustomLabel(root, text="Add Expense")
not_configured_e_list.place(x=480, y=150)

not_configured_t_list = CustomLabel(root, text="Add Transaction")
not_configured_t_list.place(x=50, y=150)


new_expense = CustomButton(root, text="New Expense", command=lambda: open_new_expense())
new_expense.place(x=600, y=950)

new_transaction_btn = CustomButton(root, text="New Transaction", command=lambda: open_new_transaction())
new_transaction_btn.place(x=350, y=950)

monthly_button = CustomButton(root, text="Enter Monthly")
monthly_button.place(x=377.5, y=877.5)


# RADAR CHART BEGINS HERE
def _invert(x, limits):
    return limits[1] - (x - limits[0])


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

    def plot(self, udata, *args, **kw):
        self.ax.plot(self.angle, np.r_[udata, udata[0]], *args, **kw)

    def fill(self, udata, *args, **kw):
        self.ax.fill(self.angle, np.r_[udata, udata[0]], *args, **kw)


if __name__ == "__main__":
    variables = ('Mortgage/Rent',
                 'Car',
                 'Food',
                 'Entertainment',)
    data = (int(mortgageTotal), int(carTotal), int(foodTotal),
            int(entertainTotal))
    ranges = [(1, 700), (1, 500), (1, 300),
              (1, 400)]

    fig1 = Figure(figsize=(4, 4))
    radar = ComplexRadar(fig1, variables, ranges)


def scrolllistbox(event):
    lst3.yview_scroll(int(-4 * (event.delta / 120)), "units")
    lst2.yview_scroll(int(-4 * (event.delta / 120)), "units")
    lst1.yview_scroll(int(-4 * (event.delta / 120)), "units")
    lst4.yview_scroll(int(-4 * (event.delta / 120)), "units")
    lst5.yview_scroll(int(-4 * (event.delta / 120)), "units")
    lst6.yview_scroll(int(-4 * (event.delta / 120)), "units")


scrollbar = Scrollbar(root)

frame1 = tk.Frame(root)
lst1.config(yscrollcommand=scrollbar.set)
lst1.bind("<MouseWheel>", scrolllistbox)
lst2.config(yscrollcommand=scrollbar.set)
lst2.bind("<MouseWheel>", scrolllistbox)
lst3.config(yscrollcommand=scrollbar.set)
lst3.bind("<MouseWheel>", scrolllistbox)

lst4.config(yscrollcommand=scrollbar.set)
lst4.bind("<MouseWheel>", scrolllistbox)
lst5.config(yscrollcommand=scrollbar.set)
lst5.bind("<MouseWheel>", scrolllistbox)
lst6.config(yscrollcommand=scrollbar.set)
lst6.bind("<MouseWheel>", scrolllistbox)

root.mainloop()