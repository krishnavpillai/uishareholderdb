from requests import get
from bs4 import BeautifulSoup
# import pandas_datareader as dr

def parsePrice(*ticker):
    for ticker in ticker:
        # print(i)

        r = get(f"https://finance.yahoo.com/quote/{ticker}?p={ticker}")
        soup = BeautifulSoup(r.text,"html5lib")
        try:
            Cost = soup.find_all('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
        except:
            Cost = soup.find_all('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text

        Cost = float(Cost.replace(',',''))


        yield Cost

def parsePriceSingle(ticker):


    r = get(f"https://finance.yahoo.com/quote/{ticker}?p={ticker}")
    soup = BeautifulSoup(r.text,"html5lib")
    Cost = soup.find_all('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text

    Cost = float(Cost.replace(',', ''))
    return Cost

def priceDatareaderDate(equity, date):
    try:
        print(equity,date)
        df = dr.data.get_data_yahoo(equity,start='1990-09-27',end='2019-09-22')
        df = df.loc[date, ['Open']]
        df = df.sample()
        print(df)
        price = round(df['Open'][0],2)
        print(price)
        date_sample = df.index[0].strftime('%Y-%m-%d')

        return price,date_sample
    except Exception as E:
        print("pricedatareaderdate",E)
        return False



if __name__ == '__main__':
    Listshare = ['TCS.BO','TCS.NS','RELIANCE.BO','RELIANCE.NS','HDFCBANK.NS','HINDUNILVR.BO','HINDUNILVR.NS','HDFC.NS','HDFC.BO','INFY.NS','INFY.BO',
             'ITC.NS','ITC.BO','KOTAKBANK.NS','KOTAKBANK.BO','ICICIBANK.BO','ICICIBANK.NS','SBIN.NS','SBIN.BO','BAJFINANCE.NS','BAJFINANCE.BO','MARUTI.NS',
             'MARUTI.BO','LT.NS','LT.BO','AXISBANK.NS','AXISBANK.BO','BHARTIARTL.NS','BHARTIARTL.BO','ASIANPAINT.BO','ASIANPAINT.NS','ONGC.BO','ONGC.NS',
             'WIPRO.NS','WIPRO.BO','HCLTECH.BO','HCLTECH.NS','NTPC.NS','NTPC.BO','IOC.NS','IOC.BO']
    # a =(parsePrice(*Listshare))
    # for items in Listshare:
    #     print(list((parsePrice(items))))

    print(parsePriceSingle('IBM'))
# a,b = (priceDatareaderDate('AAPL','2005'))
# print(type(a))
# print(type(b))
# if a:
#     print(5)
