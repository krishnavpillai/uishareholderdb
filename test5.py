import datetime
import sqlite3

def insert_table_all_customers(Name_Client, Dob, Gender, City, Email_Id, Contact_No):
    Date = datetime.datetime.now().date()
    try:
        with sqlite3.connect('All_Customers.db') as db:
            cursor = db.cursor()
            cursor.execute('''INSERT INTO All_Customer_Details (Name , Dob, 
                Gender, City, Email_Id, Contact_No, Date_Open) VALUES (?,?,?,?,?,?,?) ''',
                           (Name_Client, Dob, Gender, City, Email_Id, Contact_No, Date))
    except Exception as E:
        print("Error", E)
    else:
        db.commit()
        print("Data inserted Successfully in All_Customers...")

insert_table_all_customers('Liam','1966-05-07',"","","","")