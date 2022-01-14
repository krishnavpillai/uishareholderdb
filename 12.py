from tkinter import *

root = Tk()

options = ["10", "20", "30"]

var = StringVar(root)
var.set('10')

Value = Label(root, text="Value:", font="-weight bold")
Value.grid(row=0, column=0, sticky="W")

Search = Entry(root, width=50)
Search.grid(row=0, column=1)

Top = Label(root, text="TOP", font="-weight bold")
Top.grid(row=0, column=2, sticky="W")

Dropdownlist = OptionMenu(root, var, *options)
Dropdownlist.grid(row=0, column=3, padx=5, sticky="W")

Go = Button(root, text="GO", width=5)
Go.grid(row=0, column=4, sticky="W")

Reset = Button(root, text="RESET", width=5)
Reset.grid(row=0, column=5, padx=5, sticky="W")

Result = Text(root, height=20, width=69)
Result.grid(rowspan=10, columnspan=40, sticky='W', padx=5)

Scroll = Scrollbar(root, command=Result.yview)
Scroll.grid(row=1, column=6, ipady=135)
Result.config(yscrollcommand=Scroll.set)

root.mainloop()