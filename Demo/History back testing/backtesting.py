
# @143 line to make a last loop to execute 

print("you can!!")
print(
    'Loot of scripts are found there but all are not good for a intraday ORB strategy right res lets choose a best ones '
)
# import sys
import sys
sys.path.insert(0, '..')
sys.path.append("C:/algoTrading/Demo")
import login as login
from datetime import datetime
import time
import os
import time
import json
from niftystocks import ns
import csv

symbols= ['NSE:RELIANCE-EQ']
true = True
loss = 0
profit = 0
symbolsinlongprofit = []
symbolsinlongloss = []
symbolsinshortloss = []
symbolsinshortprofit = []
high = []
wholeEntries=0


print("LOGGED-IN")



#! python

from datetime import datetime, timedelta, date
import pdb
import pandas as pd
import pprint as pp
import calendar

"""Trade portfolio"""
tPF = {
    738561:'RELIANCE',
    
}

"""Set the period for backtesting. """

stockyear = 2022
startMonth = 11
endMonth = 12

startMonthName = calendar.month_name[startMonth]
endMonthName = calendar.month_name[endMonth]

"""MTA Switch: Allows to change between single trade per day and multiple trades per day.
if mta = 0 > Program will perform as many transactions as it can for one day before moving on.
if mta = 1 > Program will only perform 1 transaction for the day and move to the next day. 
in the code below 'trade' will be set as MTA.
"""
mta = 1  

"""This is the main part of the code. It will iterate through a number of stocks, for 12 months, across every single day of the month for one minute intervals."""
for stockToken, stockName in tPF.items():
    print("Calculating for "+stockName+" ...")
    
    percentchange = []
    
    for stockmonth in range(startMonth,endMonth+1):
        daysHigh=[]
        daysLow=[]
        for stockday in range(2): 
            try:
                end_date = date(stockyear,stockmonth, stockday)
                start_date = date(stockyear,stockmonth, stockday)
                interval = 'minute' 
                start_date =  '2023-02-17'
                end_date =  '2023-02-17'

                # print(start_date)
                hist_data = {
                        "symbol": 'NSE:ASIANPAINT-EQ',
                        "resolution": "5",
                        "date_format": 1,
                        "range_from": start_date,
                        "range_to": end_date,
                        "cont_flag": "1"
                    }
                records = login.fyers.history(hist_data)
                # print(records)
                # records = kite.historical_data(stockToken, start_date, end_date, interval)
                
                """Main dataframe"""                
                df = pd.DataFrame(records)
                print(df)
                

                """Separates the opening range dataframe"""
                ord = 7 # opening range duration  5mins candle 7
                calrange = 10 - ord # period post opening range    I HAVE NO IDEA

                # calrange = 375 - ord # period post opening range    I HAVE NO IDEA
                ordf = (df[0:ord]) # opening range dataframe
                for i in range(ord):
                    # JUST READ 30 MINS RANGE CANDLE IN A PANDA DATATYPES 
                    # print(ordf['candles'][i][2])
                    daysHigh.append(ordf['candles'][i][2])
                    daysLow.append(ordf['candles'][i][3])
               
                # print(records)
                # for k in range(ord,74):
                #     # print(j)
                #     # print('in h&l of current')
                #     ltpf = df
                #     # print(ltpf['candles'][k])
                #     currentHigh = ltpf['candles'][k][2]
                #     # print('CURRENT HIGHS',currentHigh)             
                #     currentLow = ltpf['candles'][k][3]   
                #     # print(currentHigh)             
                #     # print(currentLow)



                def ltpfinder():
                    ltpf = (df[ord:])
                    currentHigh = ltpf['candles'][i][2]
                    currentLow = ltpf['candles'][i][3]   
                    print(currentHigh)             
                    print(currentLow)             
 
                # ltpfinder()
                # daysHigh.append(ordf['candles'][1][2])
                # daysLow.append(ordf['candles'][1][3])

                # print(daysLow)

                """These below are the opening range (High and low) for the day. """
                orHigh =max(daysHigh)
                orLow = min(daysLow)
                print(f'days high=> {orHigh} days low=>{orLow}')

                # print()
                print(f'day 30 range high {orHigh} and low{orLow}')

                daysHigh.clear()
                daysLow.clear()
                # print()
                

                """Separates the post-opening range dataframe"""
                adf = df[ord:] 
                # print(adf.iloc)
                """Profit and stoploss targets"""
                profitTarget = 0.5
                pt = profitTarget/100

                stoplossTarget = 0.25
                slt = stoplossTarget/100


                """pos, trade and tradetype are switches.They have been described below."""
                pos = 0 # Used to check if an exit transaction is needed. 
                num = 0 # counter which allows iteration through every minute of the day. 
                trade = 0 # Used for switching between single and multiple trades per day 
                tradeType = 0 # Used for switching between 1 - Buy transaction(BT), 2 - Sell transaction, 0 - no transaction.
               
                # ltp = adf.iloc[[0,2]][1]
                # print('dkfhsjfhdskjfjsdfdskhh')
                # print(adf)
                # print(ltp)
                
                """The main logic: it checks if the last traded price has crossed above or below the opening range upper or lower limit."""
                for x in range(calrange):
                    print('loop =>')
                    # print('loop')
                    # print('loop')
                    # print('loop')
                    # print('loop')
                    # print('loop')


                    # ltp = adf.iloc[x,4]
                    for k in range(ord,74):
                        # print(j)
                        # print('in h&l of current')
                        ltpf = df
                        # print(ltpf['candles'][k])
                        currentHigh = ltpf['candles'][k][2]
                        # print('CURRENT HIGHS',currentHigh)             
                        currentLow = ltpf['candles'][k][3] 
                        close = ltpf['candles'][k][4]
                        # print(currentHigh)             
                        # print(currentLow)

                        ltp = close
                        # print(adf.iloc[1])
                        if pos == 0 and trade <1:
                            if ltp > orHigh:
                                print('\nOR upside breakout.')
                                if (pos == 0):
                                    bp = ltp
                                    pos = 1
                                    tradeType = 1
                                    print('BT: Buying now at time: '+ str(adf.iloc[x,0])+' @ '+str(bp))
                            elif ltp < orLow:
                                print('\nOR downside breakout.')
                                if (pos == 0):
                                    sp = ltp
                                    pos = 1
                                    tradeType = 2
                                    print('ST: Selling now at time: '+ str(adf.iloc[x,0])+' @ '+str(sp))


                            """After entering an active position (either buy or sell), the program will check for 3 things:
                            - whether the profit target is met
                            - whether the stoploss target is met
                            - whether it is the penultimate minute of the day's trading session
                            If any of these 3 criterion are met, active position will be reversed at the closing price. These 3 criterion have been written separately for the buy and sell positions. """

                        # BuyTran: Stoploss target met - sell 
                        elif (tradeType == 1 and ltp <= (bp*(1-slt)) and pos == 1 and trade<1 ):
                            pos = 0
                            sp = ltp
                            # print('BT: Stop loss sale now at time: '+ str(adf.iloc[x,0])+ ' @ '+ str(sp))
                            pc = (sp/bp-1)*100
                            trade = mta
                            percentchange.append(pc)
                            
                        # BuyTran: Last minute of the day  - sell
                        elif (tradeType == 1 and num==calrange-1 and pos == 1):
                            pos = 0
                            sp = ltp
                            # print('BT: Last trade sale now at time: '+ str(adf.iloc[x,0])+ ' @ '+ str(sp))
                            pc = (sp/bp-1)*100
                            trade = mta
                            percentchange.append(pc)

                        # BuyTran: Profit target - sell
                        elif (tradeType == 1 and pos == 1 and trade<1):
                            if ltp > (bp*(1+pt)):
                                sp = ltp
                                pos = 0
                                # print('BT: Profit sale now at time: '+ str(adf.iloc[x,0]) + ' @ '+ str(sp))
                                pc = (sp/bp-1)*100
                                percentchange.append(pc)
                                trade = mta


                        # SellTran Stoploss target met - buy 
                        elif (tradeType == 2 and ltp >= (sp*(1+slt)) and pos == 1 and trade<1):
                            pos = 0
                            bp = ltp
                            # print('ST: Stop loss purchase now at time: '+ str(adf.iloc[x,0])+ ' @ '+ str(bp))
                            pc = (sp/bp-1)*100
                            trade = mta
                            percentchange.append(pc)
                            
                        # SellTran: Last minute of the day - buy
                        elif (tradeType == 2 and num==calrange-1 and pos == 1):
                            pos = 0
                            bp = ltp
                            # print('ST: Last trade purchase now at time: '+ str(adf.iloc[x,0])+ ' @ '+ str(bp))
                            pc = (sp/bp-1)*100
                            trade = mta
                            percentchange.append(pc)
                            
                        # SellTran: Profit target met - buy
                        elif (tradeType == 2 and pos == 1 and trade<1):
                            if ltp < (sp*(1-pt)):
                                bp = ltp
                                pos = 0
                                # print('ST: Profit purchase now at time: '+ str(adf.iloc[x,0]) + ' @ '+ str(bp))
                                pc = (sp/bp-1)*100
                                percentchange.append(pc)
                                trade = mta
                        num += 1
            
            except:
                pass
    finalReturn = (round(sum(percentchange), 2))
    print()
    print("Total Return for "+ stockName+ " for period "+startMonthName[:3]+"-"+endMonthName[:3]+" "+str(stockyear)+":")
    print(str(finalReturn)+"% across "+str(len(percentchange))+" trades.")
    print()
    print()
    



























# symbols= ['NSE:JSWSTEEL-EQ']
# # OHLC

# def data_handling(symbol):
#     date = '2023-01-20'
#     date = datetime.today().strftime('%Y-%m-%d')
#     date = '2023-01-20'

#     hist_data = {
#         "symbol": symbol,
#         "resolution": "30",
#         "date_format": 1,
#         "range_from": date,
#         "range_to": date,
#         "cont_flag": "1"
#     }
#     srp = login.fyers.history(hist_data)
#     # print(date)
#     hl_data = srp["candles"][0]
#     high = hl_data[2]
#     low = hl_data[3]
#     # print("High:", high, "  ", "Low:", low)
#     return high, low, srp


# # data_handling("NSE:SBIN-EQ")


# def place_orders(symbol, h, l, day30M):
#     lSL = round(h * .003)
#     sSL = round(l * .003)
#     lTR = round(h * .006)
#     sTR = round(l * .006)
#     profitAmount=200
#     lossAmount=100
#     long = False
#     short = False
#     global loss
#     global profit
#     global wholeEntries 
#     traded = False
#     candle = 0

#     # var = login.fyers.quotes(df)["d"] #Hope this for live market
#     # print('How my LTP finded',var)
#     var = day30M['candles']  # here wwe need to loop all the 30 mis candle to find the entry and exit to calculatr profit aand loss
#     totalCandle = len(var)
#     for i in var:

#         candle += 1  #with variable candle u can diable the afternoon trades or change range
#         # print('Current candle:',candle)
#         opening = i[1]
#         high = i[2]
#         low = i[3]
#         lbuff = l * .001
#         hbuff = h * .001
#         close = [4]
#         volume = [5]

#         # long=False
#         # short=False
#         # traded=False
#         # print(i ,'high=',high , 'low',low)
#         print()
#         def trade():
#             pass

#         if traded != True:
#             # + hbuff and candle < 4
#             if high > h :
#                 # symbols.remove(symbol)
#                 # print('long')
#                 # with open('trades.txt','a') as Entrysctipt:
#                 #     Entrysctipt.write("'"+symbol+"'"+',')
                    
#                 traded = True
#                 long = True
#                 wholeEntries +=1
#                 continue
#             elif low < l :
#                 # symbols.remove(symbol)

#                 # - lbuff and candle< 4
#                 # print("sort")
#                 # with open('trades.txt','a') as Entrysctipt:
#                 #     Entrysctipt.write(symbol+',')
#                 # print(f'{symbol}Selling at{low} with SL__ TRG__ ')
#                 wholeEntries +=1
#                 traded = True
#                 short = true
#                 continue
#             # elif candle > 6:
#             # #which helps in avoiding late entries
#             #     break
#             else:
#                 pass
#                 # print(f'range Bound in candle {candle}')
#         elif short == True:

#             if high > l + sSL:

#                 loss += lossAmount
#                 symbolsinshortloss.append(symbol)
#                 print(
#                     f'{symbol}Loss in candle:{candle} SORTING at{l}  Sl{l+sSL} TRG{l-sTR}'
#                 )

#                 break
#             elif low < l - sTR:
#                 # print(sTR)
                   

#                 profit += profitAmount
#                 symbolsinshortprofit.append(symbol)

#                 print(
#                     f'{symbol}Profit in candle:{candle} SORTING at{l} Sl{l+sSL} TRG{l-sTR} '
#                 )
#                 break
#             elif candle == totalCandle:
#                 print("CLOSED AT EOD Short")
#                 break
#         elif long == True:
#             if high > h + lTR:
                

#                 profit += profitAmount
#                 symbolsinlongprofit.append(symbol)
#                 # print(symbolsinlongprofit)
#                 print(
#                     f'{symbol}Profit in candle{candle},LONG signal @ {h}  Sl{h-lSL} TRG{h+lTR}  '
#                 )
#                 break
#             elif low < h - lSL:
                
#                 loss += lossAmount
#                 symbolsinlongloss.append(symbol)
#                 print(
#                     f'{symbol}Loss in candle{candle} LONG signal at{h} entry{high} Sl{h-lSL} TRG{h+lTR} '
#                 )

#                 break
#             elif candle == totalCandle:
#                 # this works onlt EOD
#                 # print("EXITED WITH SQUARE OFF Long EOD")
#                 break

#     # 13 30mins candle in a day
#     # print("VAR:",var)
#     ltp = var[0]

#     # print("LTP:", ltp)
#     # if ltp>h:
#     #     print("Placing buy market cover order!")
#     # elif ltp<l:
#     #     print("Placing sell market cover order!")
#     # else:
#     #     print("Price between Opening Range High and Low!")


# start = "09:45:00"
# end = "15:00:00"
# now = datetime.strftime(datetime.now(), "%H:%M:%S")

# # Check is it need to run a code in range of 9:40 - 3:30
# run = True if ((now > start) & (now < end)) else False

# # next line i aded back test
# run = True

# if run == False and now < start:
#     x = True
#     while x:
#         print("Waiting for market to open")
#         time.sleep(60)
#         now = datetime.strftime(datetime.now(), "%H:%M:%S")
#         x = True if now < start else False
#     run = True

# while run:
#     print("\nCurrent time", "   ", now)
#     for i in symbols:
#         # print("\n" + i)
#         h,l,day30M = data_handling(i)
#         place_orders(i, h, l, day30M)
#     print("profit total", profit)
#     print('loss total', loss)

#     print('Total entries',wholeEntries)
#     print('Brokerages $5:',wholeEntries * 5)
#     print('AfterBrokerages:',profit - loss -(wholeEntries * 5))
#     # print("Total$:",profit - loss)
#     # print(symbols)
#     # time.sleep(30)

#     now = datetime.strftime(datetime.now(), "%H:%M:%S")
#     run = True if ((now > start) & (now < end)) else False

# print("symbolsinshortprofit", symbolsinshortprofit)
# print("symbolsinshortloss", symbolsinshortloss)
# print("symbolsinlongprofit", symbolsinlongprofit)
# print('symbolsinlongloss', symbolsinlongloss)

# if now > end:
#     print("\nMarket Closed!")

