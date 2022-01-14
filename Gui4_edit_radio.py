import sqlite3
from tkinter import *
import os
import datetime
from tkinter import messagebox

class Sharemarket:
    id = 0
    def __init__(self): # add self evaluating age later
        # self.Name_Client = args[0]
        #         # self.Dob = args[1]
        #         # self.Gender = args[2]
        #         # self.City = args[3]
        #         # self.Email_Id = args[4]
        #         # self.Contact_No = args[5]
        #         # Sharemarket.id += 1
        self.db = sqlite3.connect('All_Customers.db')
        self.cursor = self.db.cursor()
        self.db.execute('''CREATE TABLE IF NOT EXISTS All_Customer_Details (ID INTEGER PRIMARY KEY AUTOINCREMENT, Name varchar(20), Dob date, 
            Gender text, City text, Email_Id text, Contact_No int, Date_Open date  )''')


    def __del__(self):
        self.db.close()

    def insert(self,Name_Client, Dob, Gender, City, Email_Id, Contact_No):
        Date = datetime.datetime.now().date()
        try:
            self.cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ= '0' WHERE NAME='All_Customer_Details'")
            self.db.commit()
            self.cursor.execute('''INSERT INTO All_Customer_Details (Name , Dob, 
                    Gender, City, Email_Id, Contact_No, Date_Open) VALUES (?,?,?,?,?,?,?) ''', ( Name_Client,Dob,Gender,City,Email_Id,Contact_No,Date))
        except Exception as E:
            print("Error", E)
        else:
            self.db.commit()
            print("Data inserted Successfully in All_Customers...")

    def check_duplicate_entries(self,Name_Client,Dob):
        try:
            if self.cursor.execute('''SELECT Name,Dob from All_Customer_Details WHERE Name=? AND Dob=? ''',(Name_Client,Dob)).fetchall():
                print(1,'True')
                return True
            else:
                print(2,'False')
                return False
        except:
            print('some')

    def update(self,Gender, City, Email_Id,Contact_No, Name, Dob):
        try:
            self.cursor.execute("UPDATE All_Customer_Details SET Gender=?, City=?, Email_Id=?, Contact_No=? WHERE Name=? and Dob=?", (Gender, City, Email_Id, Contact_No,Name, Dob))
            self.view()
        except Exception as E:
            print("While updating update",E)

    def view(self):
        try:
            self.cursor.execute("SELECT * FROM All_Customer_Details")
            rows = self.cursor.fetchall()
            return rows
        except Exception as E:
            print("While viewing view",E)

    def delete(self,Name_Client,Dob):
        try:
            self.cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ= '0' WHERE NAME='All_Customer_Details'")
            self.db.commit()
            self.cursor.execute("DELETE FROM All_Customer_Details WHERE Name=? and Dob=?", (Name_Client, Dob))
            self.db.commit()
            self.view()
        except Exception as E:
            print("While searching delete", E)

    def search(self,Name_Client,Dob):
        try:
            self.cursor.execute("SELECT * FROM All_Customer_Details WHERE Name=? and Dob=?",(Name_Client,Dob))
            rows = self.cursor.fetchall()
            return rows
        except Exception as E:
            print("While searching search",E)

sharemarket = Sharemarket()

def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()
    selected_tuple = list1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    # e3.delete(0, END)
    # e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])
    e5.delete(0, END)
    e5.insert(END, selected_tuple[5])
    e6.delete(0, END)
    e6.insert(END, selected_tuple[6])

def view_command():
    list1.delete(0, END)
    for row in sharemarket.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in sharemarket.search( Name_Client.get(), Dob.get()):
        list1.insert(END, row)

def add_command():
    if sharemarket.check_duplicate_entries(Name_Client.get(),Dob.get()):
        messagebox.showinfo("Caution", f"Entry Already Exists {Name_Client.get()} ")

    else:
        sharemarket.insert(Name_Client.get(), Dob.get(), Gender.get(),City.get(), Email_Id.get(), Contact_No.get())
        list1.delete(0, END)
        list1.insert(END, (Name_Client.get(), Dob.get(), Gender.get(),City.get(), Email_Id.get(), Contact_No.get()))

def delete_command():
    sharemarket.delete(Name_Client.get(), Dob.get())#(selected_tuple[0])

def update_command():
    sharemarket.update( Gender.get(), City.get(), Email_Id.get(),Contact_No.get(),Name_Client.get(), Dob.get())


def on_closing():
    dd = sharemarket
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
        del dd

window = Tk()

window.title("Jumbo Jack Financial Consultants")

window.protocol("WM_DELETE_WINDOW", on_closing)  # handle window closing

l1 = Label(window, text="Name Client")
l1.grid(row=0, column=0)

l2 = Label(window, text="Dob")
l2.grid(row=0, column=2)

l4 = Label(window, text="City")
l4.grid(row=1, column=0)

l5 = Label(window, text="Email Id")
l5.grid(row=1, column=2)

l6 = Label(window, text="Contact No")
l6.grid(row=1, column=4)


Name_Client = StringVar()
e1 = Entry(window, textvariable=Name_Client)
e1.grid(row=0, column=1)

Dob = StringVar()
e2 = Entry(window, textvariable=Dob)
e2.grid(row=0, column=3)

Gender = StringVar()
Gender.set('Gender')
e3 = Radiobutton(window, text="Male", padx=14, variable=Gender, value="Male").grid(row=0, column=4)
e3 = Radiobutton(window, text="Female", padx=14, variable=Gender, value="Female").grid(row=0, column=5)

City = StringVar()
e4 = Entry(window, textvariable=City)
e4.grid(row=1, column=1)

Email_Id = StringVar()
e5 = Entry(window, textvariable=Email_Id)
e5.grid(row=1, column=3)

Contact_No = StringVar()
e6 = Entry(window, textvariable=Contact_No)
e6.grid(row=1, column=5)

sb1 = Scrollbar(window,orient='vertical')
sb1.grid(row=4, column=4, sticky='ns',rowspan=6)

list1 = Listbox(window, height=20, width=90,yscrollcommand=sb1.set)
list1.grid(row=4, column=0,rowspan=6,columnspan=4)

# list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View all", width=12, command=view_command)
b1.grid(row=4, column=5)

b2 = Button(window, text="Search entry", width=12, command=search_command)
b2.grid(row=5, column=5)

b3 = Button(window, text="Add entry", width=12, command=add_command)
b3.grid(row=6, column=5)

b4 = Button(window, text="Update selected", width=12, command=update_command)
b4.grid(row=7, column=5)

b5 = Button(window, text="Delete selected", width=12, command=delete_command)
b5.grid(row=8, column=5)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=9, column=5)

window.mainloop()

#'Abigail', '2000-09-19', 'Female', 'Khartoum', 'rtanter@aol.com', 6326848026