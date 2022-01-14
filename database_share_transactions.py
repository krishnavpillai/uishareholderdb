import sqlite3
from webscraping_1 import parsePrice, parsePriceSingle,priceDatareaderDate
import os
import random
import time
import pandas as pd
from datetime import date,datetime
import pandas_datareader as dr

def delete_database(name_client):
    try:
        os.remove(name_client)
        print(f'file removed {name_client}')
    except:
        print(f'file {name_client} does not exist.')

def delete_table_contents(name_Client,table_name):
    Name_Client =name_Client
    try:
        with sqlite3.connect(Name_Client+'.db') as db:
            cursor = db.cursor()
            cursor.execute(f"DROP TABLE IF EXISTS {table_name} ")
    except Exception as E:
        print("Error: ",E)
    else:
        db.commit()
        print("Table Transactions Deleted Succesfully")

def create_table_transaction(name_client):
    Name_Client = name_client
    if Name_Client not in os.listdir():
        try:
            with sqlite3.connect(Name_Client+'.db') as db:
                db.execute('''CREATE TABLE IF NOT EXISTS Transactions ( ID INTEGER PRIMARY KEY AUTOINCREMENT,Equity_Name text,Date text, 
                Type text, Cost float, Number int, Total float)''')
        except Exception as E:
            print("Error: ",E)
        else:
            print('Table Created Successfully..')
    else:
        print(f"Table already exists {Name_Client}"+'.db')

def create_table_Summary(name_client):
    with sqlite3.connect(f'{name_client}'+'.db') as db:
        try:
            db.execute(f'''CREATE TABLE IF NOT EXISTS Summary (ID INTEGER PRIMARY KEY AUTOINCREMENT,Equity_Name text, 
                 Current_Price float, Number float, Total_Cost float, Profit_Loss float)''')
        except Exception as E:
            print("Error: ",E)
        else:
            print('Table Summary Created Successfully..')

def insert_table_Summary(name_client,equity_name,current_price,number,total_cost,profit_loss):
    try:
        with sqlite3.connect(name_client+'.db') as db:
            cursor = db.cursor()
            cursor.execute('''INSERT INTO Summary (Equity_Name, 
                 Current_Price, Number, Total_Cost, Profit_Loss) VALUES (?,?,?,?,?) ''',(equity_name,current_price,
                                                                          number,total_cost,profit_loss))
    except Exception as E:
        print(f'Entry into Summary Table of {name_client} failed due to {E}')
    else:
        db.commit()
        print(f"Data inserted successfully into Summary of {name_client} ")

def insert_table_transaction(name_Client, equity_name,Date, type_trans, Cost, Numbers, Total):
    Name_Client = name_Client
    try:
        with sqlite3.connect(Name_Client+'.db') as db:
            cursor = db.cursor()
            cursor.execute(f'''INSERT INTO Transactions (Equity_Name ,Date , 
                Type , Cost , Number , Total ) VALUES (?,?,?,?,?,?) ''',(equity_name,Date,
                                                 type_trans, Cost, Numbers, Total))
    except Exception as E:
        print("Error",E)
    else:
        db.commit()
        print("Data inserted Successfully...")

def check_sell_buy_no_balance(name_client,equity_name,date_sample,numbers):
    '''Returns true if no balance. ie number > buy -sell'''
    Name_Client = name_client
    with sqlite3.connect(Name_Client+'.db') as db:
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
        print(dfbuy,dfsell,numbers)
        print((numbers > dfbuy-dfsell))
        return (numbers > dfbuy-dfsell)

def random_date():
    start_dt = date.today().replace(day=1, month=1, year=1990).toordinal()
    end_dt = date.today().toordinal()
    random_day = date.fromordinal(random.randint(start_dt, end_dt))
    return random_day.strftime('%Y')

def equity_cost_random_date(equity, dates):
    cost_equtiy_random_date = dr.get_data_yahoo([equity]).Close.loc[dates]
    return cost_equtiy_random_date

def show_transctions_table_from_database(name_client):
    try:
        with sqlite3.connect(name_client+'.db') as db:
            cursor = db.cursor()
            cursor.execute(f'SELECT * FROM Transactions')
            for row in cursor.fetchall():
                print(row)
    except Exception as E:
        print(f"Could not connect or no {name_client}")

def compute_summary_from_database(name_client):
    with sqlite3.connect(name_client+'.db') as db:
        try:
            # print(pd.read_sql('select * from Transactions', db).head())
            sql_select = f"select Equity_Name from Transactions "
            allEquityClient = pd.read_sql(sql_select, db)
            allEquityClientList = allEquityClient['Equity_Name'].tolist()
            allEquityClientList = set(allEquityClientList)
            allEquityClientList = list(allEquityClientList)
            allEquityClientList.sort()
            print(allEquityClientList)
            for equity_name in allEquityClientList[:10]:
                print(f'In for loop {equity_name}')
                try:
                    # equity_name = 'TCS.NS'
                    #equity_name, current_price, number, total_Cost, profit_loss
                    currentPrice = parsePriceSingle(equity_name)
                    print(1 , currentPrice,'currentprice')
                    sqlClientEquityBuy = f"SELECT Number from Transactions WHERE (Equity_Name='{equity_name}' AND Type='Buy') "
                    equityBought = pd.read_sql(sqlClientEquityBuy, db).sum()
                    print(2,equityBought,'equitybought')
                    sqlClientEquitySell = f"SELECT Number from Transactions WHERE (Equity_Name='{equity_name}' AND Type='Sell') "
                    equitySold = pd.read_sql(sqlClientEquitySell, db).sum()
                    print(22,equitySold,'equitysold')
                    number = (equityBought - equitySold)
                    number =  number.astype('float64')
                    print(3,number[0],type(number[0]),number,type(number))
                    sqlClientEquityBuyTotal = f"SELECT Total from Transactions WHERE (Equity_Name='{equity_name}' AND Type='Buy') "
                    EquityBuyTotal = pd.read_sql(sqlClientEquityBuyTotal, db).sum()
                    print(4,EquityBuyTotal[0],'eautiybuytotal')
                    sqlClientEquitySellTotal = f"SELECT Total from Transactions WHERE (Equity_Name='{equity_name}' AND Type='Sell') "
                    EquitySellTotal = pd.read_sql(sqlClientEquitySellTotal, db).sum()
                    print(5,EquitySellTotal,'equity soldtotal')
                    total_cost = round(EquityBuyTotal - EquitySellTotal,2)
                    print(6,total_cost[0],'totalcost')
                    profit_loss = round(number[0]*currentPrice - total_cost[0],2)
                    print(9,profit_loss,'profitloss')
                    insert_table_Summary(name_client,equity_name,currentPrice,number[0],total_cost[0],profit_loss)
                except Exception as E:
                    print(f"Insertion into summary table of {equity_name} failed due to {E}")
        except Exception as E:
            print(f"The database {name_client} has error {E}")
        # print(pd.read_sql('select * from Summary', db))


def read_summary_from_database(name_client):
    with sqlite3.connect(name_client+'.db') as db:
        print(pd.read_sql("Select * from Summary union select  ' ', ' ', ' ',' ', sum(Total_Cost), sum(Profit_Loss) from Summary", db))


def computeHistorical():
    # name_Client, equity_name, Date, type_trans, Cost, Numbers, Total
    name_client = random.choice(Name_Client)

    equity_name = random.choice(Equity_List)
    date_rand = random_date()
    type_trans = random.choice(Type_Trans)
    # type_trans = 'Sell'
    numbers = random.randint(2, 10)
    cost,date_sample = priceDatareaderDate(equity_name, date_rand)
    print(name_client, equity_name, date_sample, type_trans, cost, numbers)

    if not cost:
        return False
    if type_trans == 'Sell':
        if check_sell_buy_no_balance(name_client, equity_name, date_sample, numbers):
            print('ok')
            return False
    total = round(cost*numbers,2)
    return name_client, equity_name, date_sample, type_trans, cost, numbers, total

def main():
    Time1 = Time2 = time.time()
    for i in range(1):
        print(str(i).center(50,'-'))
        try:
           name_client, equity_name, date_rand, type_trans, cost, numbers, total = computeHistorical()
           # print(name_client, equity_name, date_rand, type_trans, cost, numbers, total)
        except Exception as E:
            print(11,E)
            continue
        if i%5 == 0:
            print('Time',time.time() - Time2)
            Time2 = time.time()
        # print((name_Client))
        # name_Client = 'Olivia'
        # equity_name = 'TCS.BO'
        # type_trans = 'Sell'
        # Date = datetime.now().date()
        create_table_transaction(name_client)
        insert_table_transaction(name_client, equity_name,date_rand, type_trans,cost, numbers,total)
    print(Time1 - time.time())
    print("Completed Cycle")
    # create_table_Summary(name_Client)
    # insert_table_Summary()

if __name__ == '__main__':
    # Equity_List = ['TCS.BO', 'TCS.NS', 'RELIANCE.BO', 'RELIANCE.NS', 'HDFCBANK.NS', 'HINDUNILVR.BO', 'HINDUNILVR.NS',
    #                'HDFC.NS', 'HDFC.BO', 'INFY.NS', 'INFY.BO', 'ITC.NS', 'ITC.BO', 'KOTAKBANK.NS', 'KOTAKBANK.BO',
    #                'ICICIBANK.BO', 'ICICIBANK.NS', 'SBIN.NS', 'SBIN.BO', 'BAJFINANCE.NS', 'BAJFINANCE.BO', 'MARUTI.NS',
    #                'MARUTI.BO', 'LT.NS', 'LT.BO',
    #                'AXISBANK.NS', 'AXISBANK.BO', 'BHARTIARTL.NS', 'BHARTIARTL.BO', 'ASIANPAINT.BO', 'ASIANPAINT.NS',
    #                'ONGC.BO', 'ONGC.NS', 'WIPRO.NS',
    #                'WIPRO.BO', 'HCLTECH.BO', 'HCLTECH.NS', 'NTPC.NS', 'NTPC.BO', 'IOC.NS', 'IOC.BO']
    # Name_Client = ['Liam', 'Noah', 'William', 'James', 'Logan', 'Benjamin', 'Mason', 'Elijah', 'Oliver', 'Jacob',
    #     #                'Emma', 'Olivia', 'Ava','Isabella', 'Sophia', 'Mia', 'Charlotte', 'Amelia', 'Evelyn', 'Abigail']
    Equity_List = ['IBM',  'PG', 'KO', 'AGN', 'CI', 'DD', 'JNJ', 'BID', 'PFE', 'ED', 'BK', 'CL']
    Name_Client = ['Liam','Olivia']
    Type_Trans = ['Buy', 'Sell']
    main()
