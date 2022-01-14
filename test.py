import sqlite3
# def check_duplicate_entries(self ,Name_Client ,Dob):
#
#     self.cursor.execute('''SELECT Name,Dob from All_Customer_Details WHERE Name=? AND Dob=? ''' ,(Name_Client ,Dob))
#     return True


def check_duplicate_entries(Name_Client,Dob):
    try:
        with sqlite3.connect('All_Customers.db')  as db:
            cursor = db.cursor()
            # cursor.execute('''SELECT Name,Dob as times from All_Customer_Details GROUP BY Name,Dob HAVING times>0''')
            cursor.execute('''SELECT Name,Dob from All_Customer_Details ''')
            for row in cursor.fetchall():
                # print(row[0], self.Name_Client)
                if Name_Client == row[0] and Dob == row[1]:
                    print(f'{Name_Client} already exists')
                    return True
    except:
        print('some')

def check_duplicate_entries2(Name_Client,Dob):
    try:
        with sqlite3.connect('All_Customers.db')  as db:
            cursor = db.cursor()
            # cursor.execute('''SELECT Name,Dob as times from All_Customer_Details GROUP BY Name,Dob HAVING times>0''')
            if cursor.execute('''SELECT Name,Dob from All_Customer_Details WHERE Name=? AND Dob=? ''' ,(Name_Client ,Dob)).fetchall():
                return True
            else:
                return False
    except:
        print('some')

print(check_duplicate_entries2("Lim",'1966-05-09'))