# package import statement
from smartapi import SmartConnect #or from smartapi.smartConnect import SmartConnect
#import smartapi.smartExceptions(for smartExceptions)

#create object of call
obj=SmartConnect(api_key="lMlAb4Mi")

#login api call

data = obj.generateSession("A1128018","Athuashu12#")
refreshToken= data['data']['refreshToken']

#fetch the feedtoken
feedToken=obj.getfeedToken()

#fetch User Profile
userProfile= obj.getProfile(refreshToken)
# #place order
# try:
#     orderparams = {
#         "variety": "NORMAL",
#         "tradingsymbol": "SBIN-EQ",
#         "symboltoken": "3045",
#         "transactiontype": "BUY",
#         "exchange": "NSE",
#         "ordertype": "LIMIT",
#         "producttype": "INTRADAY",
#         "duration": "DAY",
#         "price": "19500",
#         "squareoff": "0",
#         "stoploss": "0",
#         "quantity": "1"
#         }
#     orderId=obj.placeOrder(orderparams)
#     print("The order id is: {}".format(orderId))
# except Exception as e:
#     print("Order placement failed: {}".format(e.message))
# #gtt rule creation
# try:
#     gttCreateParams={
#             "tradingsymbol" : "SBIN-EQ",
#             "symboltoken" : "3045",
#             "exchange" : "NSE", 
#             "producttype" : "MARGIN",
#             "transactiontype" : "BUY",
#             "price" : 100000,
#             "qty" : 10,
#             "disclosedqty": 10,
#             "triggerprice" : 200000,
#             "timeperiod" : 365
#         }
#     rule_id=obj.gttCreateRule(gttCreateParams)
#     print("The GTT rule id is: {}".format(rule_id))
# except Exception as e:
#     print("GTT Rule creation failed: {}".format(e.message))
    
# #gtt rule list
# try:
#     status=["FORALL"] #should be a list
#     page=1
#     count=10
#     lists=obj.gttLists(status,page,count)
# except Exception as e:
#     print("GTT Rule List failed: {}".format(e.message))

#Historic api
try:
    historicParam={
    "exchange": "NSE",
    "symboltoken": "3045",
    "interval": "ONE_MINUTE",
    "fromdate": "2021-02-08 09:00", 
    "todate": "2021-02-08 09:16"
    }
    HistSBI = obj.getCandleData(historicParam)
    print(HistSBI['data'])
except Exception as e:
    print("Historic Api failed: {}".format(e.message))
# #logout
# try:
#     logout=obj.terminateSession('A1128018')
#     print("Logout Successfull")
# except Exception as e:
#     print("Logout failed: {}".format(e.message))



# ## WebSocket
# from smartapi import WebSocket

# FEED_TOKEN= feedToken
# CLIENT_CODE="A1128018"
# token="nse_cm|2885&nse_cm|1594&nse_cm|11536" #"channel you want the information of" #"nse_cm|2885&nse_cm|1594&nse_cm|11536"
# task="mw" #"mw"|"sfi"|"dp"
# ss = WebSocket(FEED_TOKEN, CLIENT_CODE)

# def on_tick(ws, tick):
#     print("Ticks: {}".format(tick))

# def on_connect(ws, response):
#     ws.websocket_connection() # Websocket connection  
#     ws.send_request(token,task) 
    
# def on_close(ws, code, reason):
#     ws.stop()

# # Assign the callbacks.
# ss.on_ticks = on_tick
# ss.on_connect = on_connect
# ss.on_close = on_close

# ss.connect()


