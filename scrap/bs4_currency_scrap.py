from bs4 import BeautifulSoup
import requests

def get_currency(in_currency,out_currency,amt):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount={amt}'
    content = requests.get(url).text
    soup = BeautifulSoup(content,'html.parser')
    currency = soup.find("span", class_="ccOutputRslt").get_text()
    currency = float(currency[:-4])
    return currency
    
result = get_currency('USD','INR',10)
print(result)    