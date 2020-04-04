from trader import Trader
from logger import Logger

API_KEY = ""
SECRET_KEY = ""

Trader = Trader( API_KEY, SECRET_KEY )
Logger = Logger()

last_XRP_price =  Trader.getLastPrice( "XRP-AUD")
invesment = 0.5
amount =  int ( invesment / float( last_XRP_price ) )

while( True ):
    lLastXRPPrice =  Trader.getLastPrice( "XRP-AUD")
    lAmount =  int ( invesment / float( lLastXRPPrice ) )
    lOrder = Trader.placeBasicLimitOrder( "XRP-AUD", str( lLastXRPPrice ), lAmount, "bid" )
    print( lOrder )
    if( lOrder['status'] != "Accepted" ):
        exit()

    print( "Order Placed " + "XRP-AUD. Amount = " + str(lAmount) + " Price = " + str(lLastXRPPrice) )
    Trader.waitForMatchedTrade( lOrder["orderId"] )

    print( "Order Matched" )
    
    lSellPrice = float( lLastXRPPrice ) * 1.0115
    print( lSellPrice )
    lSale = Trader.placeBasicLimitOrder( "XRP-AUD", str(lSellPrice)[0:5], lAmount, "ask" )
    print( lSale )
    if( lSale['status'] != "Accepted" ):
        exit()
    print( "Sale Placed " + "XRP-AUD. Amount = " + str(lAmount) + " Price = " + str(lSellPrice) )
    Trader.waitForMatchedTrade( lSale["orderId"] )
    print( "Sale Matched" )
    exit()