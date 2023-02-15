import requests
from bs4 import BeautifulSoup
import json

# read stock data from json file
STOCK_FILE_PATH = 'stock.json'
with open(STOCK_FILE_PATH, 'r') as f:
    stock_data_raw = f.read()
    stock_data = json.loads(stock_data_raw)

def get_stock_gains(**kwargs):
    URL = f"""https://www.buyupside.com/alphavantagelive/dollarcostavecomputeav.php?symbol=\
{kwargs['stock_symbol']}\
&amountinitial=\
{kwargs['initial_amount']}\
&amount=\
{kwargs['monthly_amount']}\
&start_month=\
{kwargs['start_month']}\
&start_year=\
{kwargs['start_year']}\
&end_month=\
{kwargs['end_month']}\
&end_year=\
{kwargs['end_year']}\
&submit=Calculate+Returns"""

    r = requests.get(URL)

    soup = BeautifulSoup(r.content, 'html5lib')

    # find table rows
    main = soup.find('div', attrs = {'class':'main'}) 
    rows = main.findAll('tr')

    # retrieve values from table
    invested_raw = rows[6].findAll('td')[1].text
    total_raw = rows[9].findAll('td')[1].text

    # clean values from redundant chars
    invested = float(invested_raw.replace('$', '').replace(',', ''))
    total = float(total_raw.replace('$', '').replace(',', ''))

    gains = total - invested

    return {
        'stock_name': kwargs['stock_name'],
        'stock_symbol': kwargs['stock_symbol'],
        'invested': invested,
        'total': total,
        'gains': gains,
    }

stocks = []
for stock in stock_data['stocks']:
    stock_gains = get_stock_gains(
        stock_name=stock['name'],
        stock_symbol=stock['symbol'],

        initial_amount=stock_data.get('initial_amount', 0) * stock['percentage'] / 100.0,
        monthly_amount=stock_data['monthly_amount'] * stock['percentage'] / 100.0,

        start_month=stock_data['start_month'],
        start_year=stock_data['start_year'],

        end_month=stock_data['end_month'],
        end_year=stock_data['end_year'],
    )
    stocks.append(stock_gains)

    print(stock_gains)

total = sum([stock['total'] for stock in stocks])
invested = sum([stock['invested'] for stock in stocks])
gains = sum([stock['gains'] for stock in stocks])
gains_after_tax = gains * (100.0 - stock_data['tax_percentage']) / 100.0

print(f'Total portfolio worth:{total:.2f}')
print(f'Total invested:{invested:.2f}')
print(f'Total gains:{gains:.2f}')
print(f'Total gains(after tax, if sold):{gains_after_tax:.2f}')
