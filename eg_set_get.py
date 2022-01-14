# Importing tkinter module
# and all functions
from tkinter import *
from tkinter.ttk import *

# creating master window
master = Tk()

# Entry widget
e1 = Entry(master)
e1.pack(expand=1, fill=BOTH)

# Button widget which currently has the focus
e2 = Button(master, text="Button")

# here focus_set() method is used to set the focus
e2.focus_set()
e2.pack(pady=5)

# Radiobuton widget
e3 = Radiobutton(master, text="Hello")
e3.pack(pady=5)

# Infinite loop
mainloop()