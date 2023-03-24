import matplotlib
import numpy
import tkinter as Tk

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

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

root = Tk.Tk()

f = Figure(figsize=(5,4), dpi=100)
ax = f.add_subplot(111)


current = 0
while current < len(categories):

     current += 1

width = .5

rects1 = ax.bar("Mortgage/Rent", budgets[0], width)
rects2 = ax.bar("Car", budgets[1], width)
rects3 = ax.bar("Food", budgets[2], width)
rects4 = ax.bar("Entertainment", budgets[3], width)

canvas = FigureCanvasTkAgg(f, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

ax.invert_xaxis()
ax.invert_yaxis()

Tk.mainloop()