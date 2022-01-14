from requests import get
from bs4 import BeautifulSoup

# url = f"https://finance.yahoo.com/quote/{ticker}?p={ticker}"


def parsePrice(*ticker):
    for ticker in ticker:
        # print(i)

        r = get(f"https://finance.yahoo.com/quote/{ticker}?p={ticker}")
        soup = BeautifulSoup(r.text,"xml")
        # price = soup.find_all('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').get_text(strip=True)   # This also works
        price = soup.find_all('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
        print(f"Price of {ticker} is {price}")

        # return price

# while True:
#     print(str(parsePrice()))


Listshare = ['TCS.BO','TCS.NS','RELIANCE.BO','RELIANCE.NS','HDFCBANK.NS','HINDUNILVR.BO','HINDUNILVR.NS','HDFC.NS','HDFC.BO','INFY.NS','INFY.BO',
             'ITC.NS','ITC.BO','KOTAKBANK.NS','KOTAKBANK.BO','ICICIBANK.BO','ICICIBANK.NS','SBIN.NS','SBIN.BO','BAJFINANCE.NS','BAJFINANCE.BO','MARUTI.NS',
             'MARUTI.BO','LT.NS','LT.BO','AXISBANK.NS','AXISBANK.BO','BHARTIARTL.NS','BHARTIARTL.BO','ASIANPAINT.BO','ASIANPAINT.NS','ONGC.BO','ONGC.NS',
             'WIPRO.NS','WIPRO.BO','HCLTECH.BO','HCLTECH.NS','NTPC.NS','NTPC.BO','IOC.NS','IOC.BO']

a =(parsePrice(*Listshare))
#     print(next(parsePrice(*Listshare)))
