"""
Needs 
Know to access the all indivudual value and volume 
How to find orb? 30 mins HIGH and LOW ??
how to get current LTP ??
How to CONVERT TO DATES??
HOw to get a range of date and find high and lows??



"""
import datetime

# data variable is a current live data by fyers =>using fyers.quotes(quotes)
data={'s': 'ok', 'd': [{'n': 'NSE:SBIN-EQ', 's': 'ok', 'v': {'ch': -1.3, 'chp': -0.22, 'lp': 595.8, 'spread': 0.15, 'ask': 595.95, 'bid': 595.8, 'open_price': 600.4, 'high_price': 601.85, 'low_price': 595.1, 'prev_close_price': 597.1, 'volume': 1513872, 'short_name': 'SBIN-EQ', 'exchange': 'NSE', 'description': 'NSE:SBIN-EQ', 'original_name': 'NSE:SBIN-EQ', 'symbol': 'NSE:SBIN-EQ', 'fyToken': '10100000003045', 'tt': 1672099200, 'cmd': {'t': 1672113840, 'o': 596.0, 'h': 596.0, 'l': 595.8, 'c': 595.8, 'v': 959, 'tf': '9:34'}}}]} 
# a =list(data)
# print(a[])
# To know data type whuch is DICT
# print(type(data))
# print(data['d'][0]['v']['cmd'])
# z = data['d'][0]['v']['cmd']

# print("open",z['o'])
# print("high",z['h'])
# print("low",z['l'])
# print("close",z['c'])
# print("volume",z['v'])
# print("time",z['tf'])


print("-"*50)

# for i in data.keys():
#         print(i)
#         print(data[i])
#         a=data[i]
#         print(type(a))
#         print(a[0])
#         b=a[0]
#         print(type(b))
#         print(b)
#         print(b[0])
        # for j in i:
        #         print(data[j])

#To list a piece
# print(data.get('s'))
# print(data.get('d'))
print("-"*50)



# You see progress only if a goal and time is there 
#  Get ohlc value babe   => no idea lets split a dict 

# a =data.get('d')
# print(type(a))

listdataD={'d':[{'n': 'NSE:SBIN-EQ',
            's': 'ok',
            'v': {'ch': -1.3, 'chp': -0.22, 'lp': 595.8, 'spread': 0.15, 'ask': 595.95, 'bid': 595.8, 'open_price': 600.4, 'high_price': 601.85, 'low_price': 595.1, 'prev_close_price': 597.1, 'volume': 1513872, 'short_name': 'SBIN-EQ', 'exchange': 'NSE', 'description': 'NSE:SBIN-EQ', 'original_name': 'NSE:SBIN-EQ', 'symbol': 'NSE:SBIN-EQ', 'fyToken': '10100000003045', 'tt': 1672099200, 
                 'cmd': {'t': 1672113840, 'o': 596.0, 'h': 596.0, 'l': 595.8, 'c': 595.8, 'v': 959, 'tf': '9:34'}}}]}

# print(type(listdataD))

# b=a.get('n')
# print(b)

# a = list(data)
# print(a[1])
# for i in a:
#     for j in i:
#         print(j)

# print(a)
# try to loop inside   / but convert to data 
# for i in data.get('d'):
#     print(list(i))













# for i in data:
#     print('i',i)
    
#     for j in i:
#         print('j',j)
        # for k in j:
        #     print("k",k)