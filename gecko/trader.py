from connection import Connection

class Trader:
    def __init__( self, aAPIKey, aPrivateKey ):
        self.fConnection = Connection( aAPIKey, aPrivateKey )
    
    def getAllOrders( self ):
        return self.fConnection.makeHTTPRequest( 'GET', '/v3/orders', 'status=all' )
