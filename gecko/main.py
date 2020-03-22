from trader import Trader

API_KEY = "c67aefb2-1894-4674-8c2b-3399ad612e07"
SECRET_KEY = "lVHKgk5pVbpLHeZxiBdtlp0wwq/L/uk+n4nmWXfZz1BSHQdmFT9xWST4Us297XeuxV7YPmTQh2ZT2m3r9aDxjA=="

Trader = Trader( API_KEY, SECRET_KEY )
print( Trader.getAllOrders() )
print( Trader.get_account_balance() )
print( Trader.get_BTC_ticketer() )