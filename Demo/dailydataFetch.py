import login as login
from datetime import datetime
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt
import os





def offline_data_handling(a,b,dataname):
    # srp=pd.read_csv("C:/algoTrading/10_nov_BN_5T.csv")
    # srp=pd.read_csv("C:/algoTrading/26_nov_BN_5T_sort.csv")
    # srp=pd.read_csv("C:/algoTrading/oct_BN_5T.csv")
    # srp=pd.read_csv("C:/algoTrading/13_09_23_BN_5T_long.csv")
    # srp=pd.read_csv("C:/algoTrading/2023.csv")
    srp=pd.read_csv(f"C:/algoTrading/Demo/data/{dataname}.csv")
    # file_path = os.path.join(script_directory, data_folder, 'access_token.txt')

    # print(srp.to_string())
    # high =srp.at[0,"2"] #row , column
    # low  =srp.at[0,"3"]
    # print(srp.head().to_string())
    high = srp.iloc[:10, 3].max()
    low  = srp.iloc[:10, 4].min()
    

    # print(high,low)
    
    srp.columns = ['Index', 'Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume']
    srp["Timestamp"] = pd.to_datetime(srp["Timestamp"], unit="s")
    srp.set_index("Timestamp", inplace=True)
    srp.sort_index(inplace=True)
    srp["date"] = srp.index.date
    # print(srp.loc[start_range : end_range])
    # range = srp.loc[1:5]
    # print(range["2"].max())
    # print(range["3"].min())
    range_size = 6  #30 mins if its a 5mins candle 
    prevCandlerange_size =1
    srp['recentHigh'] = srp['High'].shift(1).rolling(range_size).max()
    srp['recentLow'] = srp['Low'].shift(1).rolling(range_size).min()
    srp['prevHigh'] =srp['High'].shift(1).rolling(prevCandlerange_size).max()
    srp['prevLow'] =srp['Low'].shift(1).rolling(prevCandlerange_size).min()
    srp['dayHigh'] =srp['High'].expanding().max()
    srp['dayLow'] =srp['Low'].expanding().min()

    # print(srp.to_string())
    
 
    # ploting()
    
    print(type(high))
    print(type(low))
    print(type(srp))
    
    # srp.to_string()
    return high, low, srp



def data_handling_days(symbol,date):
    print("hello")
    # date = '2024-01-19'
    timeframe="5"
    # symbol.replace("-","")
    csvname=symbol.replace(":","") +date+timeframe
    script_directory = os.path.dirname(__file__)
    data_folder = 'data'
    file_path = os.path.join(script_directory, data_folder, csvname)
    if not os.path.isfile(f"{file_path}.csv"):

        hist_data = {
            "symbol": symbol,
            "resolution": 5,
            "date_format": 1,
            "range_from": date,
            "range_to": date,
            "cont_flag": "1"
        }
        srp = login.fyers.history(hist_data)
        print(srp)
        # if(srp.s !="ok"):{print(srp)}
        # for excel
        df=pd.DataFrame(srp["candles"])
        # df.to_csv(date+symbol+timeFrame+"T.csv")
        df_reset_index = df.reset_index(drop=True)
        if not os.path.isfile(f"{file_path}.csv"):
        # If the file doesn't exist, create a new one with header
            df_reset_index.to_csv(f"{file_path}.csv", header=True, index=True)
        else:
        # If the file exists, append without header
            df_reset_index.to_csv(f"{file_path}.csv", mode='a', header=False, index=True) 
            # df_reset_index.to_csv(f"{csvname}.csv", mode='a', header=False, index=True)
        # print(srp)
        hl_data = srp["candles"][0]
        high = hl_data[2]
        low = hl_data[3]
    # else:
    #     print("jackaee")
    
    # print("High:", high, "  ", "Low:", low)
        print(type(symbol))
    print(type(date))
    print(type(csvname))
    return offline_data_handling(symbol,date,csvname)



# noo

def data_handling(symbol,timeFrame):
    # date = datetime.today().strftime('%Y-%m-%d')
    # date = '2023-01-01'
    # date1 = '2023-03-31'
    datelist =  ['2023-01-01','2023-04-01','2023-07-01','2023-10-01']
    datelist1 = ['2023-03-31','2023-06-30','2023-09-30','2023-11-30']
    # date =  ['2023-01-01','2023-04-01','2023-07-01']
    # date1 = ['2023-03-31','2023-06-30','2023-09-30']

    for i in range(len(datelist)):
            
        date =datelist[i]
        date1=datelist1[i]
        
        hist_data = {
            "symbol": symbol,
            "resolution": 5,
            "date_format": 1,
            "range_from": date,
            "range_to": date1,
            "cont_flag": "1"
        }
        print(date,date1)
        srp = login.fyers.history(hist_data)
        # print(srp)
        # for excel
        df=pd.DataFrame(srp["candles"])
        # df.to_csv(date+symbol+timeFrame+"T.csv")
        df_reset_index = df.reset_index(drop=True)

        df_reset_index.to_csv("axis1.csv", mode='a', header=False, index=True)
        # print(srp)
        hl_data = srp["candles"][0]
        high = hl_data[2]
        low = hl_data[3]
    
    
    # print("High:", high, "  ", "Low:", low)

    return high, low, srp


#    def ploting():
#         plt.figure(figsize=(10, 6))
#         plt.plot(srp['recentHigh'], marker='o', linestyle='-')
#         plt.plot(srp['recentLow'], marker='p', linestyle='-')
#         plt.title('High_OR Plot')
#         plt.xlabel('Index')
#         plt.ylabel('High_OR Value')
#         plt.grid(True)
#         plt.show()


#  13 -11-23
# def offline_data_handling(start_range:0, end_range):
#     # srp=pd.read_csv("C:/algoTrading/10_nov_BN_5T.csv")
#     srp=pd.read_csv("C:/algoTrading/26_nov_BN_5T_sort.csv")
#     # print(srp.to_string())
#     # high =srp.at[0,"2"] #row , column
#     # low  =srp.at[0,"3"]
#     # print(srp.head().to_string())
#     high = srp.iloc[:10, 3].max()
#     low  = srp.iloc[:10, 4].min()
    

#     # print(high,low)
    
#     srp.columns = ['Index', 'Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume']

#     # print(srp.loc[start_range : end_range])
#     # range = srp.loc[1:5]
#     # print(range["2"].max())
#     # print(range["3"].min())
#     range_size = 6  #30 mins if its a 5mins candle 
#     prevCandlerange_size =1
#     srp['recentHigh'] = srp['High'].shift(1).rolling(range_size).max()
#     srp['recentLow'] = srp['Low'].shift(1).rolling(range_size).min()
#     srp['prevHigh'] =srp['High'].shift(1).rolling(prevCandlerange_size).max()
#     srp['prevLow'] =srp['Low'].shift(1).rolling(prevCandlerange_size).min()
#     srp['dayHigh'] =srp['High'].expanding().max()
#     srp['dayLow'] =srp['Low'].expanding().min()

#     # print(srp.to_string())
    
#     def ploting():
#         plt.figure(figsize=(10, 6))
#         plt.plot(srp['recentHigh'], marker='o', linestyle='-')
#         plt.plot(srp['recentLow'], marker='p', linestyle='-')
#         plt.title('High_OR Plot')
#         plt.xlabel('Index')
#         plt.ylabel('High_OR Value')
#         plt.grid(True)
#         plt.show()
#     # ploting()
    
    
    
#     srp.to_string()
#     return high, low, srp
 
# print(offline_data_handling(1,2))










# 1=open
# 2=high
# 3=low 
# 4=close


def sampleforchart():
    # srp=pd.read_csv("C:/algoTrading/10_nov_BN_5T.csv")
    # srp=pd.read_csv("C:/algoTrading/26_nov_BN_5T_sort.csv")
    # srp=pd.read_csv("C:/algoTrading/oct_BN_5T.csv")
    srp=pd.read_csv("C:/algoTrading/13_09_23_BN_5T_long.csv")
    
    # print(srp.to_string())
    # high =srp.at[0,"2"] #row , column
    # low  =srp.at[0,"3"]
    # print(srp.head().to_string())
    high = srp.iloc[:10, 3].max()
    low  = srp.iloc[:10, 4].min()
    

    # print(high,low)
    
    srp.columns = ['Index', 'Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume']
    srp["Timestamp"] = pd.to_datetime(srp["Timestamp"], unit="s")
    srp.set_index("Timestamp", inplace=True)
    srp.sort_index(inplace=True)
    srp["date"] = srp.index.date
    # print(srp.loc[start_range : end_range])
    # range = srp.loc[1:5]
    # print(range["2"].max())
    # print(range["3"].min())
    range_size = 6  #30 mins if its a 5mins candle 
    prevCandlerange_size =1
    srp['recentHigh'] = srp['High'].shift(1).rolling(range_size).max()
    srp['recentLow'] = srp['Low'].shift(1).rolling(range_size).min()
    srp['prevHigh'] =srp['High'].shift(1).rolling(prevCandlerange_size).max()
    srp['prevLow'] =srp['Low'].shift(1).rolling(prevCandlerange_size).min()
    srp['dayHigh'] =srp['High'].expanding().max()
    srp['dayLow'] =srp['Low'].expanding().min()

    # print(srp.to_string())
    
    
    



    def ploting():
        plt.figure(figsize=(10, 6))
        plt.plot(srp['recentHigh'], marker='o', linestyle='-')
        # plt.plot(srp['recentLow'], marker='p', linestyle='-')
        plt.title('High_OR Plot')
        plt.xlabel('Index')
        plt.ylabel('High_OR Value')
        plt.grid(True)
        plt.show()
    ploting()
    
    
    
    # srp.to_string()
    return high, low, srp



# sampleforchart();