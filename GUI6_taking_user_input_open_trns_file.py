from tkinter import *
import sqlite3
from tkinter import *
import os
import datetime
from tkinter import messagebox


def view(name_client):
    try:
        with sqlite3.connect(name_client + '.db') as db:
            cursor = db.cursor()
            cursor.execute(f'SELECT * FROM Transactions')
            rows = cursor.fetchall()
            print(rows)
            return rows

    except Exception as E:
        print(f"Could not connect or no {name_client}")

def search( name_client, equity_name=""):
    try:
        with sqlite3.connect(name_client + '.db') as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM Transactions WHERE Equity_Name=?", (equity_name,))
            rows = cursor.fetchall()
            print(rows)
            return rows
    except Exception as E:
        print(f"Could not connect or no {name_client}")

def view_command():
    list1.delete(0, END)
    for row in view(e1.get()):
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in search(e1.get(),e2.get()):
        list1.insert(END, row)


root = Tk()

root.title('Name')

l1 = Label(root, text="Name Client")
l1.grid(row=0, column=0)

l1 = Label(root, text="Equity Name")
l1.grid(row=1, column=0)

e1 = Entry(root)
e1.grid(row=0, column=1)
e1.focus_set()

e2 = Entry(root)
e2.grid(row=1, column=1)

b1 = Button(root,text='View Trans',command=view_command)
b1.grid(row=0, column=2)

b2 = Button(root,text='View Share',command=search_command)
b2.grid(row=1, column=2)

sb1 = Scrollbar(root, orient='vertical')
sb1.grid(row=4, column=4, sticky='ns', rowspan=6)

list1 = Listbox(root, height=20, width=90, yscrollcommand=sb1.set)
list1.grid(row=4, column=0, rowspan=6, columnspan=4)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)


root.mainloop()