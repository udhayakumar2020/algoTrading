print("you can!!")
import login as login
from datetime import datetime
import time
import os
import time
import json
from niftystocks import ns
import math
true = True 
# WHOLE WROMG ITS JUST BACKTESTING WE NEED TO CHANGE AS A LIVE PRICE TO TRADE IN LICE AND CURRENT PRICe
# =>After 10:15 no trade is a best 
# => buffer of 0.01 is a best to cut some entries 
loss=0
profit=0
symbolsinlongprofit=[]
symbolsinlongloss=[]
symbolsinshortloss=[]
symbolsinshortprofit=[]
high=[]
trades = 0



# print(login.fyers.get_profile())
print("LOGGED-IN")

# get Current price

# symbols = ['NSE:AXISBANK-EQ', 'NSE:BAJAJ-AUTO-EQ', 'NSE:BHARTIARTL-EQ', 'NSE:BPCL-EQ', 'NSE:CIPLA-EQ', 'NSE:COALINDIA-EQ', 'NSE:EICHERMOT-EQ', 'NSE:GRASIM-EQ', 'NSE:HCLTECH-EQ', 'NSE:HDFC-EQ', 'NSE:HDFCBANK-EQ', 'NSE:HDFCLIFE-EQ', 'NSE:HEROMOTOCO-EQ', 'NSE:HINDALCO-EQ', 'NSE:HINDUNILVR-EQ', 'NSE:ICICIBANK-EQ', 'NSE:INDUSINDBK-EQ', 'NSE:INFY-EQ', 'NSE:IOC-EQ', 'NSE:ITC-EQ', 'NSE:JSWSTEEL-EQ', 'NSE:KOTAKBANK-EQ', 'NSE:LT-EQ', 'NSE:M&M-EQ', 'NSE:NTPC-EQ', 'NSE:RELIANCE-EQ', 'NSE:SBILIFE-EQ', 'NSE:SBIN-EQ', 'NSE:SUNPHARMA-EQ', 'NSE:TATACONSUM-EQ', 'NSE:TATAMOTORS-EQ', 'NSE:TATASTEEL-EQ', 'NSE:TCS-EQ', 'NSE:TECHM-EQ', 'NSE:TITAN-EQ', 'NSE:UPL-EQ']

# janhighproba=['NSE:ASIANPAINT-EQ','NSE:HDFC-EQ','NSE:HDFCBANK-EQ','NSE:EICHERMOT-EQ','NSE:INDUSINDBK-EQ','NSE:SBIN-EQ','NSE:ICICIBANK-EQ','NSE:MARUTI-EQ','NSE:BAJAJFINSV-EQ','NSE:HINDUNILVR-EQ','NSE:JSWSTEEL-EQ','NSE:HDFCLIFE-EQ','NSE:M&M-EQ','NSE:BAJAJ-AUTO-EQ','NSE:BHARTIARTL-EQ','NSE:IOC-EQ','NSE:KOTAKBANK-EQ','NSE:POWERGRID-EQ','NSE:RELIANCE-EQ']

# symbols= ["NSE:ICICIBANK-EQ","NSE:BPCL-EQ","NSE:HCLTECH-EQ",'NSE:INFY-EQ', 'NSE:BHARTIARTL-EQ','NSE:AXISBANK-EQ','NSE:CIPLA-EQ','NSE:HINDALCO-EQ','NSE:LT-EQ','NSE:TATAMOTORS-EQ','NSE:HDFCBANK-EQ', 'NSE:JSWSTEEL-EQ', 'NSE:UPL-EQ']

# symbols = janhighproba
symbols = ['NSE:AXISBANK-EQ']
def data_handling(symbol):
    date = datetime.today().strftime('%Y-%m-%d')
    hist_data = {"symbol":symbol,"resolution":"60","date_format":1,"range_from":date,"range_to":date,"cont_flag":"1"}
    srp = login.fyers.history(hist_data)
    # print(srp)
    hl_data = srp["candles"][0]
    high = hl_data[2] 
    low = hl_data[3]
    # print("High:",high,"  ","Low:",low)
    return high, low
    
def calculate_long_position_size(price):
    available_capital = get_available_funds() / 4
    quantity = 1
    risk_per_unit = price * 0.003
    max_capital_risk = available_capital * 0.003
    quantity = max_capital_risk / risk_per_unit

    return round(quantity)

def calculate_short_position_size(price):
    available_capital = get_available_funds() / 3
    quantity = 1
    risk_per_unit = price * 0.003
    max_capital_risk = available_capital * 0.003
    quantity = max_capital_risk / risk_per_unit

    return math.floor(quantity)
    
def get_available_funds():
    try:
        return login.fyers.funds()['fund_limit'][-1]['equityAmount']

    except:
        return 70000

# print(funds())

def place_orders(symbol,h,l):
   
    df = {"symbols":symbol}
    var = login.fyers.quotes(df)["d"]
    ltp = var[0]["v"]['lp']
    
    LSL=round(h*.003)
    SSL=round(l*.003)
    LTR=round(h*.006)
    STR=round(l*.006)
    longWithBuffer=math.ceil(0.001 * h) + h
    shortWithBuffer= l - round(0.001 * l)  
    print(f"LTP:{ltp} Low:{l} High:{h} longwithbuff{longWithBuffer} shortbuff{shortWithBuffer}")

    global trades
    


    if (ltp >= longWithBuffer)  and (trades < 5):
        trades += 1
        symbols.remove(symbol)                   
        print(f'LONG:{symbol} Signal@: {h} Signal with buffer:{shortWithBuffer} Entry@:{ltp} qty:calculate_position_size(ltp)')
        data = {"symbol":symbol,"qty":calculate_long_position_size(ltp),"type":2,"side":1,"productType":"BO",
        "limitPrice":0,"stopPrice":0,"validity":"DAY","disclosedQty":0,"offlineOrder":"False",  "stopLoss":LSL,"takeProfit":LTR}
        response = login.fyers.place_order(data)
        print(response)
        
    elif (ltp <= shortWithBuffer) and (trades < 5):
        trades += 1
        symbols.remove(symbol)

        print(f'sorted:{symbol} Signal@: {l} Signal with buffer:{shortWithBuffer} Entry@:{ltp} qty:calculate_position_size(ltp)')
        data = {"symbol":symbol,"qty":calculate_short_position_size(ltp),"type":2,"side":-1,"productType":"BO",
        "limitPrice":0,"stopPrice":0,"validity":"DAY","disclosedQty":0,"offlineOrder":"False",  "stopLoss":SSL,"takeProfit":STR}
        
        response = login.fyers.place_order(data)
        
        print(response)
        
    
    else:
        pass


    
    
    ltp = var[0]
    
   
        
        
        
        
        
        
# response = login.fyers.gainers()
# print(response)
        
        
        
        
    
start = "09:44:00"    
end = "15:00:00"
now = datetime.strftime(datetime.now(),"%H:%M:%S")

# Check is it need to run a code in range of 9:40 - 3:30
run = True if ((now>start) & (now<end)) else False

# next line i aded back test
# run = True 


if run==False and now<start:
    x = True
    while x:
        # funds()
        print("Waiting for market to open")
        time.sleep(30)
        now = datetime.strftime(datetime.now(),"%H:%M:%S")
        x = True if now<start else False
    run = True
    

while run:
    print("\nCurrent time","   ",now)
    for i in symbols:
        print("\n"+i)
        h,l= data_handling(i)
        place_orders(i,h,l)
    print("after delete",symbols)
    time.sleep(30)
    
    now = datetime.strftime(datetime.now(),"%H:%M:%S")
    run = True if ((now>start) & (now<end)) else False




if now>end:
    print("\nMarket Closed!")





#                 # data = {"symbol":symbol,"qty":1,"type":2,"side":1,"productType":"CO",
                # "limitPrice":0,"stopPrice":0,"validity":"DAY","disclosedQty":0,"offlineOrder":"False",  "stopLoss":l-1,"takeProfit":0}
                # response = login.fyers.place_order(data)
# 
#       elif short == True:
        
#             if high > l+sSL :
#                 loss +=200
#                 symbolsinshortloss.append(symbol)
#                 print(f'{symbol}Loss in candle:{candle} SORTING at{l}  Sl{l+sSL} TRG{l-sTR}')
#                 break
#             elif low < l+sTR:
#                 profit +=400
#                 symbolsinshortprofit.append(symbol)
#                 print(f'{symbol}Profit in candle:{candle} SORTING at{l} Sl{l+sSL} TRG{l-sTR} ')
#                 break
#             elif candle == totalCandle:
#                 # print("CLOSED AT EOD Short")               
#                 break
#         elif long == True:
#             if high > h+lTR :
#                 profit +=400
#                 symbolsinlongprofit.append(symbol)
#                 # print(symbolsinlongprofit)
#                 print(f'{symbol}Profit in candle{candle},LONG signal @ {h}  Sl{h-lSL} TRG{h+lTR}  ')
#                 break
#             elif low < h-lSL:
#                 loss+=200
#                 symbolsinlongloss.append(symbol)
#                 print(f'{symbol}Loss in candle{candle} LONG signal at{h} entry{high} Sl{h-lSL} TRG{h+lTR} ')

#                 break
#             elif candle == totalCandle :
#                 print("EXITED WITH SQUARE OFF Long EOD" )
#                 break

