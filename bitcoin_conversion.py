import requests
from pprint import pprint

response1 = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')


def main():
    currency_type = get_conversion_type()
    amount = get_dollar_amount(currency_type)
    exchange_rate = get_conversion_data(currency_type)
    print_converted_amount(amount, exchange_rate)


def get_conversion_type():
    currency_type = input('Enter the 3 letter currency abbreviation: ').upper()
    return currency_type


def get_dollar_amount(currency_type):
    return float(input(f'Enter amount of {currency_type} to convert to BTC: '))


def get_conversion_data(currency_type):
    data = response1.json()
    pprint(data)
    exchange_rate = data['bpi'][currency_type]['rate_float']
    return exchange_rate


def print_converted_amount(amount, exchange_rate):
    print(f'The amount of BTC you have are worth: ${amount * exchange_rate}')


if __name__ == '__main__':
    main()
