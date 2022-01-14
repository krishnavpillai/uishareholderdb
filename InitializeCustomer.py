import datetime
import sqlite3
from webscraping_1 import parsePrice
class Sharemarket:

    def __init__(self, name):
        self.name = name
        self.date_of_creation_account = datetime.datetime.now().date()
        self.shares = []



    # def StartingInvestment(self, startinginvestment):
    #     self.startingInvestment = startinginvestment
    #
    # def AddInvestment(self, addmoney):
    #     self.startingInvestment = self.startingInvestment + addmoney

    # def RemoveInvestment(self, removemoney):
    #     if removemoney < self.startingInvestment:
    #         self.startingInvestment = self.startingInvestment - removemoney
    #     else:
    #         print(f'Maximum amount deductable is {self.startingInvestment}')




    # def buy_shares(self,company,buying_price, numbers):
    #     # TODO enter price of share corresponding to company
    #
    # def sell_shares(self,company,price_share,numbers):
    #     pass


    def position(self):
        pass



#
# krishna = sharemarket('krishna')
# krishna.StartingInvestment(50000)
# print(krishna.startingInvestment)
# krishna.AddInvestment(100000)
# print(krishna.startingInvestment)
# krishna.RemoveInvestment(25000)
# print(krishna.startingInvestment)
# krishna.buy_shares('TCS',250,150)
# print(krishna.startingInvestment)
# print(krishna.shares)
# krishna.sell_shares('TCS',250,50)
# print(krishna.startingInvestment)
# print(krishna.shares)

