import sqlite3
from webscraping_1 import parsePrice, parsePriceSingle
import os
import random
import time
import pandas as pd
from datetime import date,datetime
import pandas_datareader as dr

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
        print(f"Table {table_name} Deleted Succesfully")

def create_table_Summary(name_client):
    with sqlite3.connect(f'{name_client}'+'.db') as db:
        try:
            db.execute(f'''CREATE TABLE IF NOT EXISTS Summary (ID INTEGER PRIMARY KEY AUTOINCREMENT,Equity_Name text, 
                 Current_Price float, Number float, Total_Cost float, Profit_Loss float)''')
        except Exception as E:
            print("Error: ",E)
        else:
            print('Table Summary Created Successfully..')

# insert_table_Summary(name_client, equity_name, currentPrice, number, total_cost, profit_loss)


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


if __name__ == '__main__':
    # Time1 = time.time()
    # delete_table_contents('Olivia','Summary')
    # create_table_Summary('Olivia')
    # compute_summary_from_database('Olivia')
    read_summary_from_database('Olivia')
    # print(time.time() - Time1)
    #select equity_name,current_price, number,total_cost,profit_loss, (select sum(Profit_Loss) from Summary) Gain from Summary