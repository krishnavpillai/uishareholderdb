from tkinter import *
import sqlite3

con = sqlite3.connect('test.db')
cur = con.cursor()

class Welcome():
    def __init__(self,master):
        self.master = master
        self.master.geometry('170x110+100+200')
        self.master.title('Welcome!')
        self.label1=Label(self.master,text='Test Database Main Menu',fg='red').grid(row=0,column=1)
        self.button1=Button(self.master,text="Enter Data",fg='green',command=self.gotodataentry).grid(row=1,column=1)
        self.button2=Button(self.master,text="Data Records",fg='blue',command=self.gotorecords).grid(row=2,column=1)
        self.button3=Button(self.master,text="Exit",fg='red',command=self.exit).grid(row=3,column=1)

    def exit(self):
        self.master.destroy()

    def gotodataentry(self):
        root2=Toplevel(self.master)
        myGUI=DataEntry(root2)

    def gotorecords(self):
        root2=Toplevel(self.master)
        mygui=Records(root2)

class DataEntry():
    def __init__(self,master):
        self.master = master
        self.master.geometry('250x200+100+200')
        self.master.title('Data Entry')

        self.label2=Label(self.master,text='Welcome to the data entry menu',fg='red').grid(row=0,column=0)
        self.label3=Label(self.master,text='Please enter some text',fg='black').grid(row=3,column=0)
        self.label4=Label(self.master,text='Please enter a number',fg='black').grid(row=4,column=0)

        self.text1=StringVar()
        self.text_entry=Entry(self.master,textvariable=self.text1).grid(row=3,column=1)
        self.int1=IntVar()
        self.int_entry=Entry(self.master,textvariable=self.int1).grid(row=4,column=1)
        self.button4=Button(self.master,text="Save",fg='red',command=lambda: self.savedata(self.text1.get(), self.int1.get())).grid(row=7,column=0)
        self.button5=Button(self.master,text="Exit",fg='red',command=self.exit).grid(row=9,column=0)

    def exit(self):
        self.master.destroy()

    def savedata(self, text1, int1):
        con = sqlite3.connect('test.db')
        cur = con.cursor()
        cur.execute('INSERT INTO Data (t1, i1) VALUES (?,?)', (text1, int1))
        con.commit()
        print('Record inserted in Data')

class Records:
    def __init__(self, master):
        self.master = master
        self.master.geometry('250x200+100+200')
        self.master.title('Records')
        self.connection = sqlite3.connect('test.db')
        self.cur = self.connection.cursor()
        self.textLabel = Label(self.master, text="Text", width=10)
        self.textLabel.grid(row=0, column=0)
        self.intLabel = Label(self.master, text="Number", width=10)
        self.intLabel.grid(row=0, column=1)
        self.showallrecords()

    def showallrecords(self):
        Data = self.readfromdatabase()
        for index, dat in enumerate(Data):
            Label(self.master, text=dat[0]).grid(row=index+1, column=0)
            Label(self.master, text=dat[1]).grid(row=index+1, column=1)

    def readfromdatabase(self):
        self.cur.execute("SELECT * FROM Data")
        return self.cur.fetchall()

def main():
     root=Tk()
     myGUIWelcome=Welcome(root)
     root.mainloop()

if __name__ == '__main__':
     main()