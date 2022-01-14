import sqlite3
import os
import datetime
def check_if_database_exists(client_name):
    if (client_name in os.listdir()):
        return True
    else:
        return False
def check_table_exists(db_connect_object):
    pass

def create_database_object(client_name):
    conn = sqlite3.connect(f'{client_name.capitalize()}')
    cursor = conn.cursor()
    return conn, cursor

def create_table(cursor):
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS Shares (Tradedate varchar(20) , Equity_Name int, Price_Current 
    float, Cost float, Number float, Gain_Loss float, Value float, Percentage_Change float)''')

def data_entry(cursor,conn):
    date = datetime.datetime.now().date().isoformat()


    print(date)
    cursor.execute(f'''INSERT INTO Shares VALUES ({date}, 'TCS', 225, 
       200, 10, 50, 2250, 1 )  ''')
    conn.commit()
    cursor.close()
    conn.close()

def dynamic_insert_into_table(db, table_name_client_name,dataset):
        cursor = db.cursor()
        sql_command = f''' insert into {table_name_client_name} 
        (Tradedate, Number_of_shares_credit, Number_of_shares_debit,
            price , Total_no_shares) values (:Tradedate, :Number_of_shares_credit, :Number_of_shares_debit,
            :price , :Total_no_shares) '''
        cursor.executemany(sql_command,dataset)

def select_data(db,table_name_companyname,query):
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()
def create_overview_table(db_connect_object,person_name):
    cursor = db_connect_object.cursor()
    sql_command = f'''create temporary table {person_name} 
           (Tradedate date, company_name float null,
           price_per_share float, Total_no_shares float not null, position)
               '''

conn,cursor = create_database_object("Krishna")
create_table(cursor)
data_entry(cursor,conn)
# close_connection(conn,cursor)

