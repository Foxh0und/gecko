from connection import Connection
import json
import time

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

    def getLastPrice( self, aMarketID ):
        lResponse = self.Connection.makeHTTPRequest( 'GET', '/v3/markets/' + aMarketID + "/ticker", None )
        return lResponse["lastPrice"]

    def get_BTC_ticketer(self):
        return self.Connection.makeHTTPRequest('GET',  '/v3/markets/XRP-AUD/ticker', 'status=all')

    def placeBasicLimitOrder(self, aMarketID, aPrice, aAmount, aSide ):
        lData = dict(
            marketId = aMarketID,
            price = aPrice,
            amount = aAmount,
            type = "Limit",
            side = aSide
        )
        return self.Connection.makeHTTPRequest( 'POST', '/v3/orders', "", lData )

    #Does not work for XRP
    def place_take_profit_order(self, market_id, price, amount):

        trigger_price = float(price) * 1.1

        data = dict(
            marketId = market_id,
            price = price, 
            amount = amount,
            type = "Take Profit",
            side = "ask", 
            triggerPrice = str(trigger_price)
        )
        return self.Connection.makeHTTPRequest( 'POST', '/v3/orders', "", data )

    def place_stop_loss_order(self, market_id, price, amount):

        trigger_price = float(price) * 0.9885

        data = dict(
            marketId = market_id,
            price = price, 
            amount = amount,
            type = "Stop Loss",
            side = "bid", 
            triggerPrice = str(trigger_price)
        )
        return self.Connection.makeHTTPRequest( 'POST', '/v3/orders', "", data )

    def getOrderStatus( self, aOrderID ):
        lResponse = self.Connection.makeHTTPRequest( 'GET', '/v3/orders/' + aOrderID, "" )
        return lResponse["status"]

    # TODO: Add Timeout
    def waitForMatchedTrade( self, aOrderID ):
        while( True ):
            lStatus = self.getOrderStatus( aOrderID )
            if( lStatus == "Fully Matched"):
                return
            else:
                time.sleep(20)
