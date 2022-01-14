import pandas as pd
import sqlite3
import os
from os import path


def read_Transaction(Name_Client ):
    name_client = Name_Client
    if name_client in os.listdir():
        try:
            with sqlite3.connect(name_client) as db:
                df = pd.read_sql(f'SELECT * FROM Transactions', db)
                print(df)
        except Exception as E:
            print("Error: ",E)
        else:
            print('Table Created Successfully..')
    else:
        print("Table does not exist.")



read_Transaction('Olivia.db')

