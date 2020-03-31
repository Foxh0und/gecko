from connection import Connection
import json

class Trader:
    def __init__( self, aAPIKey, aPrivateKey ):
        self.Connection = Connection( aAPIKey, aPrivateKey )
    
    def getAllOrders( self ):
        return self.Connection.makeHTTPRequest( 'GET', '/v3/orders', 'status=all' )

    def get_account_balance(self):
        return self.Connection.makeHTTPRequest('GET', '/v3/accounts/me/balances', 'status=all')

    def get_orders( self):
        return self.Connection.makeHTTPRequest('GET',  '/v3/orders', 'status=all')

    def get_markets(self):
        return self.Connection.makeHTTPRequest('GET',  '/v3/markets', 'status=all')

    def getLastPrice( self, aMarketID ):
        lResponse = self.Connection.makeHTTPRequest( 'GET', '/v3/markets/' + aMarketID + "/ticker", None )
        return lResponse["lastPrice"]

    def get_BTC_ticketer(self):
        return self.Connection.makeHTTPRequest('GET',  '/v3/markets/XRP-AUD/ticker', 'status=all')

    def placeBacicLimitOrder(self, aMarketID, aPrice, aAmount, aSide ):
        lData = dict(
            marketId = aMarketID,
            price = aPrice,
            amount = aAmount,
            type = "Limit",
            side = aSide
        )
        return self.Connection.makeHTTPRequest( 'POST', '/v3/orders', "", lData )

    def getOrderStatus( self, aOrderID ):
        lResponse = self.Connection.makeHTTPRequest( 'GET', '/v3/orders/' + aOrderID, "" )
        return lResponse["status"]
