print("you can!! - backtesting")
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
from datetime import datetime, timedelta, date
import pdb
import pandas as pd
import pprint as pp
import calendar



# print(ns.get_nifty50())
# print(ns.get_nifty200())


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
start_date =''
percentageProfit=0
percentageLoss=0



lSL =0
sSL = 0
lTR = 0
sTR = 0
lbuffer = 0
hbuffer = 0
profitAmount=0
lossAmount=0


wins=0
losses=0
draw=0
# symbols = ['NSE:GRASIM-EQ', 'NSE:HDFC-EQ', 'NSE:HDFCBANK-EQ', 'NSE:HDFCLIFE-EQ', 'NSE:HEROMOTOCO-EQ', 'NSE:HINDALCO-EQ', 'NSE:HINDUNILVR-EQ', 'NSE:ICICIBANK-EQ', 'NSE:INDUSINDBK-EQ', 'NSE:INFY-EQ', 'NSE:IOC-EQ', 'NSE:ITC-EQ', 'NSE:JSWSTEEL-EQ', 'NSE:KOTAKBANK-EQ', 'NSE:LT-EQ', 'NSE:M&M-EQ', 'NSE:NTPC-EQ', 'NSE:RELIANCE-EQ', 'NSE:SBILIFE-EQ', 'NSE:SBIN-EQ', 'NSE:SUNPHARMA-EQ', 'NSE:TATACONSUM-EQ', 'NSE:TATAMOTORS-EQ', 'NSE:TATASTEEL-EQ', 'NSE:TCS-EQ', 'NSE:TECHM-EQ', 'NSE:TITAN-EQ', 'NSE:UPL-EQ']

# symbols= ["NSE:ICICIBANK-EQ","NSE:BPCL-EQ","NSE:HCLTECH-EQ",'NSE:INFY-EQ', 'NSE:BHARTIARTL-EQ','NSE:AXISBANK-EQ','NSE:CIPLA-EQ','NSE:HINDALCO-EQ','NSE:LT-EQ','NSE:TATAMOTORS-EQ','NSE:HDFCBANK-EQ','NSE:HINDALCO-EQ', 'NSE:JSWSTEEL-EQ', 'NSE:UPL-EQ']

# symbols= ['NSE:HDFCBANK-EQ']




symbols=['NSE:ASIANPAINT-EQ', 'NSE:AXISBANK-EQ', 'NSE:BAJAJ-AUTO-EQ', 'NSE:BAJAJFINSV-EQ', 'NSE:BAJFINANCE-EQ', 'NSE:BHARTIARTL-EQ', 'NSE:BPCL-EQ', 'NSE:BRITANNIA-EQ', 'NSE:CIPLA-EQ', 'NSE:COALINDIA-EQ', 'NSE:DIVISLAB-EQ', 'NSE:DRREDDY-EQ', 'NSE:EICHERMOT-EQ', 'NSE:GAIL-EQ', 'NSE:GRASIM-EQ', 'NSE:HCLTECH-EQ', 'NSE:HDFC-EQ', 'NSE:HDFCBANK-EQ', 'NSE:HDFCLIFE-EQ', 'NSE:HEROMOTOCO-EQ', 'NSE:HINDALCO-EQ', 'NSE:HINDUNILVR-EQ', 'NSE:ICICIBANK-EQ', 'NSE:INDUSINDBK-EQ', 'NSE:INFY-EQ', 'NSE:IOC-EQ', 'NSE:ITC-EQ', 'NSE:JSWSTEEL-EQ', 'NSE:KOTAKBANK-EQ', 'NSE:LT-EQ', 'NSE:M&M-EQ', 'NSE:MARUTI-EQ', 'NSE:NESTLEIND-EQ', 'NSE:NTPC-EQ', 'NSE:ONGC-EQ', 'NSE:POWERGRID-EQ', 'NSE:RELIANCE-EQ', 'NSE:SBILIFE-EQ', 'NSE:SBIN-EQ', 'NSE:SHREECEM-EQ', 'NSE:SUNPHARMA-EQ', 'NSE:TATAMOTORS-EQ', 'NSE:TATASTEEL-EQ', 'NSE:TCS-EQ', 'NSE:TECHM-EQ', 'NSE:TITAN-EQ', 'NSE:ULTRACEMCO-EQ', 'NSE:UPL-EQ', 'NSE:WIPRO-EQ']

nifty500=['NSE:AARTIIND-EQ', 'NSE:ABBOTINDIA-EQ', 'NSE:ABCAPITAL-EQ', 'NSE:ABFRL-EQ', 'NSE:ACC-EQ', 'NSE:ADANIENT-EQ', 'NSE:ADANIGREEN-EQ', 'NSE:ADANIPORTS-EQ', 'NSE:ADANITRANS-EQ', 'NSE:AJANTPHARM-EQ', 'NSE:ALKEM-EQ', 'NSE:AMARAJABAT-EQ', 'NSE:AMBUJACEM-EQ', 'NSE:APLLTD-EQ', 'NSE:APOLLOHOSP-EQ', 'NSE:APOLLOTYRE-EQ', 'NSE:ASHOKLEY-EQ', 'NSE:ASIANPAINT-EQ', 'NSE:ATGL-EQ', 'NSE:AUBANK-EQ', 'NSE:AUROPHARMA-EQ', 'NSE:AXISBANK-EQ', 'NSE:BAJAJ-AUTO-EQ', 'NSE:BAJAJFINSV-EQ', 'NSE:BAJAJHLDNG-EQ', 'NSE:BAJFINANCE-EQ', 'NSE:BALKRISIND-EQ', 'NSE:BANDHANBNK-EQ', 'NSE:BANKBARODA-EQ', 'NSE:BANKINDIA-EQ', 'NSE:BATAINDIA-EQ', 'NSE:BBTC-EQ', 'NSE:BEL-EQ', 'NSE:BERGEPAINT-EQ', 'NSE:BHARATFORG-EQ', 'NSE:BHARTIARTL-EQ', 'NSE:BHEL-EQ', 'NSE:BIOCON-EQ', 'NSE:BOSCHLTD-EQ', 'NSE:BPCL-EQ', 'NSE:BRITANNIA-EQ', 'NSE:CADILAHC-EQ', 'NSE:CANBK-EQ', 'NSE:CASTROLIND-EQ', 'NSE:CESC-EQ', 'NSE:CHOLAFIN-EQ', 'NSE:CIPLA-EQ', 'NSE:COALINDIA-EQ', 'NSE:COFORGE-EQ', 'NSE:COLPAL-EQ', 'NSE:CONCOR-EQ', 'NSE:COROMANDEL-EQ', 'NSE:CROMPTON-EQ', 'NSE:CUB-EQ', 'NSE:CUMMINSIND-EQ', 'NSE:DABUR-EQ', 'NSE:DALBHARAT-EQ', 'NSE:DEEPAKNTR-EQ', 'NSE:DHANI-EQ', 'NSE:DIVISLAB-EQ', 'NSE:DIXON-EQ', 'NSE:DLF-EQ', 'NSE:DMART-EQ', 'NSE:DRREDDY-EQ', 'NSE:EICHERMOT-EQ', 'NSE:EMAMILTD-EQ', 'NSE:ENDURANCE-EQ', 'NSE:ESCORTS-EQ', 'NSE:EXIDEIND-EQ', 'NSE:FEDERALBNK-EQ', 'NSE:FORTIS-EQ', 'NSE:GAIL-EQ', 'NSE:GLENMARK-EQ', 'NSE:GMRINFRA-EQ', 'NSE:GODREJAGRO-EQ', 'NSE:GODREJCP-EQ', 'NSE:GODREJIND-EQ', 'NSE:GODREJPROP-EQ', 'NSE:GRASIM-EQ', 'NSE:GSPL-EQ', 'NSE:GUJGASLTD-EQ', 'NSE:HAL-EQ', 'NSE:HAVELLS-EQ', 'NSE:HCLTECH-EQ', 'NSE:HDFC-EQ', 'NSE:HDFCAMC-EQ', 'NSE:HDFCBANK-EQ', 'NSE:HDFCLIFE-EQ', 'NSE:HEROMOTOCO-EQ', 'NSE:HINDALCO-EQ', 'NSE:HINDPETRO-EQ', 'NSE:HINDUNILVR-EQ', 'NSE:HINDZINC-EQ', 'NSE:IBULHSGFIN-EQ', 'NSE:ICICIBANK-EQ', 'NSE:ICICIGI-EQ', 'NSE:ICICIPRULI-EQ', 'NSE:IDEA-EQ', 'NSE:IDFCFIRSTB-EQ', 'NSE:IGL-EQ', 'NSE:INDHOTEL-EQ', 'NSE:INDIAMART-EQ', 'NSE:INDIGO-EQ', 'NSE:INDUSINDBK-EQ', 'NSE:INDUSTOWER-EQ', 'NSE:INFY-EQ', 'NSE:IOC-EQ', 'NSE:IPCALAB-EQ', 'NSE:IRCTC-EQ', 'NSE:ISEC-EQ', 'NSE:ITC-EQ', 'NSE:JINDALSTEL-EQ', 'NSE:JSWENERGY-EQ', 'NSE:JSWSTEEL-EQ', 'NSE:JUBLFOOD-EQ', 'NSE:KOTAKBANK-EQ', 'NSE:L&TFH-EQ', 'NSE:LALPATHLAB-EQ', 'NSE:LAURUSLABS-EQ', 'NSE:LICHSGFIN-EQ', 'NSE:LT-EQ', 'NSE:LTI-EQ', 'NSE:LTTS-EQ', 'NSE:LUPIN-EQ', 'NSE:M&M-EQ', 'NSE:M&MFIN-EQ', 'NSE:MANAPPURAM-EQ', 'NSE:MARICO-EQ', 'NSE:MARUTI-EQ', 'NSE:MCDOWELL-N-EQ', 'NSE:MFSL-EQ', 'NSE:MGL-EQ', 'NSE:MINDTREE-EQ', 'NSE:MOTHERSUMI-EQ', 'NSE:MPHASIS-EQ', 'NSE:MRF-EQ', 'NSE:MUTHOOTFIN-EQ', 'NSE:NAM-INDIA-EQ', 'NSE:NATCOPHARM-EQ', 'NSE:NAUKRI-EQ', 'NSE:NAVINFLUOR-EQ', 'NSE:NESTLEIND-EQ', 'NSE:NMDC-EQ', 'NSE:NTPC-EQ', 'NSE:OBEROIRLTY-EQ', 'NSE:OIL-EQ', 'NSE:ONGC-EQ', 'NSE:PAGEIND-EQ', 'NSE:PEL-EQ', 'NSE:PETRONET-EQ', 'NSE:PFC-EQ', 'NSE:PFIZER-EQ', 'NSE:PGHH-EQ', 'NSE:PIDILITIND-EQ', 'NSE:PIIND-EQ', 'NSE:PNB-EQ', 'NSE:POLYCAB-EQ', 'NSE:POWERGRID-EQ', 'NSE:PRESTIGE-EQ', 'NSE:RAMCOCEM-EQ', 'NSE:RBLBANK-EQ', 'NSE:RECLTD-EQ', 'NSE:RELIANCE-EQ', 'NSE:SAIL-EQ', 'NSE:SANOFI-EQ', 'NSE:SBICARD-EQ', 'NSE:SBILIFE-EQ', 'NSE:SBIN-EQ', 'NSE:SHREECEM-EQ', 'NSE:SIEMENS-EQ', 'NSE:SRF-EQ', 'NSE:SRTRANSFIN-EQ', 'NSE:SUNPHARMA-EQ', 'NSE:SUNTV-EQ', 'NSE:SYNGENE-EQ', 'NSE:TATACHEM-EQ', 'NSE:TATACONSUM-EQ', 'NSE:TATAELXSI-EQ', 'NSE:TATAMOTORS-EQ', 'NSE:TATAPOWER-EQ', 'NSE:TATASTEEL-EQ', 'NSE:TCS-EQ', 'NSE:TECHM-EQ', 'NSE:TITAN-EQ', 'NSE:TORNTPHARM-EQ', 'NSE:TORNTPOWER-EQ', 'NSE:TRENT-EQ', 'NSE:TVSMOTOR-EQ', 'NSE:UBL-EQ', 'NSE:ULTRACEMCO-EQ', 'NSE:UNIONBANK-EQ', 'NSE:UPL-EQ', 'NSE:VBL-EQ', 'NSE:VEDL-EQ', 'NSE:VGUARD-EQ', 'NSE:VOLTAS-EQ', 'NSE:WHIRLPOOL-EQ', 'NSE:WIPRO-EQ', 'NSE:YESBANK-EQ', 'NSE:ZEEL-EQ']

highprobability=['NSE:ASIANPAINT-EQ', 'NSE:BAJAJ-AUTO-EQ', 'NSE:BAJAJFINSV-EQ', 'NSE:COALINDIA-EQ', 'NSE:EICHERMOT-EQ', 'NSE:HDFC-EQ', 'NSE:HDFCBANK-EQ', 'NSE:HDFCLIFE-EQ', 'NSE:HINDUNILVR-EQ', 'NSE:ICICIBANK-EQ', 'NSE:INDUSINDBK-EQ', 'NSE:INFY-EQ', 'NSE:JSWSTEEL-EQ', 'NSE:M&M-EQNSE:TCS-EQ', 'NSE:MARUTI-EQ', 'NSE:POWERGRID-EQ', 'NSE:RELIANCE-EQ', 'NSE:SBIN-EQ', 'NSE:SUNPHARMA-EQ', 'NSE:TATAMOTORS-EQ', 'NSE:WIPRO-EQ']
janhighproba=['NSE:ASIANPAINT-EQ','NSE:HDFC-EQ','NSE:HDFCBANK-EQ','NSE:EICHERMOT-EQ','NSE:COALINDIA-EQ','NSE:INDUSINDBK-EQ','NSE:TATAMOTORS-EQ','NSE:SBIN-EQ','NSE:ICICIBANK-EQ','NSE:MARUTI-EQ','NSE:BAJAJFINSV-EQ','NSE:HINDUNILVR-EQ','NSE:JSWSTEEL-EQ','NSE:HDFCLIFE-EQ','NSE:M&M-EQ','NSE:INFY-EQ','NSE:BAJAJ-AUTO-EQ','NSE:BHARTIARTL-EQ','NSE:IOC-EQ','NSE:KOTAKBANK-EQ','NSE:POWERGRID-EQ','NSE:RELIANCE-EQ','NSE:WIPRO-EQ']

symbols=janhighproba
# symbols=['NSE:NIFTY50-INDEX']
# 'NSE:AXISBANK-EQ'
symbols=['NSE:AXISBANK-EQ']
def data_handling(symbol,start_date,end_date):
    # The drawback here is =>I can easily get 30 mins or 60 mins H&L but 31 or 61 mins is hard so here a PANDAS CAME TO PLAY WITHOUT ALSO POSSIBLE using srt[0:31] and so on may be lol
    
    
        
    # print('what is here ',symbol ,'date is =>',start_date)
    hist_data = {
        "symbol": symbol,
        "resolution": "60",
        "date_format": 1,
        "range_from": start_date,
        "range_to": end_date,
        "cont_flag": "1"
    }
    srp = login.fyers.history(hist_data)
    # print(date)
    # print(srp)
    hl_data = srp["candles"][0]
    high = hl_data[2]
    low = hl_data[3]
    
    # print("High:", high, "  ", "Low:", low)
    return high, low, srp

        
def range_handling(symbol='NSE:ASIANPAINT-EQ',start_date='2023-02-17',end_date= '2023-02-17'):
    # The drawback here is =>I can easily get 30 mins or 60 mins H&L but 31 or 61 mins is hard so here a PANDAS CAME TO PLAY WITHOUT ALSO POSSIBLE using srt[0:31] and so on may be lol
    
    daysHigh =[]
    daysLow = []  
    # print('what is here ',symbol ,'date is =>',start_date)
    hist_data = {
        "symbol": symbol,
        "resolution": "30",
        "date_format": 1,
        "range_from": start_date,
        "range_to": end_date,
        "cont_flag": "1"
    }
   
    
    records = login.fyers.history(hist_data)
    # print(records)
    """Main dataframe"""                
    df = pd.DataFrame(records)
    # print(df)
    """Separates the opening range dataframe"""
    ord = 7 # opening range duration  5mins candle 7 #start from 1
    ordf = (df[0:ord]) # opening range dataframe
    for i in range(ord):
        # JUST READ 30 MINS RANGE CANDLE IN A PANDA DATATYPES 
        daysHigh.append(ordf['candles'][i][2])
        daysLow.append(ordf['candles'][i][3])
    
    def ltpfinder():
        ltpf = (df[ord:])
        currentHigh = ltpf['candles'][i][2]
        currentLow = ltpf['candles'][i][3]   
        print(currentHigh)             
        print(currentLow)             


    """These below are the opening range (High and low) for the day. """
    orHigh =max(daysHigh)
    orLow = min(daysLow)
    # print(f'days high=> {orHigh} days low=>{orLow}')

    # print(f'day 30 range high {orHigh} and low{orLow}')

    daysHigh.clear()
    daysLow.clear()
    # print()

    """Separates the post-opening range dataframe"""
    # print(adf.iloc)
    return orHigh, orLow, records      
    
        
# range_handling()



def place_orders(symbol, h, l, day30M):
    
    lSL = round(h * .003)
    sSL = round(l * .003)
    lTR = round(h * .006)
    sTR = round(l * .006)
    lbuffer = round( (l * 0.001))
    hbuffer = round( (h * 0.001))
    profitAmount=600
    lossAmount=100
    long = False
    short = False
    global loss
    global profit
    global wholeEntries 
    global percentageProfit
    global percentageLoss
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
        # print(high)
       

        if traded != True:
            # + hbuff and candle < 4
            if high > (h + hbuffer) and candle < 9:
                
                # symbols.remove(symbol)
                # print(f'Long in {symbol} at {start_date}' )
                # with open('trades.txt','a') as Entrysctipt:
                #     Entrysctipt.write("'"+symbol+"'"+',')
                    
                traded = True
                long = True
                wholeEntries +=1
                continue
            elif low < (l - lbuffer) and candle < 9:
                # symbols.remove(symbol)

                # - lbuff and candle< 4
                # print(f"Sort in {symbol} at {start_date}")
            
                # print(f'{symbol}Selling at{low} with SL__ TRG__ ')
                wholeEntries +=1
                traded = True
                short = True
                continue
            # elif candle > 6:
            # #which helps in avoiding late entries
            #     break
            else:
                pass
                # print(f'range Bound in candle {candle}')
        elif short == True:

            if high > l + sSL:
                losses +=1

                percentageLoss +=.10
                loss += lossAmount
                symbolsinshortloss.append(symbol + str(start_date))
                # print(
                #     f'{symbol}Loss in candle:{candle} SORTING at{l}  Sl{l+sSL} TRG{l-sTR}'
                # )

                break
            elif low < l - sTR:
                # print(sTR)
                wins+=1
                percentageProfit +=.60
                profit += profitAmount
                symbolsinshortprofit.append(symbol +str(start_date))

                # print(
                #     f'{symbol}Profit in candle:{candle} SORTING at{l} Sl{l+sSL} TRG{l-sTR} '
                # )
                break
            
            elif candle == totalCandle:
                draw+=1
                print("CLOSED AT EOD Short")
                break
            
        elif long == True:
            if high > h + lTR:
                wins+=1
                percentageProfit +=.60
                profit += profitAmount
                symbolsinlongprofit.append(symbol + str(start_date))
                # print(symbolsinlongprofit)
                # print(
                #     f'{symbol}Profit in candle{candle},LONG signal @ {h}  Sl{h-lSL} TRG{h+lTR}  '
                # )
                break
            
            elif low < h - lSL:
                losses += 1
                percentageLoss +=.10
                loss += lossAmount
                symbolsinlongloss.append(symbol + str(start_date))
                print(
                    f'{symbol}Loss in candle{candle} LONG signal at{h} entry{high} Sl{h-lSL} TRG{h+lTR} '
                )

                break
            elif candle == totalCandle:
                # this works onlt EOD
                draw +=1
                print("EXITED WITH SQUARE OFF Long EOD")
                break

    # 13 30mins candle in a day
    # print("VAR:",var)
    ltp = var[0]

    


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




start = time.perf_counter()

stockyear = 2022
startMonth = 1
endMonth = 12

SDATE=1
EDATE=23

startMonthName = calendar.month_name[startMonth]
endMonthName = calendar.month_name[endMonth]

for script in symbols:
    # lSL=0
    # sSL=0
    # wins=0
    # losses=0
    # draw=0
    # loss =0
    # profit=0
    # wholeEntries =0
    # percentageProfit=0
    # percentageLoss=0
    # symbolsinlongprofit = []
    # symbolsinlongloss = []
    # symbolsinshortloss = []
    # symbolsinshortprofit = []

    for stockmonth in range(startMonth,endMonth+1):
        time.sleep(1)  #use if a big run only
        for stockday in range(SDATE,EDATE): 
            try:
                start_date = date(stockyear,stockmonth, stockday)
                end_date = date(stockyear,stockmonth, stockday)

                # print("\nCurrent time", "   ", now)
                
                i=script
                print("\n" + i)
                h,l,day30M = data_handling(i,start_date,end_date)
                # h,l,day30M = range_handling(i,start_date,end_date)

                place_orders(i, h, l, day30M)
                print(start_date)
                
            except  :
                # print()
                print(f'Holiday {start_date}')
                pass
        
    # print('symbol:',symbols)
print("profit total", profit)
print('loss total', loss)
print('DRAWS total', draw)

print('percentageProfit' ,percentageProfit)

print('percentageLoss' ,percentageLoss)

print('Total entries',wholeEntries)
# print('Brokerages $5:',wholeEntries * 5)
# print('AfterBrokerages:',profit - loss -(wholeEntries * 5))
print("symbolsinshortprofit", symbolsinshortprofit)
print("symbolsinshortloss", symbolsinshortloss)
print("symbolsinlongprofit", symbolsinlongprofit)
print('symbolsinlongloss', symbolsinlongloss)
print('/n')
try:
    probabilitys=wins / (wins+losses)*100
    print('Probabilyty of winns',wins / (wins+losses)*100)
except ZeroDivisionError:
    print('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFtocalculate peob')
    probabilitys=0
    pass
# print('draw',draw)

    end = time.perf_counter()
    ms = end-start 
    print(f"Elapsed {ms}  secs.")
    # try:
        
    #     with open('monthOfJan.csv', 'a') as csvfile:
                
    #         FieldName = [
    #             'Name','totalEntries','risk','reward','buffer', 'Profit', 'Loss', 'PercentageProfit', 'PercentageLoss','Win','losses','probability'
    #         ]
    #         theWritter = csv.DictWriter(csvfile, fieldnames=FieldName)
    #         theWritter.writeheader()
    #         theWritter.writerow({
    #             'Name':i,
    #             'totalEntries':wholeEntries,
    #             'risk':lSL,
    #             'reward':lTR,
    #             'buffer':hbuffer,
    #             'Profit':profit, 
    #             'Loss':loss,
    #             'PercentageProfit':percentageProfit,
    #             'PercentageLoss':percentageLoss,
    #             'Win':wins,
    #             'losses':losses,
    #             'probability':'=SUM(J3/(J3+K3)*100)'
    #         })
    # except :
    #      pass




# for stockmonth in range(startMonth,endMonth+1):
#     for stockday in range(1,29): 
#         try:
#             start_date = date(stockyear,stockmonth, stockday)
#             end_date = date(stockyear,stockmonth, stockday)

#             # print("\nCurrent time", "   ", now)
            
#             for i in symbols:
#                 print("\n" + i)
#                 h,l,day30M = data_handling(i,start_date,end_date)
#                 place_orders(i, h, l, day30M)
#                 print(start_date)
            
#         except :
            
#             print('Holiday {start_date}')
#             pass
        
   
#     print("profit total", profit)
#     print('loss total', loss)
#     print('percentageProfit' ,percentageProfit)

#     print('percentageLoss' ,percentageLoss)

#     print('Total entries',wholeEntries)
#     print('Brokerages $5:',wholeEntries * 5)
#     print('AfterBrokerages:',profit - loss -(wholeEntries * 5))

    # print("Total$:",profit - loss)
    # print(symbols)
    # time.sleep(30)

    

































# print("LTP:", ltp)
    # if ltp>h:
    #     print("Placing buy market cover order!")
    # elif ltp<l:
    #     print("Placing sell market cover order!")
    # else:
    #     print("Price between Opening Range High and Low!")