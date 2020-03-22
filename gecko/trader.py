from connection import Connection

class Trader:
    def __init__( self, aAPIKey, aPrivateKey ):
        self.Connection = Connection( aAPIKey, aPrivateKey )
    
    def getAllOrders( self ):
        return self.Connection.makeHTTPRequest( 'GET', '/v3/orders', 'status=all' )

    def get_account_balance(self):
        return self.Connection.makeHTTPRequest('GET', '/v3/accounts/me/balances', 'status=all')

    def get_orders(self):
        return self.Connection.makeHTTPRequest('GET',  '/v3/orders', 'status=all')

    def get_markets(self):
        return self.Connection.makeHTTPRequest('GET',  '/v3/markets', 'status=all')

    def get_BTC_ticketer(self):
        return self.Connection.makeHTTPRequest('GET',  '/v3/markets/BTC-AUD/ticker', 'status=all')
