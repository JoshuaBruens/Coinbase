from coinbase_pro_feed.coinbase import CoinbaseConnection
from coinbase_pro_feed.fund_management import FundManagement
import pandas as pd
import datetime


def create_df(account_pnl):
    currency = [coin for coin in account_pnl]
    amount = [account_pnl[coin] for coin in account_pnl]
    date = [datetime.datetime.now() for _ in account_pnl]
    data = {
        'date': date,
        'coin': currency,
        'pnl' : amount
    }
    return pd.DataFrame(data=data)


def write_pnl_summary_to_csv(account_pnl):
    df_new = pd.concat([pd.read_csv('data/pnl_summary.csv'), create_df(account_pnl)])
    df_new.to_csv('data/pnl_summary.csv', index=False)


if __name__ == '__main__':
    print('Coinbase_Pro App running!!!')
    coinbase_pro_connection = CoinbaseConnection()
    fund_management = FundManagement()

    account_balance_coin_currency = coinbase_pro_connection.get_account_balance_currency()
    account_balance_eur = coinbase_pro_connection.get_account_balance_eur()
    account_balance_pnl = fund_management.get_pnl(account_balance_eur)
    account_balance_fess = fund_management.get_fees()

    print('Account summary in coin currency:')
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

    write_pnl_summary_to_csv(account_balance_pnl)
