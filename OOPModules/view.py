# importing
from model_controller import GetData

# viewing output
stock_1 = GetData("WING")
print(stock_1.get_data())

stock_2 = GetData("MSFD")
print(stock_2.get_data())
