import bs4
import requests
from bs4 import BeautifulSoup

# url = "https://finance.yahoo.com/quote/{0}?p={0}".format(ticker)



r = requests.get('https://finance.yahoo.com/quote/FB?p=FB')
soup = bs4.BeautifulSoup(r.text, 'html.parser')
price = soup.find_all('div',{'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').get_text(strip=True)   # This also works


print(price)


