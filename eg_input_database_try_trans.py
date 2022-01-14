from tkinter import *
import sqlite3

'''This part is connecting to the database, creating the tables, and adding data.
You can change this part by connecting to a different database, making different tables,
columns, datatypes, and inputs. But this is the basic format.'''

db_conn = sqlite3.connect('test_tutorial.db')

c = db_conn.cursor()

db_conn.execute('''CREATE TABLE IF NOT EXISTS Test3(Name, Age INT(2));''')

db_conn.commit()

db_conn.execute("INSERT INTO Test3 VALUES('Billy', 12);")

db_conn.commit()

db_conn.execute('''INSERT INTO Test3 VALUES('Bob', 35);''')

db_conn.commit()

rows = c.execute("SELECT name FROM sqlite_master WHERE type='table'")

e = [i[0] for i in rows.fetchall()]

'''Swiches between two frames in tkinter.'''


class MyApp(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)
        container.pack()

        self.frames = {}

        self.dict = {}

        for F in (StartPage, Data):
            frame = F(container, self, self.dict)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_window(StartPage)

    def show_window(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(Frame):
    def __init__(self, parent, controller, d):
        Frame.__init__(self, parent)

        for x in e:
            Label(self, text=x).pack()
            d[x] = Button(self, text=x,
                          command=lambda: controller.show_window(Data))
            d[x].pack()

            '''In this part, we create buttons by incrementing the table names in a dictionary.'''


class Data(Frame):
    def __init__(self, parent, controller, d):
        Frame.__init__(self, parent)

        data = []
        for x in e:
            text = (d[x])['text']
            rows = c.execute('''SELECT * FROM ''' + text)
            data = []
            for row in rows:
                data.append(list(row))

            label = data

            Label(self, text=label).pack()

            Button(self, text='Go to Start Page',
                   command=lambda: controller.show_window(StartPage)).pack()

            '''Here, we check the text config of each button and according to that
            select data out of that table. Then we create the labels and buttons
            that go back to the home page.'''


app = MyApp()
app.mainloop()