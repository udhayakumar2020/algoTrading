# ITS  BACKTESTING WE NEED TO CHANGE AS A LIVE PRICE TO TRADE IN LIvE AND CURRENT PRICe
# =>Issue =>in cipla sorting sorting all issue i think dude
# =>Need a buffers.01 and stopentry at after 10:20
# Need a single symbol to take a month or year data to test which scripts are suitable with which R:R and SL:TR:

# make a accurate numberr rounding and buffer price should be ggod
# candle close after that entry is good buddy
# LTSL be wise and profit should be in points and percentages is good and scaleable
# print(
#     'Loot of scripts are found there but all are not good for a intraday ORB STRategy right res lets choose a best ones '
# )
print("you can!!")

import matplotlib as plt
import matplotlib.pyplot as plt
import login as login
import dailydataFetch as DFL
from datetime import datetime
import time
import os
import time
import json
from niftystocks import ns
import math
import pandas as pd

import matplotlib.dates as mdates

timeFrame = "5"
loss = 0
profit = 0
symbolsinlongprofit = []
symbolsinlongloss = []
symbolsinshortloss = []
symbolsinshortprofit = []
noentrys=[]
symbolsindraw = []
candleHigh = []
cumPer=0
cumPerlist=[]
wholeEntries = 0
lbuffer = 0
No_entry = 0
wins = 0
losses = 0
draw = 0
longLPts = 0
longPPts = 0
shortLPts = 0
shortPPts = 0
recentHigh = 0
cumSortPer = 0
cumLongPer =0
j=1
close_plot =[]
# timeFrame, loss, profit = "5", 0, 0
# symbols = {'long': {'profit': [], 'loss': []}, 'short': {'profit': [], 'loss': []}, 'draw': [], 'noentry': []}
# candleHigh, cumPer, cumPerlist, wholeEntries, lbuffer, No_entry, wins, losses, draw = [], 0, [], 0, 0, 0, 0, 0, 0
# points = {'long': {'profit': 0, 'loss': 0}, 'short': {'profit': 0, 'loss': 0}}
# recentHigh, cumSortPer, cumLongPer = 0, 0, 0
# symbolsinlongprofit'   not defined

print("LOGGED-IN")

# symbols = [
#     'NSE:SBIN-EQ', 'NSE:KOTAKBANK-EQ', 'NSE:AXISBANK-EQ', 'NSE:HDFCBANK-EQ',
#     'NSE:ICICIBANK-EQ', 'NSE:LT-EQ', 'NSE:BHARTIARTL-EQ', 'NSE:INDUSINDBK-EQ',
#      'NSE:HINDALCO-EQ', 'NSE:TITAN-EQ', 'NSE:TCS-EQ',
#     'NSE:POWERGRID-EQ', 'NSE:WIPRO-EQ', 'NSE:INFY-EQ', 'NSE:TECHM-EQ'
# ]
symbols = ['NSE:BHARTIARTL-EQ', 'NSE:BPCL-EQ', 'NSE:CIPLA-EQ', 'NSE:COALINDIA-EQ', 'NSE:EICHERMOT-EQ', 'NSE:GRASIM-EQ', 'NSE:HCLTECH-EQ', 'NSE:HDFCLIFE-EQ', 'NSE:HEROMOTOCO-EQ', 'NSE:HINDALCO-EQ', 'NSE:HINDUNILVR-EQ', 'NSE:ICICIBANK-EQ', 'NSE:INDUSINDBK-EQ', 'NSE:INFY-EQ', 'NSE:IOC-EQ', 'NSE:ITC-EQ', 'NSE:JSWSTEEL-EQ', 'NSE:KOTAKBANK-EQ', 'NSE:LT-EQ', 'NSE:M&M-EQ', 'NSE:NTPC-EQ', 'NSE:RELIANCE-EQ', 'NSE:SBILIFE-EQ', 'NSE:SBIN-EQ', 'NSE:SUNPHARMA-EQ', 'NSE:TATACONSUM-EQ', 'NSE:TATAMOTORS-EQ', 'NSE:TATASTEEL-EQ', 'NSE:TCS-EQ', 'NSE:TECHM-EQ', 'NSE:TITAN-EQ', 'NSE:UPL-EQ']
# symbols = ['NSE:BHARTIARTL-EQ']
# symbols = ['NSE:NIFTYBANK-INDEX']
# symbols = ['NSE:BHARTIARTL-EQ']

def YDCfn(symbol):
    df = {"symbols": symbol}
    SYdata = login.fyers.quotes(df)["d"]
    YDC = SYdata[0]["v"]['prev_close_price']
    return YDC
    



day_hignsight =[]
day_hindsight=[]
tradedate="2024-04-25"

def place_orders(symbol, resistence, support, data):
   
    print(type(symbol))
    print(type(resistence))
    print(type(support))
    print(type(support))
    print(type(data))

    for  i in range (1):
        global day_hindsight
        # day_hindsight.append(day_data)
        closeplot=  data["Open"].tolist()
        normalized_data = [val / closeplot[0] - 1 for val in closeplot]

        day_hindsight.append(normalized_data)
        # print(normalized_data)
        for  i in day_hindsight:
            plt.plot(i , label=f'{symbol}')


    # Use a different color or style for each stock

    # print(support,resistence)
    # print(data.head().to_string())
    # YDC = YDCfn(symbol)
    global longLPts, longPPts, shortLPts, shortPPts, loss, profit, wholeEntries,cumPer,cumPerlist
    global wins, losses, draw, No_entry, recentHigh ,cumSortPer,cumLongPer
    longLPts = longPPts = shortLPts = shortPPts = loss = profit = wholeEntries = 0
    wins = losses = draw = No_entry = recentHigh = 0
    # print(cumSortPer)
     
    # Initial parameters
    lSL = resistence - round(resistence * 0.005, 1)
    SSL = round(support * 0.005,1)
    LTR = round(resistence * 0.9,1)
    STR = round(support * 0.5,1)
    LTSLper=.005
    STSLper=.005
    LTTR=00 ##trailing long target
    STTR=00 ##trailing long target
    
    
    # Buffers and trading signals
    lbuffer = hbuffer = 0
    long = short = traded = False
    candle = 0
    
# Plot high values for each date on the same graph without transparency
    b =[]
    counts = 0
        
    for countss , day_data in data.groupby("date"):
        # counts +=1
        # print(counts)
        hi =[]
        for index, i in day_data.iterrows():
            hi.append(i["Close"])
        normalized_b = [val / hi[0] - 1 for val in hi]

    #     plt.plot(normalized_b)
    # plt.show() 
    
    
    
    
            # plt.plot(i["High"])
            # plt.show()
    # plt.title('High Values Overlay Across Dates')
    # plt.xlabel('Index')
    # plt.ylabel('High Value')
    # plt.legend()
    # plt.show()

        # for i in range(1, len(day_data)):
        #   day_data[i] = day_data[i].reindex_like(day_data[0], method='ffill')
        # for idx, day_data in enumerate(day_data):
        #     plt.plot(day_data['High'], marker='o', linestyle='-', label=f'Data Set {idx + 1}')

    for date, day_data in data.groupby("date"):

        traded = False
        # day_data.sort_index(inplace=True)
        # print(day_data['High'].head(6))
        
        resistence =day_data['High'].head(7).max()
        support=day_data['Low'].head(7).min()

        # print()
        candle=0
        totalCandle = len(day_data)
        
        

        # print(day_data.head())
        for index, i in day_data.iterrows():
            candle += 1           
            candleHigh = i['High']
            candleLow = i['Low']
            lbuff = support * .001
            hbuff = resistence * .001
            close = i['Close']
            volume = i['Volume']
            recentHigh=i['recentHigh']
            recentLow=i['recentLow']
            dayHigh=i['dayHigh']
            dayLow=i['dayLow']



            if traded != True:
                # + hbuff and candle < 4and high > YDC and low < YDC
                # print(f'-{support}-{resistence} --{close} {candle}')
                if close > resistence and candle < 80 :
                    print(f'Long-{symbol} Resistence{resistence} Candle:{candle}')
                    traded = True ; long = True; short = False; wholeEntries += 1
                    continue
                
                elif close < support and candle < 30:
                    # - lbuff and candle< 4
                    print(f"Sort-{symbol} Support:{support} Candle:{candle}")
                    wholeEntries += 1;traded = True;long = False; short = True
                    continue

                elif candle == totalCandle:
                    No_entry += 1
                    noentrys.append(date)
                    pass

            elif short == True:
                STSL = round(((candleLow + dayHigh) / 2 ) + round(dayLow * STSLper, 1),2)
                STTR = dayLow - round(dayLow * LTSLper, 1)
                IS_STSL = True
                # print(f'STSL:{STSL} / low:high{candleLow}/{candleHigh}')               

                if candleLow < (support - STR):
                    # print(STR)
                    points=support - candleLow
                    cumSortPer +=((support - candleLow) / support) * 100
                    cumPer +=((support - candleLow) / support) * 100  
                    cumPerlist.append(cumPer)
                    wins += 1
                    symbolsinshortprofit.append(f"{symbol}=> =>{((support - candleLow) / support) * 100}")
                    print(
                        f'Targeted:{symbol}- {date}Profit in candle:{candle} SORTING at{l} Sl{l+SSL} TRG{l-STR} Shortprofit{points}%={cumLongPer}'
                    )
                    break
                
                elif candleHigh > STSL:
                    if IS_STSL:
                        points=candleHigh - support
                        cumSortPer +=((support - candleLow) / support) * 100
                        cumPer +=((support - candleLow) / support) * 100
                        cumPerlist.append(cumPer)
                        losses += 1
                        symbolsinshortloss.append(f"{symbol}=>  =>{((support - candleLow) / support) * 100}")
                        print(
                            f'LTSL {symbol} - {date} exited@candle:{candle} SORTING at{support}  Sl{STSL} TRG{support-STR} ShortLosspts:{points} cumul%={cumLongPer}'
                        )
                        break
                
                   
                elif candle == totalCandle:
                    shortPPts += STR
                    cumSortPer += ((support - candleLow) / support) * 100
                    cumPer += ((support - candleLow) / support) * 100
                    cumPerlist.append(cumPer)
                    draw +=1
                    symbolsinshortprofit.append(f"{symbol} =>{((support - candleLow) / support) * 100}")
                    print("Sort exit at eod")

                    # elif
            
            elif long == True:
                
                # print(f'current SL:{lSL} & candle:{candle} & {recentHigh} &{dayHigh}')
                LTSL = round(((candleLow + dayHigh) / 2 ) - round(dayHigh * LTSLper, 1),2)
                LTTR = dayHigh - round(dayHigh * LTSLper, 1)
                # print(LTSL)
                IS_TRSL = True
                print(f' ltsl:{LTSL} / low:{candleLow}')
               
                if candleHigh > resistence + LTR:
                     
                    # print("1")
                    cumLongPer += ((candleHigh - resistence) / resistence)*100
                    cumPer +=((candleHigh - resistence) / resistence)*100
                    cumPerlist.append(cumPer)

  
                    wins += 1
                    symbolsinlongprofit.append(f"{symbol}=>{((candleHigh - resistence) / resistence)*100}")
                    # print(symbolsinlongprofit)
                    longPPts += candleHigh - resistence
                    print(
                        f'Targeeet hit:{symbol}- {date} Profit in candle:{candle} LONG signal @:{resistence}  Sl:{h-lSL} TRG:{h+LTR}  target_static_pts:{longPPts} exited at {candleHigh}%={cumLongPer}'
                    )
                    break

                elif candleLow < LTSL:
                    if IS_TRSL:
                        # print("2")

                        cumLongPer += round(((candleHigh - resistence) / resistence)*100 ,3 )
                        cumPer +=round(((candleHigh - resistence) / resistence)*100 ,3)
                        cumPerlist.append(cumPer)

                        
                        wins += 1
                        symbolsinlongprofit.append(f"{symbol}=>{((candleHigh - resistence) / resistence)*100}")
                        # print(symbolsinlongprofit)
                        longPPts += round(candleHigh - resistence , 3)

                        print(
                            f'Target/stoploss {symbol}-{date}Profit in candle{candle} LONG signal @ {h}  Sl{LTSL} TRG-{resistence +LTR}  PTSstatic:{round(longPPts,3)} exited at {candleHigh},Cumul%={cumLongPer}'
                        )
                        break
                        
                    
                elif candle == totalCandle:
                    # print("3")

                    print("EOD exit")
                    cumLongPer += ((candleHigh - resistence) / resistence)*100
                    cumPer +=  ((candleHigh - resistence) / resistence)*100 
                    cumPerlist.append(cumPer)
                    symbolsinlongprofit.append(f"{symbol}=>{((candleHigh - resistence) / resistence)*100}")

                    break
 


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
        now = datetime.STRftime(datetime.now(), "%H:%M:%S")
        x = True if now < start else False
    run = True

while run:
    print("\nCurrent time", "   ", now)
    for i in symbols:
        print("\n" + i)
        h,l,data = DFL.data_handling_days(i , tradedate)
        # h, l, data = DFL.offline_data_handling(i, timeFrame)

        place_orders(i, h, l, data)
    print(cumPerlist)
    # plt.plot(cumPerlist)
    # plt.show()       
    plt.legend(fontsize='small')
    plt.show()
    
    print("In sort total %   :", cumSortPer)
    print('long total %   :', cumLongPer)
    print('DRAW total     :', draw)
    print('Total entries  :', wholeEntries)


    now = datetime.strftime(datetime.now(), "%H:%M:%S")
    # run = True if ((now > start) & (now < end)) else False
    run = False

print("symbolsinshortprofit :", symbolsinshortprofit)
print("symbolsinshortloss   :", symbolsinshortloss)
print("symbolsinlongprofit  :", symbolsinlongprofit)
print('symbolsinlongloss    :', symbolsinlongloss)
print('no entries           :', No_entry)
# print('no entries           :', noentrys)    


try:
    print('Probabilityof win    :', wins / (wins + losses) * 100)
except ZeroDivisionError:
    print("zero")







# print('num',number)
            # print(recentHigh)
            # print(number >= recentHigh)
            # if (number > recentHigh):
            #     # its good but not as pd.rollling
            #     IS_TLSL = True
            #     recentHigh = number
            #     print('made HH', recentHigh)
            #     lSL = recentHigh - (recentHigh * .002)
            #     print('LTSL', lSL)





