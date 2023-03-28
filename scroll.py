import tkinter as tk
from tkinter import *

root = tk.Tk()

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

budgets = ['700.00',
           '300.00',
           '400.00',
           '500.00'
           ]

#root.title("Budget List")
#root.geometry("400x100")


def scrolllistbox(event):
    lst3.yview_scroll(int(-4 * (event.delta / 120)), "units")
    lst2.yview_scroll(int(-4 * (event.delta / 120)), "units")
    lst1.yview_scroll(int(-4 * (event.delta / 120)), "units")


scrollbar = Scrollbar(root)
# scrollbar.pack(side=RIGHT, fill=Y)


def def_listbox1():
    listbox = Listbox(None)
    listbox.insert(END, *categories)
    # listbox.pack(expand=1, fill="both", side="left")
    return listbox


def def_listbox2():
    listbox = Listbox(None)
    listbox.insert(END, *costs)
    # listbox.pack(expand=1, fill="both", side="left")
    return listbox


def def_listbox3():
    listbox = Listbox(None)
    listbox.insert(END, *dates)
    # listbox.pack(expand=1, fill="both", side="left")
    return listbox


frame1 = tk.Frame(root)
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
