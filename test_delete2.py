import sqlite3
import pandas as pd

name_client = 'Olivia'
equity_name ='BD'
with sqlite3.connect(name_client + '.db') as db:
    try:
        sql_buy = f"select Number from Summary where (Equity_Name='{equity_name}' ) "
        dfbuy = pd.read_sql(sql_buy, db).sum()
        print(dfbuy[0],type(dfbuy[0]))

    except Exception as E:
        print(E)