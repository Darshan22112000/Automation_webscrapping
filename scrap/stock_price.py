import requests
from datetime import datetime
import time

def convert_date(date1):
    d = datetime.strptime(date1,'%Y/%m/%d')
    epoch = int(time.mktime(d.timetuple()))
    return epoch

ticker = input("Enter ticker(stock name): ")

from_date = input("enter start date in (yyyy/mm/dd) format: ")
from_date_converted = convert_date(from_date)
print(from_date_converted)

to_date = input("enter end date in (yyyy/mm/dd) format: ")
to_date_converted = convert_date(to_date)
print(to_date_converted)

url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_date_converted}&period2={to_date_converted}&interval=1d&events=history&includeAdjustedClose=true"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

content = requests.get(url,headers=headers).content

print(content)

with open ('data.csv','wb') as file:
    file.write(content)
    


