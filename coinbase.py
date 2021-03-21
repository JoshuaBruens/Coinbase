import coinbasepro as cbp
from coinbasepro.exceptions import CoinbaseAPIError

from coinbase_pro_feed.api_keys import API_KEY, API_SECRET, API_PASS

BTC = 'BTC'
EUR = 'EUR'
DAI = 'DAI'


class CoinbaseConnection:
    def __init__(self):
        self.public_connection = cbp.PublicClient()
        self.personal_connection = cbp.AuthenticatedClient(
            key=API_KEY,
            secret=API_SECRET,
            passphrase=API_PASS
        )
        btc_eur = self.public_connection.get_product_ticker('BTC-EUR')
        self.__BTC_EUR = float(btc_eur['price'])
        eth_eur = self.public_connection.get_product_ticker('ETH-EUR')
        self.__ETH_EUR = float(eth_eur['price'])

    def get_account_balance_currency(self):
        account_balance = self.personal_connection.get_accounts()
        account_balance_currency = {account['currency']: float(account['balance'])
                                    for account in account_balance if float(account['balance']) > 0.0 }
        return account_balance_currency

    def get_account_balance_eur(self):
        account_balance_currency = self.get_account_balance_currency()
        account_balance_eur = {}
        for coin_currency in account_balance_currency:
            try:
                if coin_currency == BTC:
                    spot_price = self.__BTC_EUR
                    account_balance_eur[coin_currency] = account_balance_currency[coin_currency] * spot_price
                elif coin_currency == EUR:
                    account_balance_eur[coin_currency] = account_balance_currency[coin_currency]
                elif coin_currency == DAI:
                    spot = self.public_connection.get_product_ticker('ETH-DAI')
                    spot_price = (1 / float(spot['price'])) * self.__ETH_EUR
                    account_balance_eur[coin_currency] = account_balance_currency[coin_currency] * spot_price
                else:
                    spot = self.public_connection.get_product_ticker(coin_currency+'-BTC')
                    spot_price = float(spot['price']) * self.__BTC_EUR
                    account_balance_eur[coin_currency] = account_balance_currency[coin_currency] * spot_price
            except CoinbaseAPIError:
                print(f'Could not find balance for {coin_currency + "-BTC"} or !')
        account_balance_eur['TOTAL'] = sum(account_balance_eur.values())
        return account_balance_eur
