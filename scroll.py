from tkinter import *

root = Tk()

listbox = Listbox(root)

listbox.pack(side=LEFT, fill=BOTH)

scrollbar = Scrollbar(root)

scrollbar.pack(side=RIGHT, fill=BOTH)

for values in range(100):
    listbox.insert(END, values)

listbox.config(yscrollcommand=scrollbar.set)

scrollbar.config(command=listbox.yview)

root.mainloop()