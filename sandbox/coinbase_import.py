import coinbasepro as cbp
client = cbp.PublicClient()

print(client.get_product_historic_rates('BTC-USD')[0])

API_KEY = 'cbfdc503eb028fcd2da3e1a4f5d20e5a'
API_SECRET = 'AsY/042KZF+a4Tfnlk/CnW4or7z7dQW/dwUoNrfMbCduQbtMpv2TL93xrRFlw+SQkWTXROs9KGA4wf1kG3zJ0Q=='
API_PASS = 'p6l4lisylh'


auth_client = cbp.AuthenticatedClient(key='cbfdc503eb028fcd2da3e1a4f5d20e5a',
                                          secret='AsY/042KZF+a4Tfnlk/CnW4or7z7dQW/dwUoNrfMbCduQbtMpv2TL93xrRFlw+SQkWTXROs9KGA4wf1kG3zJ0Q==',
                                          passphrase='p6l4lisylh')
accounts = auth_client.get_accounts()
total = 0

for account in accounts:
    print(f'{account["currency"]} : {account["balance"]}')

print(accounts)

print(client.get_product_ticker('ATOM-EUR'))