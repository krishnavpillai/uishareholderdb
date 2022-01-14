import tkinter
import sqlite3

with sqlite3.connect('All_Customers.db') as db:
    cursor = db.cursor()
    cursor.execute('SELECT * FROM All_Customer_Details')
    All_Customer_Details = [row[0] for row in cursor.fetchall()]

class MyApp(Tk,*args,**kwargs):
    def __init__(self):
        Tk.__init__(self,*args,**kwargs)
        container = Frame(self)
        containe.pack()

        self.frames = {}
        self.dict = {}

        for F
