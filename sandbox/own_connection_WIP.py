# import json, hmac, hashlib, time, requests, base64
# from requests.auth import AuthBase
#
#
# # Create custom authentication for Exchange
# class CoinbaseExchangeAuth(AuthBase):
#     def __init__(self, api_key, secret_key, passphrase):
#         self.api_key = api_key
#         self.secret_key = secret_key
#         self.passphrase = passphrase
#
#     def __call__(self, request):
#         timestamp = str(time.time())
#         print(f'timestamp:{timestamp}')
#         message = timestamp + request.method + request.path_url + (request.body or '')
#         print(f'message:{message}')
#         message = 'hhhhhhhhh'
#         hmac_key = base64.b64decode(self.secret_key)
#         print(f'hmac_key:{hmac_key}')
#         print(f'type(hmac_key):{type(hmac_key)}')
#         signature = hmac.new(hmac_key, message.encode('utf-8'), hashlib.sha256)
#         print(f'signature:{signature}')
#         print(f'type(signature):{type(signature)}')
#         signature_b64 = signature.digest().encode('base64').rstrip('\n')
#
#         request.headers.update({
#             'CB-ACCESS-SIGN': signature_b64,
#             'CB-ACCESS-TIMESTAMP': timestamp,
#             'CB-ACCESS-KEY': self.api_key,
#             'CB-ACCESS-PASSPHRASE': self.passphrase,
#             'Content-Type': 'application/json'
#         })
#         return request
#
#
# #Website
# #https://public.sandbox.pro.coinbase.com
#
# #REST API
# #https://api-public.sandbox.pro.coinbase.com
#
# #Websocket Feed
# #wss://ws-feed-public.sandbox.pro.coinbase.com
#
# #FIX API
# #tcp+ssl://fix-public.sandbox.pro.coinbase.com:4198
#
# API_KEY = 'cbfdc503eb028fcd2da3e1a4f5d20e5a'
# API_SECRET = 'AsY/042KZF+a4Tfnlk/CnW4or7z7dQW/dwUoNrfMbCduQbtMpv2TL93xrRFlw+SQkWTXROs9KGA4wf1kG3zJ0Q=='
# API_PASS = 'p6l4lisylh'
#
# # api_url = 'https://api.pro.coinbase.com/'
# api_url = 'https://api-public.sandbox.pro.coinbase.com/'
# auth = CoinbaseExchangeAuth(API_KEY, API_SECRET, API_PASS)
#
# # Get accounts
# r = requests.get(api_url + 'accounts', auth=auth)
# print(r.json())
# # [{"id": "a1b2c3d4", "balance":...
#
# # Place an order
# #order = {
# #    'size': 1.0,
# #    'price': 1.0,
# #    'side': 'buy',
# #    'product_id': 'BTC-USD',
# #}
# #r = requests.post(api_url + 'orders', json=order, auth=auth)
# #print(r.json())
# # {"id": "0428b97b-bec1-429e-a94c-59992926778d"}
from datetime import datetime
import pandas as pd




deposits = [
    {'name': 'Bitcoin', 'currency': 'BTC', 'date': pd.to_datetime(datetime(2021, 2, 1)), 'deposit': 990.77, 'withdraw': 0, 'fee': 40.23},
    {'name': 'Bitcoin', 'currency': 'BTC', 'date': pd.to_datetime(datetime(2021, 3, 1)), 'deposit': 248.76, 'withdraw': 0, 'fee': 1.24},
    {'name': 'Ether', 'currency': 'ETH', 'date': pd.to_datetime(datetime(2021, 2, 1)), 'deposit': 1269.36, 'withdraw': 0, 'fee': 50.64},
    {'name': 'Ether', 'currency': 'ETH', 'date': pd.to_datetime(datetime(2021, 3, 1)), 'deposit': 248.79, 'withdraw': 0, 'fee': 1.21},
    {'name': 'DAI', 'currency': 'DAI', 'date': pd.to_datetime(datetime(2021, 2, 1)), 'deposit': 10.02, 'withdraw': 0, 'fee': 1.98},
    {'name': 'Litecoin', 'currency': 'LTC', 'date': pd.to_datetime(datetime(2021, 2, 1)), 'deposit': 96.16, 'withdraw': 0, 'fee': 3.84},
    {'name': 'Chainlink', 'currency': 'LINK', 'date': pd.to_datetime(datetime(2021, 2, 1)), 'deposit': 96.16, 'withdraw': 0, 'fee': 3.85},
    {'name': 'Bitcoin_Cash', 'currency': 'BCH', 'date':pd.to_datetime( datetime(2021, 2, 1)), 'deposit': 96.16, 'withdraw': 0, 'fee': 3.84},
    {'name': 'Stellar_Lumens', 'currency': 'XLM', 'date': pd.to_datetime(datetime(2021, 2, 1)), 'deposit': 96.16, 'withdraw': 0, 'fee': 3.84},
    {'name': 'The_Graph', 'currency': 'GRT', 'date': pd.to_datetime(datetime(2021, 2, 1)), 'deposit': 96.16, 'withdraw': 0, 'fee': 3.84},
    {'name': 'Uniswap', 'currency': 'UNI', 'date': pd.to_datetime(datetime(2021, 2, 1)), 'deposit': 96.16, 'withdraw': 0, 'fee': 3.84},
    {'name': 'Cosmos', 'currency': 'ATOM', 'date': pd.to_datetime(datetime(2021, 2, 1)), 'deposit': 96.16, 'withdraw': 0, 'fee': 3.84},
    {'name': 'Dash', 'currency': 'DASH', 'date': pd.to_datetime(datetime(2021, 2, 1)), 'deposit': 88.47, 'withdraw': 0, 'fee': 3.53},
    {'name': 'Cardano', 'currency': 'ADA', 'date': pd.to_datetime(datetime(2021, 3, 1)), 'deposit': 244.68, 'withdraw': 0, 'fee': 1.21}
]

name = []
currency = []
date = []
deposit = []
withdraw = []
fee = []
for loop in deposits:
    name.append(loop['name'])
    currency.append(loop['currency'])
    date.append(loop['date'])
    deposit.append(loop['deposit'])
    withdraw.append(loop['withdraw'])
    fee.append(loop['fee'])

data = {
    'name': name,
    'currency': currency,
    'date': date,
    'deposit': deposit,
    'withdraw': withdraw,
    'fee': fee,
}
df = pd.DataFrame(data=data)
df = df.sort_values(by=['date'])
df.to_csv('deposits.csv', index=False)