import math

def buffer_price(equity_price):
    buffer = 0.001  # 0.1% buffer
    buffer_price = equity_price * (1 + buffer)
    buffer_price_rounded = round(buffer_price + 0.0005, 3)
    buffer_price_rounded = buffer_price_rounded - equity_price
    buffer_price_divisible = round(buffer_price_rounded * 20) / 20
    return buffer_price_divisible

# def buffer_price(equity_price):
#     buffer = 0.001  # 0.1% buffer
#     buffer_price = equity_price * (1 + buffer)
#     buffer_price_rounded = math.ceil(buffer_price * 20) / 20
#     return buffer_price_rounded


# def buffer_price(equity_price):
#     buffer = 0.001  # 0.1% buffer
#     buffer_price = equity_price * (1 + buffer)
#     print(buffer_price)
#     buffer_price_rounded = math.ceil(buffer_price * 20) / 20 
#     buffer_price_rounded = buffer_price_rounded - equity_price
#     return buffer_price_rounded

price = 109004.8767 # current equity price
buffered_price = buffer_price(price)
print("Current Price:", price)
print("Buffered Price:", buffered_price)