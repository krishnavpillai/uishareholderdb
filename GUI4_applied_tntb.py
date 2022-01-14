from tkinter import *
import sqlite3
from webscraping_1 import parsePrice, parsePriceSingle,priceDatareaderDate

from tkinter import *
import os
import datetime
from tkinter import messagebox
import pandas as pd
import time
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

    def search(self,Name_Client):
        try:
            self.cursor.execute("SELECT * FROM All_Customer_Details WHERE Name=? ",(Name_Client,)) #and Dob=? ,Dob
            rows = self.cursor.fetchall()
            return rows
        except Exception as E:
            print("While searching search",E)

# class TransactionTable:
#     # def __init__(self,name_client):
#     #     self.db = sqlite3.connect(name_client+'.db')
#     #     self.cursor = self.db.cursor()
#     #     self.db.execute('''CREATE TABLE IF NOT EXISTS Transactions ( ID INTEGER PRIMARY KEY AUTOINCREMENT,Equity_Name text,Date text,
#     #                     Type text, Cost float, Number int, Total float)''')
#     #     self.db.commit()
#     #
#     # def __del__(self):
#     #     self.db.close()
#
#
#     def view(name_client):
#         try:
#             with sqlite3.connect(name_client + '.db') as db:
#                 cursor = db.cursor()
#                 cursor.execute(f'SELECT * FROM Transactions')
#                 for row in cursor.fetchall():
#                     print(row)
#         except Exception as E:
#             print(f"Could not connect or no {name_client}")
#
#     def search( equity_name=""):
#         cursor.execute("SELECT * FROM Transactions WHERE Equity_Name=?", (equity_name,))
#         rows = cursor.fetchall()
#         return rows

LARGE_FONT = ('Verdana',12)

class SeaofBTCapp(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)
        container.pack(side="top",fill='both', expand='True')
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.frames = {}
        for F in (StartPage,PageOne,PageTwo,PageThree):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0,column =0, sticky="nsew")
        self.show_frame(StartPage)
        self.title("Jumbo Jack Financial Consultants")

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(Frame):

    def __init__(self,parent, controller):
        Frame.__init__(self, parent)


        sharemarket = Sharemarket()

        def get_selected_row(event):
            global selected_tuple
            index = list1.curselection()[0]
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
            for row in sharemarket.search(Name_Client.get()):#, Dob.get()
                list1.insert(END, row)

        def add_command():
            if len(Name_Client.get()) == 0 or len(Dob.get()) == 0 or len(Gender.get()) == 0 or len(City.get()) == 0 or len(Email_Id.get()) == 0 or len(Contact_No.get()) == 0 :
                # filtered = filter(len,(Name_Client.get(),Dob.get(),Gender.get(),City.get(),Email_Id.get(),Contact_No.get()))
                list2 = [Name_Client.get(),Dob.get(),Gender.get(),City.get(),Email_Id.get(),Contact_No.get()]
                # l = [i for i in list2 if filter(len, list2)]
                # for i in l:
                #     print(i)
                    # list1.remove(i)
                # print(list1)
                # for i in filtered:
                #     print(i)
                messagebox.showinfo("Caution", f"Box should not be empty {list2} ")
            else:
                if sharemarket.check_duplicate_entries(Name_Client.get(), Dob.get()):
                    messagebox.showinfo("Caution", f"Entry Already Exists {Name_Client.get()} ")

                else:
                    sharemarket.insert(Name_Client.get(), Dob.get(), Gender.get(), City.get(), Email_Id.get(),
                                       Contact_No.get())
                    list1.delete(0, END)
                    list1.insert(END,
                                 (Name_Client.get(), Dob.get(), Gender.get(), City.get(), Email_Id.get(), Contact_No.get()))

        def delete_command():
            sharemarket.delete(Name_Client.get(), Dob.get())  # (selected_tuple[0])

        def update_command():
            if len(Name_Client.get()) == 0 or len(Dob.get()) == 0 or len(Gender.get()) == 0 or len(City.get()) == 0 or len(Email_Id.get()) == 0 or len(Contact_No.get()) == 0 :
                filtered = filter(len,(Name_Client.get(),Dob.get(),Gender.get(),City.get(),Email_Id.get(),Contact_No.get()))
                for i in filtered:
                    print(i)
                messagebox.showinfo("Caution", f"Box should not be empty {Name_Client.get()} ")
            else:
                sharemarket.update(Gender.get(), City.get(), Email_Id.get(), Contact_No.get(), Name_Client.get(), Dob.get())

        def on_closing():
            dd = sharemarket
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.destroy()
                del dd

        # self.protocol("WM_DELETE_WINDOW", on_closing)  # handle window closing

        l1 = Label(self, text="Name Client")
        l1.grid(row=0, column=0)

        l2 = Label(self, text="Dob")
        l2.grid(row=0, column=2)

        # l3 = Label(self, text="Gender")
        # l3.grid(row=0, column=4)

        l4 = Label(self, text="City")
        l4.grid(row=1, column=0)

        l5 = Label(self, text="Email Id")
        l5.grid(row=1, column=2)

        l6 = Label(self, text="Contact No")
        l6.grid(row=1, column=4)

        Name_Client = StringVar()
        e1 = Entry(self, textvariable=Name_Client)
        e1.grid(row=0, column=1)

        Dob = StringVar()
        e2 = Entry(self, textvariable=Dob)
        e2.grid(row=0, column=3)

        Gender = StringVar()
        Gender.set("Female")
        e3 = Radiobutton(self, text="Male", padx=14, variable=Gender, value="Male",command = lambda : selected_tuple[3]).grid(row=0, column=4)
        e3 = Radiobutton(self, text="Female", padx=14, variable=Gender, value="Female",command = lambda : selected_tuple[3]).grid(row=0, column=5)

        City = StringVar()
        e4 = Entry(self, textvariable=City)
        e4.grid(row=1, column=1)

        Email_Id = StringVar()
        e5 = Entry(self, textvariable=Email_Id)
        e5.grid(row=1, column=3)

        Contact_No = StringVar()
        e6 = Entry(self, textvariable=Contact_No)
        e6.grid(row=1, column=5)

        sb1 = Scrollbar(self, orient='vertical')
        sb1.grid(row=4, column=4, sticky='ns', rowspan=6)

        list1 = Listbox(self, height=20, width=90, yscrollcommand=sb1.set)
        list1.grid(row=4, column=0, rowspan=6, columnspan=4)

        # list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview)

        list1.bind('<<ListboxSelect>>', get_selected_row)

        b1 = Button(self, text="View all", width=12, command=view_command)
        b1.grid(row=4, column=5)

        b2 = Button(self, text="Search entry", width=12, command=search_command)
        b2.grid(row=5, column=5)

        b3 = Button(self, text="Add entry", width=12, command=add_command)
        b3.grid(row=6, column=5)

        b4 = Button(self, text="Update selected", width=12, command=update_command)
        b4.grid(row=7, column=5)

        b5 = Button(self, text="Delete selected", width=12, command=delete_command)
        b5.grid(row=8, column=5)

        b6 = Button(self, text="Close", width=12, command=self.destroy)
        b6.grid(row=9, column=5)

        label = Label(self, text = 'Start Page', font=LARGE_FONT)
        label.grid(row=10, column=0)
        button1 = Button(self,text="Visit Transaction Page",
                         command= lambda :controller.show_frame(PageOne))
        button1.grid(row=11, column=0)
        button2 = Button(self, text="Visit Summary Page",
                         command=lambda: controller.show_frame(PageTwo))
        button2.grid(row=11, column=1)
        button3 = Button(self, text="Buy/Sell Page",
                         command=lambda: controller.show_frame(PageThree))
        button3.grid(row=11, column=2)

class PageOne(Frame):

    def __init__(self,parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text = 'Page One', font=LARGE_FONT)
        label.grid(row=10, column=0)
        button1 = Button(self,text="Back to Home",
                         command= lambda :controller.show_frame(StartPage))
        button1.grid(row=11, column=0)
        button2 = Button(self, text="Summary Page",
                         command=lambda: controller.show_frame(PageTwo))
        button2.grid(row=11, column=1)
        button3 = Button(self, text="Buy/Sell Page",
                         command=lambda: controller.show_frame(PageThree))
        button3.grid(row=11, column=2)
        # tntb = TransactionTable('Liam')

        def view(name_client):
            try:
                with sqlite3.connect(name_client + '.db') as db:
                    cursor = db.cursor()
                    cursor.execute(f'SELECT * FROM Transactions')
                    rows = cursor.fetchall()
                    # print(rows)
                    return rows

            except Exception as E:
                print(f"Could not connect or no {name_client}")

        def search(name_client, equity_name=""):
            try:
                with sqlite3.connect(name_client + '.db') as db:
                    cursor = db.cursor()
                    cursor.execute("SELECT * FROM Transactions WHERE Equity_Name=?", (equity_name,))
                    rows = cursor.fetchall()
                    # print(rows)
                    return rows
            except Exception as E:
                print(f"Could not connect or no {name_client}")

        def view_command():
            list1.delete(0, END)
            for row in view(e1.get()):
                list1.insert(END, row)

        def search_command():
            list1.delete(0, END)
            for row in search(e1.get(), e2.get()):
                list1.insert(END, row)

        l1 = Label(self, text="Name Client")
        l1.grid(row=0, column=0)

        l1 = Label(self, text="Equity Name")
        l1.grid(row=1, column=0)

        e1 = Entry(self)
        e1.grid(row=0, column=1)
        e1.focus_set()

        e2 = Entry(self)
        e2.grid(row=1, column=1)

        b1 = Button(self, text='View Transactions', command=view_command)
        b1.grid(row=0, column=2)

        b2 = Button(self, text='View Equity', command=search_command)
        b2.grid(row=1, column=2)

        sb1 = Scrollbar(self, orient='vertical')
        sb1.grid(row=4, column=4, sticky='ns', rowspan=6)

        list1 = Listbox(self, height=20, width=90, yscrollcommand=sb1.set)
        list1.grid(row=4, column=0, rowspan=6, columnspan=4)

        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview)

class PageTwo(Frame):

    def __init__(self,parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text = 'Summary Page', font=LARGE_FONT)
        label.grid(row=10, column=0)
        button1 = Button(self,text="Back to Home",
                         command= lambda :controller.show_frame(StartPage))
        button1.grid(row=11, column=0)
        button2 = Button(self, text="Transaction Page",
                         command=lambda: controller.show_frame(PageOne))
        button2.grid(row=11, column=1)
        button3 = Button(self, text="Buy/Sell Page",
                         command=lambda: controller.show_frame(PageThree))
        button3.grid(row=11, column=2)

        def view(name_client):
            try:
                with sqlite3.connect(name_client + '.db') as db:
                    cursor = db.cursor()
                    cursor.execute(f'SELECT * FROM Summary')
                    rows = cursor.fetchall()
                    # print(rows)
                    return rows

            except Exception as E:
                print(f"Could not connect or no {name_client}")

        def search(name_client, equity_name=""):
            try:
                with sqlite3.connect(name_client + '.db') as db:
                    cursor = db.cursor()
                    cursor.execute("SELECT * FROM Summary WHERE Equity_Name=?", (equity_name,))
                    rows = cursor.fetchall()
                    # print(rows)
                    return rows
            except Exception as E:
                print(f"Could not connect or no {name_client}")

        def compute_summary_from_database(name_client):
            with sqlite3.connect(name_client + '.db') as db:
                try:
                    print(pd.read_sql('select * from Transactions', db).head())
                    sql_select = "select Equity_Name from Transactions "
                    allEquityClient = pd.read_sql(sql_select, db)
                    allEquityClientList = allEquityClient['Equity_Name'].tolist()
                    allEquityClientList = set(allEquityClientList)
                    allEquityClientList = list(allEquityClientList)
                    allEquityClientList.sort()
                    print(allEquityClientList)
                    for equity_name in allEquityClientList[:10]:
                        print(f'In for loop {equity_name}')
                        try:
                            print('Hi')
                            # equity_name = 'TCS.NS'
                            # equity_name, current_price, number, total_Cost, profit_loss
                            currentPrice = parsePriceSingle(equity_name)
                            print(1, currentPrice, 'currentprice')
                            sqlClientEquityBuy = f"SELECT Number from Transactions WHERE (Equity_Name='{equity_name}' AND Type='Buy') "
                            equityBought = pd.read_sql(sqlClientEquityBuy, db).sum()
                            print(2, equityBought, 'equitybought')
                            sqlClientEquitySell = f"SELECT Number from Transactions WHERE (Equity_Name='{equity_name}' AND Type='Sell') "
                            equitySold = pd.read_sql(sqlClientEquitySell, db).sum()
                            print(22, equitySold, 'equitysold')
                            number = (equityBought - equitySold)
                            number = number.astype('float64')
                            print(3, number[0], type(number[0]), number, type(number))
                            sqlClientEquityBuyTotal = f"SELECT Total from Transactions WHERE (Equity_Name='{equity_name}' AND Type='Buy') "
                            EquityBuyTotal = pd.read_sql(sqlClientEquityBuyTotal, db).sum()
                            print(4, EquityBuyTotal[0], 'eautiybuytotal')
                            sqlClientEquitySellTotal = f"SELECT Total from Transactions WHERE (Equity_Name='{equity_name}' AND Type='Sell') "
                            EquitySellTotal = pd.read_sql(sqlClientEquitySellTotal, db).sum()
                            print(5, EquitySellTotal, 'equity soldtotal')
                            total_cost = round(EquityBuyTotal - EquitySellTotal, 2)
                            print(6, total_cost[0], 'totalcost')
                            profit_loss = round(number[0] * currentPrice - total_cost[0], 2)
                            print(9, profit_loss, 'profitloss')
                            insert_table_Summary(name_client, equity_name, currentPrice, number[0], total_cost[0],
                                                 profit_loss)
                        except Exception as E:
                            print(f"Insertion into summary table of {equity_name} failed due to {E}")
                except Exception as E:
                    print(f"The database {name_client} has error {E}")
                # print(pd.read_sql('select * from Summary', db))

        def insert_table_Summary(name_client, equity_name, current_price, number, total_cost, profit_loss):
            try:
                with sqlite3.connect(name_client + '.db') as db:
                    cursor = db.cursor()
                    cursor.execute('''INSERT INTO Summary (Equity_Name, 
                         Current_Price, Number, Total_Cost, Profit_Loss) VALUES (?,?,?,?,?) ''',
                                   (equity_name, current_price,
                                    number, total_cost, profit_loss))
            except Exception as E:
                print(f'Entry into Summary Table of {name_client} failed due to {E}')
            else:
                db.commit()
                print(f"Data inserted successfully into Summary of {name_client} ")

        def create_table_Summary(name_client):
            with sqlite3.connect(name_client + '.db') as db:
                try:
                    db.execute(
                        f'''CREATE TABLE Summary (ID INTEGER PRIMARY KEY AUTOINCREMENT,Equity_Name text, 
                         Current_Price float, Number float, Total_Cost float, Profit_Loss float)''')
                except Exception as E:
                    print("Error: ", E)
                else:
                    print('Table Summary Created Successfully..')

        def delete_table_contents(name_Client, table_name):
            Name_Client = name_Client
            try:
                with sqlite3.connect(Name_Client + '.db') as db:
                    cursor = db.cursor()
                    cursor.execute(f"DROP TABLE IF EXISTS {table_name} ")
            except Exception as E:
                print("Error: ", E)
            else:
                db.commit()
                print("Table Summary Deleted Succesfully")

        def view_command():
            list1.delete(0, END)
            for row in view(e1.get()):
                list1.insert(END, row)

        def search_command():
            list1.delete(0, END)
            for row in search(e1.get(), e2.get()):
                list1.insert(END, row)

        def regenrate_summary_table():
            print(1)
            print(e1.get())
            delete_table_contents(e1.get(),'Summary')
            print(2)
            create_table_Summary(e1.get())
            print(3)
            messagebox.showinfo("Wait Table is being Regenerated ")
            Time1 = time.time()
            compute_summary_from_database(e1.get())
            print(Time1 - time.time())
            list1.delete(0, END)
            for row in view(e1.get()):
                list1.insert(END, row)


        l1 = Label(self, text="Name Client")
        l1.grid(row=0, column=0)

        l1 = Label(self, text="Equity Name")
        l1.grid(row=1, column=0)

        e1 = Entry(self)
        e1.grid(row=0, column=1)
        e1.focus_set()

        e2 = Entry(self)
        e2.grid(row=1, column=1)

        b1 = Button(self, text='View Summary', command=view_command)
        b1.grid(row=0, column=2)

        b2 = Button(self, text='View Equity', command=search_command)
        b2.grid(row=1, column=2)

        b3 = Button(self, text='Regenerate Table', command=regenrate_summary_table)
        b3.grid(row=0, column=4)

        sb1 = Scrollbar(self, orient='vertical')
        sb1.grid(row=4, column=4, sticky='ns', rowspan=6)

        list1 = Listbox(self, height=20, width=90, yscrollcommand=sb1.set)
        list1.grid(row=4, column=0, rowspan=6, columnspan=4)

        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview)

class PageThree(Frame):

    def __init__(self,parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text = 'Buy/Sell', font=LARGE_FONT)
        label.grid(row=10, column=0)
        button1 = Button(self,text="Back to Home",
                         command= lambda :controller.show_frame(StartPage))
        button1.grid(row=11, column=0)
        button2 = Button(self, text="Transaction Page",
                         command=lambda: controller.show_frame(PageOne))
        button2.grid(row=11, column=1)
        button3 = Button(self, text="Summary Page",
                         command=lambda: controller.show_frame(PageTwo))
        button3.grid(row=11, column=2)
        def view(name_client):
            try:
                with sqlite3.connect(name_client + '.db') as db:
                    cursor = db.cursor()
                    cursor.execute(f'SELECT * FROM Summary')
                    rows = cursor.fetchall()
                    # print(rows)
                    return rows
            except Exception as E:
                print(f"Could not connect or no {name_client}")

        def search(name_client, equity_name=""):
            try:
                with sqlite3.connect(name_client + '.db') as db:
                    cursor = db.cursor()
                    cursor.execute("SELECT * FROM Summary WHERE Equity_Name=?", (equity_name,))
                    rows = cursor.fetchall()
                    # print(rows)
                    return rows
            except Exception as E:
                print(f"Could not connect or no {name_client}")

        def view_command():
            list1.delete(0, END)
            for row in view(e1.get()):
                list1.insert(END, row)

        def search_command():
            list1.delete(0, END)
            for row in search(e1.get(), e2.get()):
                list1.insert(END, row)

        def insert_table_transaction(name_Client, equity_name, Date, type_trans, Cost, Numbers, Total):
            Name_Client = name_Client
            try:
                with sqlite3.connect(Name_Client + '.db') as db:
                    cursor = db.cursor()
                    cursor.execute(f'''INSERT INTO Transactions (Equity_Name ,Date , 
                        Type , Cost , Number , Total ) VALUES (?,?,?,?,?,?) ''', (equity_name, Date,
                                                                                  type_trans, Cost, Numbers, Total))
            except Exception as E:
                print("Error", E)
            else:
                db.commit()
                print("Data inserted Successfully...")

        def check_sell_buy_no_balance(name_client, equity_name, date_sample, numbers):
            '''Returns true if no balance. ie number > buy -sell'''
            Name_Client = name_client
            with sqlite3.connect(Name_Client + '.db') as db:
                print(1)
                try:
                    sql_buy = f"select Number from Transactions where (Equity_Name='{equity_name}' and Type='Buy' and Date<'{date_sample}' ) "
                    print(2)
                    dfbuy = pd.read_sql(sql_buy, db).sum()
                    dfbuy = dfbuy[0]
                    print(3)
                except Exception as E:
                    print(4)
                    print(f'{equity_name} has no Buy {E} ')
                    print(5)
                    return True
                else:
                    print(6)

                    print(7)
                    try:
                        sql_sell = f"select Number from Transactions where (Equity_Name='{equity_name}' and Type='Sell' and Dob<'{date_sample}' ) "
                        dfsell = pd.read_sql(sql_sell, db).sum()
                        dfsell = dfsell[0]
                        print(8)
                    except:
                        dfsell = 0
                        print(9)
                print(dfbuy, dfsell, numbers)
                print((numbers > dfbuy - dfsell))
                return (numbers > dfbuy - dfsell)

        def buy():
            Datetoday = datetime.now().date()
            Cost = parsePriceSingle(e2.get())
            numbers = e3.get()
            total = round(Cost * numbers, 2)
            insert_table_transaction(e1.get(),e2.get(),Datetoday,'Buy',Cost,numbers,total)

        def sell():
            Datetoday = datetime.now().date()
            name_client = e1.get()
            equity_name = e2.get()
            Cost = parsePriceSingle(equity_name)
            numbers = e3.get()
            total = round(Cost * numbers, 2)
            # if check_sell_buy_no_balance(name_client,equity_name,Datetoday,numbers):
            #     with sqlite3.connect(name_client + '.db') as db:
            #         try:
            #             sql_buy = f"select Number from Summary where (Equity_Name='{equity_name}' ) "
            #             dfbuy = pd.read_sql(sql_buy, db).sum()
            #             dfbuy = dfbuy[0]
            #             messagebox.showinfo("Caution", f"Number of Shares of {equity_name} are {dfbuy} ")
            # # else:
            #     a = insert_table_transaction(name_client,equity_name,Datetoday,'Sell',Cost,numbers,total)

        l1 = Label(self, text="Name Client")
        l1.grid(row=0, column=0)

        l1 = Label(self, text="Equity Name")
        l1.grid(row=1, column=0)

        l3 = Label(self, text="Number of Stocks")
        l3.grid(row=0, column=3)

        e1 = Entry(self)
        e1.grid(row=0, column=1)
        e1.focus_set()

        e2 = Entry(self)
        e2.grid(row=1, column=1)

        e3 = Entry(self)
        e3.grid(row=0, column=4)


        b1 = Button(self, text='View Summary', command=view_command)
        b1.grid(row=0, column=2)

        b2 = Button(self, text='View Equity', command=search_command)
        b2.grid(row=1, column=2)

        b3 = Button(self, text='Buy', command=buy)
        b3.grid(row=1, column=3,sticky='ew')

        b4 = Button(self, text='Sell', command=sell)
        b4.grid(row=1, column=4,sticky='ew')

        sb1 = Scrollbar(self, orient='vertical')
        sb1.grid(row=4, column=4, sticky='ns', rowspan=6)

        list1 = Listbox(self, height=20, width=90, yscrollcommand=sb1.set)
        list1.grid(row=4, column=0, rowspan=6, columnspan=4,sticky='nsew')

        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview)


app = SeaofBTCapp()
app.mainloop()

