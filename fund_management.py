import pandas as pd


class FundManagement:
    def __init__(self):
        self.fund_management_df = pd.read_csv('data/deposits.csv')

    def get_pnl(self, account_balance_eur):
        df_funds = self.fund_management_df.groupby(['currency']).agg({'deposit': 'sum'}).reset_index()
        account_balance_pnl = {}
        for coin_currency in account_balance_eur:
            if (coin_currency != 'EUR') and (coin_currency != 'TOTAL'):
                try:
                    account_balance_pnl[coin_currency] = \
                        account_balance_eur[coin_currency] - df_funds[df_funds['currency'] == coin_currency]['deposit'].iloc[0]

                except Exception as err:
                    print(f'ERROR {err}')
                    print(f'Could not find {coin_currency} :(')
        account_balance_pnl['TOTAL'] = sum(account_balance_pnl.values())
        return account_balance_pnl

    def get_fees(self):
        df_funds = self.fund_management_df.groupby(['currency']).agg({'fee': 'sum'}).reset_index()
        account_balance_fee = {}
        for coin_currency in df_funds['currency']:
            account_balance_fee[coin_currency] = df_funds[df_funds['currency'] == coin_currency]['fee'].iloc[0]
        account_balance_fee['TOTAL'] = sum(account_balance_fee.values())
        return account_balance_fee
