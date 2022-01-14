import os
import sqlite3
import datetime
import pandas as pd
class Sharemarket:
    id = 0
    def __init__(self,*args): # add self evaluating age later
        self.Name_Client = args[0]
        self.Dob = args[1]
        self.Gender = args[2]
        self.City = args[3]
        self.Email_Id = args[4]
        self.Contact_No = args[5]
        Sharemarket.id += 1

    def create_table_all_customers(self):
        try:
            if "All_Customers.db" not in os.listdir():
                with sqlite3.connect('All_Customers.db') as db:
                    cursor = db.cursor()
                    db.execute('''CREATE TABLE IF NOT EXISTS All_Customer_Details (ID INTEGER PRIMARY KEY AUTOINCREMENT, Name varchar(20), Dob date, 
                    Gender text, City text, Email_Id text, Contact_No int, Date_Open date  )''')
        except Exception as E:
            print("Error: ",E)
        else:
            print('Table Created Successfully All_Customers..')

    def insert_table_all_customers(self):
        Date = datetime.datetime.now().date()
        try:
            with sqlite3.connect('All_Customers.db') as db:
                cursor = db.cursor()
                cursor.execute('''INSERT INTO All_Customer_Details (Name , Dob, 
                    Gender, City, Email_Id, Contact_No, Date_Open) VALUES (?,?,?,?,?,?,?) ''', ( self.Name_Client,self.Dob,self.Gender,self.City,self.Email_Id,self.Contact_No,Date))
        except Exception as E:
            print("Error", E)
        else:
            db.commit()
            print("Data inserted Successfully in All_Customers...")

    def check_duplicate_entries(self):
        try:
            with sqlite3.connect('All_Customers.db')  as db:
                cursor = db.cursor()
                # cursor.execute('''SELECT Name,Dob as times from All_Customer_Details GROUP BY Name,Dob HAVING times>0''')
                cursor.execute('''SELECT Name,Dob from All_Customer_Details ''')
                for row in cursor.fetchall():
                    # print(row[0], self.Name_Client)
                    if self.Name_Client == row[0] and self.Dob == row[1]:
                        print(f'{self.Name_Client} already exists')
                        return True
        except:
            print('some')


def main():
    data_set = [('Liam', '1966-05-09', 'Male', 'Singapore', 'intlprog@aol.com', 9366057055), ('Noah', '1968-01-10', 'Male', 'Monterrey', 'grady@hotmail.com', 2225007421), ('William', '1969-08-16', 'Male', 'Zunyi', 'vganesh@outlook.com', 8317306377), ('James', '1969-08-18', 'Male', 'Palembang', 'jonadab@att.net', 3003535814), ('Logan', '1969-09-30', 'Male', 'Fortaleza', 'pspoole@outlook.com', 8514211417), ('Benjamin', '1969-12-25', 'Male', 'Lagos', 'wagnerch@sbcglobal.net', 5197052911), ('Mason', '1974-01-03', 'Male', 'Kwangju', 'stecoop@att.net', 4073468379), ('Elijah', '1981-08-24', 'Male', 'Montevideo', 'breegster@mac.com', 4594274621), ('Oliver', '1982-03-21', 'Male', 'Tangshan', 'crusader@verizon.net', 8628762953), ('Jacob', '1983-02-10', 'Male', 'Brisbane', 'druschel@gmail.com', 3399024748), ('Emma', '1984-09-25', 'Female', 'Istanbul', 'meder@att.net', 3952226485), ('Olivia', '1985-12-19', 'Female', 'Saitama', 'euice@msn.com', 4568645037), ('Ava', '1988-08-06', 'Female', 'Yaoundé', 'thrymm@verizon.net', 3323269801), ('Isabella', '1988-10-26', 'Female', 'Dhaka', 'moonlapse@aol.com', 4169310205), ('Sophia', '1990-09-04', 'Female', 'Cali', 'conteb@optonline.net', 4873797552), ('Mia', '1992-04-12', 'Female', 'Islamabad', 'isaacson@hotmail.com', 2047807950), ('Charlotte', '1993-08-10', 'Female', 'Shenyang', 'padme@optonline.net', 6583901307), ('Amelia', '1998-03-19', 'Female', "T'bilisi", 'rande@yahoo.com', 4017555096), ('Evelyn', '1998-11-26', 'Female', 'Campinas', 'shang@icloud.com', 2883749695), ('Abigail', '2000-09-19', 'Female', 'Khartoum', 'rtanter@aol.com', 6326848026)]
    for i in data_set:
        # print(i)
        Kish = Sharemarket(*i)
        Kish.create_table_all_customers()
        if Kish.check_duplicate_entries():
            continue
        Kish.insert_table_all_customers()
# def get_stocks_by_name(equity_name):
#     try:
#         with sqlite3.connect(name_client) as db:
#             cursor = db.cursor()
#             cursor.execute(f"""SELECT * FROM Transactions WHERE Equity_Name={equity_name}""")
#             return cursor.fetchall()
#     except Exception as E:
#         print("Error",E)
#     else:
#         db.commit()
#         print("Data retrieved Successfully...")

if __name__ == '__main__':
    # name = input("name")
    # dob = input('Dob')
    # Gender = input('Gender')
    # City = input('City')
    # Email = input('Email')
    # Contact_no = int(input('Contact no'))
    # Equity_Name = input(f"Type Equity List, You are willing to Transact {Equity_List}\n")
    # type_transaction = input("Type b for buy and s for sell")
    # if type_transaction == 'b':
    #     type = 'Buy'
    # elif type_transaction == 's':
    #     type = 'Sell'
    # number_Equity = int(input("Enter No of Equity to Trade"))
    main()
    # check_duplicate_entries()






