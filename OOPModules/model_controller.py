# importing external libraries
import yfinance as yf

# model/controller (data/brain)
class GetData:
    # constructor method
    def __init__(self, ticker):
        self.ticker = ticker

    # method to obtain the dataset
    def get_data(self):
        stock = yf.Ticker(self.ticker)
        prices_day = stock.history(period="max")
        return prices_day
