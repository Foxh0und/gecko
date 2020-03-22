from trader import Trader

API_KEY = ""
SECRET_KEY = ""

lTrader = Trader( API_KEY, SECRET_KEY )
print( lTrader.getAllOrders() )