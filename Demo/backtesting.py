print("you can!!")
print(
    'Loot of scripts are found there but all are not good for a intraday ORB strategy right res lets choose a best ones '
)
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

# =>Issue =>in cipla sorting sorting all issue i think dude
# =>Need a buffers.01 and stopentry at after 10:20 


# Need a single symbol to take a month or year data to test which scripts are suitable with which R:R and SL:TR:


loss = 0
profit = 0
symbolsinlongprofit = []
symbolsinlongloss = []
symbolsinshortloss = []
symbolsinshortprofit = []
symbolsindraw=[]
high = []
wholeEntries=0
lbuffer = 0

wins=0
losses=0
draw=0


print("LOGGED-IN")
# symbols = [
#     'NSE:SBIN-EQ', 'NSE:KOTAKBANK-EQ', 'NSE:AXISBANK-EQ', 'NSE:HDFCBANK-EQ',
#     'NSE:ICICIBANK-EQ', 'NSE:LT-EQ', 'NSE:BHARTIARTL-EQ', 'NSE:INDUSINDBK-EQ',
#     'NSE:HDFC-EQ', 'NSE:HINDALCO-EQ', 'NSE:TITAN-EQ', 'NSE:TCS-EQ',
#     'NSE:POWERGRID-EQ', 'NSE:WIPRO-EQ', 'NSE:INFY-EQ', 'NSE:TECHM-EQ'
# ]






symbols = ['NSE:AXISBANK-EQ', 'NSE:BAJAJ-AUTO-EQ', 'NSE:BHARTIARTL-EQ', 'NSE:BPCL-EQ', 'NSE:CIPLA-EQ', 'NSE:COALINDIA-EQ', 'NSE:EICHERMOT-EQ', 'NSE:GRASIM-EQ', 'NSE:HCLTECH-EQ', 'NSE:HDFC-EQ', 'NSE:HDFCBANK-EQ', 'NSE:HDFCLIFE-EQ', 'NSE:HEROMOTOCO-EQ', 'NSE:HINDALCO-EQ', 'NSE:HINDUNILVR-EQ', 'NSE:ICICIBANK-EQ', 'NSE:INDUSINDBK-EQ', 'NSE:INFY-EQ', 'NSE:IOC-EQ', 'NSE:ITC-EQ', 'NSE:JSWSTEEL-EQ', 'NSE:KOTAKBANK-EQ', 'NSE:LT-EQ', 'NSE:M&M-EQ', 'NSE:NTPC-EQ', 'NSE:RELIANCE-EQ', 'NSE:SBILIFE-EQ', 'NSE:SBIN-EQ', 'NSE:SUNPHARMA-EQ', 'NSE:TATACONSUM-EQ', 'NSE:TATAMOTORS-EQ', 'NSE:TATASTEEL-EQ', 'NSE:TCS-EQ', 'NSE:TECHM-EQ', 'NSE:TITAN-EQ', 'NSE:UPL-EQ']
# janhighproba=['NSE:ASIANPAINT-EQ','NSE:HDFC-EQ','NSE:HDFCBANK-EQ','NSE:EICHERMOT-EQ','NSE:COALINDIA-EQ','NSE:INDUSINDBK-EQ','NSE:SBIN-EQ','NSE:ICICIBANK-EQ','NSE:MARUTI-EQ','NSE:BAJAJFINSV-EQ','NSE:HINDUNILVR-EQ','NSE:JSWSTEEL-EQ','NSE:HDFCLIFE-EQ','NSE:M&M-EQ','NSE:INFY-EQ','NSE:BAJAJ-AUTO-EQ','NSE:BHARTIARTL-EQ','NSE:KOTAKBANK-EQ','NSE:POWERGRID-EQ','NSE:RELIANCE-EQ']
# symbols=janhighproba

# symbols=['NSE:HDFC-EQ', 'NSE:HDFCBANK-EQ','NSE:AXISBANK-EQ', 'NSE:GRASIM-EQ', 'NSE:HEROMOTOCO-EQ', 'NSE:HINDALCO-EQ', 'NSE:ICICIBANK-EQ', 'NSE:ITC-EQ', 'NSE:SBIN-EQ', 'NSE:TATACONSUM-EQ', 'NSE:TATASTEEL-EQ']  

# symbols= ['NSE:NIFTY50-INDEX']
# OHLC
def data_handling(symbol):
    # date = '2023-01-20'
    # date = datetime.today().strftime('%Y-%m-%d')
    date = '2023-03-23'

    hist_data = {
        "symbol": symbol,
        "resolution": "30",
        "date_format": 1,
        "range_from": date,
        "range_to": date,
        "cont_flag": "1"
    }
    srp = login.fyers.history(hist_data)
    # print(date)
    hl_data = srp["candles"][0]
    high = hl_data[2]
    low = hl_data[3]
    # print("High:", high, "  ", "Low:", low)
    return high, low, srp


# data_handling("NSE:SBIN-EQ")


def place_orders(symbol, h, l, day30M):
    lSL = round(h * .003)
    sSL = round(l * .003)
    lTR = round(h * .006)
    sTR = round(l * .006)
    global lbuffer
    
    lbuffer = math.floor( l * .001)
    lbuffer = 0

    print(lbuffer)
    hbuffer = round( 0)
    lbuffer = 0
    hbuffer = 0

    profitAmount=200
    lossAmount=100
    long = False
    short = False
    global loss
    global profit
    global wholeEntries 
    traded = False
    candle = 0
    
    
    global wins
    global losses
    global draw

    var = day30M['candles']  # here wwe need to loop all the 30 mis candle to find the entry and exit to calculatr profit aand loss
    totalCandle = len(var)
    for i in var:

        candle += 1  #with variable candle u can diable the afternoon trades or change range
        # print('Current candle:',candle)
        opening = i[1]
        high = i[2]
        low = i[3]
        lbuff = l * .001
        hbuff = h * .001
        close = [4]
        volume = [5]

        # long=False
        # short=False
        # traded=False
        # print(i ,'high=',high , 'low',low)
        # print()
        def trade():
            pass

        if traded != True:
            # + hbuff and candle < 4
            if high > (h + hbuffer) and candle <= 9:
                # symbols.remove(symbol)
                print(f'Long in {symbol}')
                # with open('trades.txt','a') as Entrysctipt:
                #     Entrysctipt.write("'"+symbol+"'"+',')
                    
                traded = True
                long = True
                wholeEntries +=1
                continue
            elif low < (l - lbuffer) and candle <= 9:
                # symbols.remove(symbol)

                # - lbuff and candle< 4
                print(f"Sort in {symbol} at:{l-lbuffer}")
            
                # print(f'{symbol}Selling at{low} with SL__ TRG__ ')
                wholeEntries +=1
                traded = True
                short = True
                continue
            # elif candle > 6:
            # #which helps in avoiding late entries
            #     break
            elif candle == totalCandle:
                draw +=1
                pass
                # print(f'range Bound in candle {candle}')
        elif short == True:

            if high > l + sSL:
                losses +=1
                loss += lossAmount
                symbolsinshortloss.append(symbol)
                print(
                    f'{symbol}Loss in candle:{candle} SORTING at{l}  Sl{l+sSL} TRG{l-sTR}'
                )

                break
            elif low < l - sTR:
                # print(sTR)
                
                wins +=1
                profit += profitAmount
                symbolsinshortprofit.append(symbol)

                print(
                    f'{symbol}Profit in candle:{candle} SORTING at{l} Sl{l+sSL} TRG{l-sTR} '
                )
                break
            
            elif candle == totalCandle:
                draw +=1
                symbolsindraw.append(symbol)
                # drawpoint = float(l[0]) - float(close[0])
                # drawpoint = float(l) - float(close)

                # print(f'drawPoints:{drawpoint}')
            
                # wins +=1
                print("CLOSED AT EOD Short")
                break
            
        elif long == True:
            if high > h + lTR:
               
                wins +=1
                profit += profitAmount
                symbolsinlongprofit.append(symbol)
                # print(symbolsinlongprofit)
                print(
                    f'{symbol}Profit in candle{candle},LONG signal @ {h}  Sl{h-lSL} TRG{h+lTR}  '
                )
                break
            
            elif low < h - lSL:
                losses +=1
                loss += lossAmount
                symbolsinlongloss.append(symbol)
                print(
                    f'{symbol}Loss in candle{candle} LONG signal at{h + hbuffer} entry{high} Sl{h-lSL} TRG{h+lTR} '
                )

                break
            elif candle == totalCandle:
                # this works onlt EOD
                symbolsindraw.append(symbol)
                # drawpoint = h - close   
                # print(f'drawPoints:{drawpoint}')
                draw +=1
                print("EXITED WITH SQUARE OFF Long EOD")
                break

    # 13 30mins candle in a day
    # print("VAR:",var)
    ltp = var[0]

    # print("LTP:", ltp)
    # if ltp>h:
    #     print("Placing buy market cover order!")
    # elif ltp<l:
    #     print("Placing sell market cover order!")
    # else:
    #     print("Price between Opening Range High and Low!")


start = "09:45:00"
end = "15:00:00"
now = datetime.strftime(datetime.now(), "%H:%M:%S")

# Check is it need to run a code in range of 9:40 - 3:30
run = True if ((now > start) & (now < end)) else False

# next line i aded back test
run = True

if run == False and now < start:
    x = True
    while x:
        print("Waiting for market to open")
        time.sleep(60)
        now = datetime.strftime(datetime.now(), "%H:%M:%S")
        x = True if now < start else False
    run = True

while run:
    print("\nCurrent time", "   ", now)
    for i in symbols:
        print("\n" + i)
        h,l,day30M = data_handling(i)
        place_orders(i, h, l, day30M)
    print("profit total", profit)
    print('loss total', loss)
    print('DRAW total', draw)

    print('Total entries',wholeEntries)
    print('Brokerages $5:',wholeEntries * 20)
    print('AfterBrokerages:',profit - loss -(wholeEntries * 5))
    # print("Total$:",profit - loss)
    # print(symbols)
    # time.sleep(30)

    now = datetime.strftime(datetime.now(), "%H:%M:%S")
    # run = True if ((now > start) & (now < end)) else False
    run = False 

print("symbolsinshortprofit", symbolsinshortprofit)
print("symbolsinshortloss", symbolsinshortloss)
print("symbolsinlongprofit", symbolsinlongprofit)
print('symbolsinlongloss', symbolsinlongloss)
print('Probabilityof win' ,wins / (wins+losses) *100)

if now > end:
    print("\nMarket Closed!")

#
#
#


# with open('ExcelUi.csv', 'a') as csvfile:
#                     FieldName = [
#                         'Name', 'Entryprice', 'Exitprice', 'side', 'status'
#                     ]
#                     theWritter = csv.DictWriter(csvfile, fieldnames=FieldName)
#                     theWritter.writeheader()
#                     theWritter.writerow({
#                         'Name': symbol,
#                         'Entryprice': h,
#                         'Exitprice': low,
#                         'side': 'long',
#                         'status': 'loss'
#                     })

#  with open('ExcelUi.csv', 'a') as csvfile:
#                     FieldName = [
#                         'Name', 'Entryprice', 'Exitprice', 'side', 'status'
#                     ]
#                     theWritter = csv.DictWriter(csvfile, fieldnames=FieldName)
#                     theWritter.writeheader()
#                     theWritter.writerow({
#                         'Name': symbol,
#                         'Entryprice': h,
#                         'Exitprice': high,
#                         'side': 'long',
#                         'status': 'Profit'
#                     })