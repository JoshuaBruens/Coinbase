from coinbase_pro_feed.coinbase import CoinbaseConnection

if __name__ == '__main__':
    print('Coinbase_Pro App running!!!')
    coinbase_pro_connection = CoinbaseConnection()
    account_balance_coin_currency = coinbase_pro_connection.get_account_balance_currency()
    print('Account summary in coin_currency:')
    for coin_currency in account_balance_coin_currency:
        print(f'{coin_currency} : {account_balance_coin_currency[coin_currency]}')

    account_balance_eur = coinbase_pro_connection.get_account_balance_eur()
    print('Account summary in eur:')
    for coin_currency in account_balance_eur:
        print(f'{coin_currency} : {account_balance_eur[coin_currency]}')




