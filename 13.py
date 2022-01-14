import tkinter

root = tkinter.Tk()

# Scrollbar erstellen
scrollbar = tkinter.Scrollbar(root, orient='vertical')
scrollbar.grid(row=0, column=1, sticky='ns')

# Listbox erstellen
listbox = tkinter.Listbox(root, width=30, height=10, yscrollcommand=scrollbar.set )
listbox.grid(row=0, column=0)

# Scrollbar an Listbox binden
scrollbar.config(command=listbox.yview)

# Listbox befüllen
for i in range(30):
    listbox.insert('end', i)


root.mainloop()