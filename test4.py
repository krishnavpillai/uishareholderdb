import sqlite3
import pandas as pd
numbers = 10

with sqlite3.connect('Liam.db') as db:
    print(1)
    try:
        sql_buy = f"select Number from Transactions where (Equity_Name='DD' and Type='Buy' and Date<'2000-05-20' ) "
        print(2)
        dfbuy = pd.read_sql(sql_buy, db).sum()
        dfbuy = dfbuy[0]
        print(dfbuy)
        # print((dfbuy.sum()[0]))
        # print(3)
    except Exception as E:
        print(4)
        print(f'DD has no Buy {E} ')
        print(5)

    else:
        print(6)


    print(7)
    try:
        sql_sell = f"select Number from Transactions where (Equity_Name='DD' and Type='Sell' and Dob<'2000-05-20' ) "
        dfsell = pd.read_sql(sql_sell, db).sum()
        dfsell = dfsell[0]
        print(8)
    except:
        dfsell = 0
        print(9)
    print(dfbuy,dfsell,numbers)

