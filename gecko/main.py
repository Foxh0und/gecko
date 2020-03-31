from trader import Trader

API_KEY = ""
SECRET_KEY = ""

Trader = Trader( API_KEY, SECRET_KEY )
#print( Trader.getAllOrders() )
#print( Trader.get_account_balance() )
# print( Trader.placeOrder("XRP-AUD", 20,5,"Limit","Bid") );

lLastXRPPrice =  Trader.getLastPrice( "XRP-AUD")
lAmount = float( lLastXRPPrice ) % 2 
print( lLastXRPPrice )
print( lAmount )
#lOrder = Trader.placeBacicLimitOrder( "XRP-AUD", str( lLastXRPPrice ), lAmount, "bid" )
#print( lOrder )
print( Trader.getOrderStatus( '5727608782' ) )





