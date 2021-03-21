from coinbase_pro_feed.coinbase import CoinbaseConnection
from coinbase_pro_feed.fund_management import FundManagement

if __name__ == '__main__':
    print('Coinbase_Pro App running!!!')

    coinbase_pro_connection = CoinbaseConnection()
    fund_management = FundManagement()

    account_balance_coin_currency = coinbase_pro_connection.get_account_balance_currency()
    account_balance_eur = coinbase_pro_connection.get_account_balance_eur()
    account_balance_pnl = fund_management.get_pnl(account_balance_eur)
    account_balance_fess = fund_management.get_fees()

    print('Account summary in coin_currency:')
    for coin_currency in account_balance_coin_currency:
        print(f'{coin_currency} : {account_balance_coin_currency[coin_currency]}')

    print('Account summary in eur:')
    for coin_currency in account_balance_eur:
        print(f'{coin_currency} : {account_balance_eur[coin_currency]}')

    print('Account summary PnL:')
    for coin_currency in account_balance_pnl:
        print(f'{coin_currency} : {account_balance_pnl[coin_currency]}')

    print('Account summary fees:')
    for coin_currency in account_balance_fess:
        print(f'{coin_currency} : {account_balance_fess[coin_currency]}')