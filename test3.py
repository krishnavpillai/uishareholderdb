import random
from database_share_transactions import random_date
import pandas_datareader as dr

Equity_List = ['IBM', 'PG', 'KO', 'AGN', 'CI', 'DD', 'JNJ', 'BID', 'PFE', 'ED', 'BK', 'CL', 'JWA']
equity_name = random.choice(Equity_List)
date_rand = random_date()


def priceDatareaderDate(equity_name, date_rand):
        pan = dr.get_data_yahoo([equity_name]).Close.loc[date_rand]
        pan = round(pan[0], 2)
        if pan:
            print(pan)

#
# for i in range(20):
#     equity_name = random.choice(Equity_List)
#     date_rand = random_date()
#     print(equity_name,date_rand, end=' ')
#     try:
#         priceDatareaderDate(equity_name,date_rand)
#     except:
#         continue
print(random_date())