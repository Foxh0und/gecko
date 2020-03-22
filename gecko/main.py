from trader import Trader

API_KEY = ""
SECRET_KEY = ""

Trader = Trader( API_KEY, SECRET_KEY )
print( Trader.getAllOrders() )
print( Trader.get_account_balance() )
print( Trader.get_BTC_ticketer() )