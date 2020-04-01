from trader import Trader

API_KEY = "0518eb10-4c30-42ea-b35c-3e460b92bb16"
SECRET_KEY = "0PdlKrG+Pmyb31J/UfLfysOIxtkRys2zoCceDaCeGj8Rk3cD+zTFZ4Q2yazfsyQRqQ3fdl7yBU+RJDJSXwWE6Q=="

Trader = Trader( API_KEY, SECRET_KEY )

while( True ):
    lLastXRPPrice =  Trader.getLastPrice( "XRP-AUD")
    lAmount =  int ( 4 / float( lLastXRPPrice ) )
    lOrder = Trader.placeBacicLimitOrder( "XRP-AUD", str( lLastXRPPrice ), lAmount, "bid" )
    print( lOrder )
    if( lOrder['status'] != "Accepted" ):
        exit()

    print( "Order Placed " + "XRP-AUD. Amount = " + str(lAmount) + " Price = " + str(lLastXRPPrice) )
    Trader.waitForMatchedTrade( lOrder["orderId"] )

    print( "Order Matched" )
    
    lSellPrice = float( lLastXRPPrice ) * 1.0115
    print( lSellPrice )
    lSale = Trader.placeBacicLimitOrder( "XRP-AUD", str(lSellPrice)[0:5], lAmount, "ask" )
    print( lSale )
    if( lSale['status'] != "Accepted" ):
        exit()
    print( "Sale Placed " + "XRP-AUD. Amount = " + str(lAmount) + " Price = " + str(lSellPrice) )
    Trader.waitForMatchedTrade( lSale["orderId"] )
    print( "Sale Matched" )
    exit()

