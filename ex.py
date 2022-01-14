from tkinter import *
def getScript(event):
    state = rb.get()
    listScript = []
    processor = ()
    processor = lb1.get(lb1.curselection())
    if processor :
        if (state == 1):
            print (processor)
        if (state == 2):
            pass
        if (state == 3):
            pass

root = Tk()
root = Frame()
root.pack(fill = X)
rb = IntVar()

R1 = Radiobutton(root, text = "Parallel Test",
                 variable = rb, value = 1, command = getScript)
R2 = Radiobutton(root, text = "Non Parallel Test",
                 variable = rb, value = 2, command = getScript)
R3 = Radiobutton(root, text = "Specific Test",
                 variable = rb, value = 3, command = getScript)

R1.grid(row = 0, column = 0, padx = 10)
R2.grid(row = 0, column = 1, padx = 10)
R3.grid(row = 0, column = 2, padx = 10)

root = Frame()
root.pack(fill = X)
space_frame3 = Frame(root, width = 10)
l5 = Label(root, text = "Processor Unit")
l6 = Label(root, text = "Script for test")
lb1 = Listbox(root, height = 7, exportselection = 0)
lb1.bind('<<ListboxSelect>>',getScript)
scrollbar = Scrollbar(root)
lb2 = Listbox(root, height = 7, width = 40,
              yscrollcommand = scrollbar.set, exportselection = 0)


# frame2.mainloop()
root.mainloop()