print("you can!!")
import login as login
from datetime import datetime
import time
import os
import time
import json
from niftystocks import ns
import math

high=[]
trades = 0



# print(login.fyers.get_profile())

print("LOGGED-IN")

# symbols = ['NSE:AXISBANK-EQ', 'NSE:BAJAJ-AUTO-EQ', 'NSE:BHARTIARTL-EQ', 'NSE:BPCL-EQ', 'NSE:CIPLA-EQ', 'NSE:COALINDIA-EQ', 'NSE:EICHERMOT-EQ', 'NSE:GRASIM-EQ', 'NSE:HCLTECH-EQ', 'NSE:HDFC-EQ', 'NSE:HDFCBANK-EQ', 'NSE:HDFCLIFE-EQ', 'NSE:HEROMOTOCO-EQ', 'NSE:HINDALCO-EQ', 'NSE:HINDUNILVR-EQ', 'NSE:ICICIBANK-EQ', 'NSE:INDUSINDBK-EQ', 'NSE:INFY-EQ', 'NSE:IOC-EQ', 'NSE:ITC-EQ', 'NSE:JSWSTEEL-EQ', 'NSE:KOTAKBANK-EQ', 'NSE:LT-EQ', 'NSE:M&M-EQ', 'NSE:NTPC-EQ', 'NSE:RELIANCE-EQ', 'NSE:SBILIFE-EQ', 'NSE:SBIN-EQ', 'NSE:SUNPHARMA-EQ', 'NSE:TATACONSUM-EQ', 'NSE:TATAMOTORS-EQ', 'NSE:TATASTEEL-EQ', 'NSE:TCS-EQ', 'NSE:TECHM-EQ', 'NSE:TITAN-EQ', 'NSE:UPL-EQ']

symbols= ['NSE:TATASTEEL-EQ']



def buffer_price(equity_price):
    buffer = 0.001  # 0.1% buffer
    buffer_price = equity_price * (1 + buffer)
    buffer_price_rounded = round(buffer_price + 0.0005, 3)
    buffer_price_rounded = buffer_price_rounded - equity_price
    buffer_price_divisible = round(buffer_price_rounded * 20) / 20
    return buffer_price_divisible




def data_handling(symbol):
    date = datetime.today().strftime('%Y-%m-%d')
    hist_data = {"symbol":symbol,"resolution":"30","date_format":1,"range_from":date,"range_to":date,"cont_flag":"1"}
    srp = login.fyers.history(hist_data)
    # print(srp)
    hl_data = srp["candles"][0]
    high = hl_data[2] 
    low = hl_data[3]
    # print("High:",high,"  ","Low:",low)
    return high, low
    
def calculate_position_size(price):
    available_capital = get_available_funds() / 4
    quantity = 1
    risk_per_unit = price * 0.003
    max_capital_risk = available_capital * 0.003
    quantity = max_capital_risk / risk_per_unit
    return round(quantity)

    
def get_available_funds():
    try:
        return login.fyers.funds()['fund_limit'][-1]['equityAmount']
    except:
        return 50000

# print(funds())

def place_orders(symbol,h,l):
   
    df = {"symbols":symbol}
    var = login.fyers.quotes(df)["d"]
    ltp = var[0]["v"]['lp']
    
    LSL=round(h*.003)
    SSL=round(l*.003)
    LTR=round(h*.006)
    STR=round(l*.006)
    
    longWithBuffer=buffer_price(h)
    shortWithBuffer= buffer_price(l)
      
    print(f"LTP:{ltp} Low:{l} High:{h} longwithbuff{longWithBuffer} shortbuff{shortWithBuffer}")

    global trades

    if (ltp >= longWithBuffer)  and (trades < 5):
        trades += 1
        symbols.remove(symbol)                   
        print(f'LONG:{symbol} Signal@: {h} Signal with buffer:{shortWithBuffer} Entry@:{ltp} qty:{calculate_position_size(ltp)}')
        # data = {"symbol":symbol,"qty":calculate_position_size(ltp),"type":2,"side":1,"productType":"BO",
        # "limitPrice":0,"stopPrice":0,"validity":"DAY","disclosedQty":0,"offlineOrder":"False",  "stopLoss":LSL,"takeProfit":LTR}
        # response = login.fyers.place_order(data)
        # print(response)
        
    elif (ltp <= shortWithBuffer) and (trades < 5):
        trades += 1
        symbols.remove(symbol)

        print(f'sorted:{symbol} Signal@: {l} Signal with buffer:{shortWithBuffer} Entry@:{ltp} qty:{calculate_position_size(ltp)}')
        # data = {"symbol":symbol,"qty":calculate_position_size(ltp),"type":2,"side":-1,"productType":"BO",
        # "limitPrice":0,"stopPrice":0,"validity":"DAY","disclosedQty":0,"offlineOrder":"False",  "stopLoss":SSL,"takeProfit":STR}
        # response = login.fyers.place_order(data)
        # print(response)
        
    
    else:
        pass


    
    
    
        
    
start = "09:44:00"    
end = "15:00:00"
now = datetime.strftime(datetime.now(),"%H:%M:%S")

# Check is it need to run a code in range of 9:40 - 3:30
run = True if ((now>start) & (now<end)) else False

# next line i added back test
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



