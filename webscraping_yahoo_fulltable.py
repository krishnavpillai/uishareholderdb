import bs4 as bs
import urllib.request
import pandas as pd


def get_ticker(ticker):
    url = 'https://finance.yahoo.com/quote/' + ticker + '/history?p=' + ticker
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source, 'lxml')
    tr = soup.find_all('tr')

    data = []

    for table in tr:
        td = table.find_all('td')
        row = [i.text for i in td]
        data.append(row)

    columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    data = data[1:-2]
    # print(data)
    df = pd.DataFrame(data)
    df.columns = columns
    df.set_index(columns[0], inplace=True)
    # df = df.convert_objects(convert_numeric=True)
    df = df.iloc[::-1]
    print(df)
    # df.dropna(inplace=True)

    # return df
ticker = 'AAPL'
print(get_ticker(ticker))