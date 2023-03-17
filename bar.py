import matplotlib
import numpy
import tkinter as Tk

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

root = Tk.Tk()

f = Figure(figsize=(5,4), dpi=100)
ax = f.add_subplot(111)

data = (20, 35, 30, 35, 27)

ind = numpy.arange(5)
width = .5

rects1 = ax.bar(ind, data, width)

canvas = FigureCanvasTkAgg(f, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

Tk.mainloop()