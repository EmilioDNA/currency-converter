# write your code here!
import requests
import json


def calculate_exchange(amt, target, arr_cache):
    for c in arr_cache:
        code = c['code']
        if code == target.upper():
            print(f'You received {round(c["rate"] * amt, 2)} {c["code"]}.')


def calculate_exchange_dict(amt, target, obj_request):
    for c in obj_request.keys():
        if c == target.lower():
            print(f'You received {round(obj_request[c]["rate"] * amt, 2)} {obj_request[c]["code"]}.')


def request_exchange():
    exchange_code = input()
    amount = float(input())
    return exchange_code, amount


def make_exchange_request(currency_c):
    r = requests.get(f"http://www.floatrates.com/daily/${currency_c}.json")
    currency_dict = json.loads(r.text)
    return currency_dict


def check_cache(arr_cache, target):
    for curr in arr_cache:
        code = curr['code']
        if code == target.upper():
            return True
    return False


def save_cache(arr_cache, currency_dict, currency_c):
    try:
        arr_cache.append(currency_dict[currency_c])
    except:
        pass


arr_currency_cache = []
currency_code = input()
currency = make_exchange_request(currency_code)
save_cache(arr_currency_cache, currency, "usd")
save_cache(arr_currency_cache, currency, "eur")

while True:
    exchange_code = str(input())
    if exchange_code != '':
        amount = float(input())
        print('Checking the cache...')
        if check_cache(arr_currency_cache, exchange_code):
            print('Oh! It is in the cache!')
            calculate_exchange(amount, exchange_code, arr_currency_cache)
        else:
            print("Sorry, but it is not in the cache!")
            currency = make_exchange_request(currency_code)
            calculate_exchange_dict(amount, exchange_code, currency)
            save_cache(arr_currency_cache, currency, exchange_code.lower())
    else:
        break
