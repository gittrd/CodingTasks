# importing
import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
import yfinance as yf
from model_controller import GetData

# defining test class
class TestDataFrameEqual(unittest.TestCase):
    def test_dataframes_equal(self):
        # df1 to test
        df1 = yf.Ticker("WING")
        df1_ = pd.DataFrame(df1.history(period="max"))

        # Arrange
        my_stock = "WING"  
        # Act
        df2 = GetData(my_stock)
        df2_ = pd.DataFrame(df2.get_data())
        # Assert
        assert_frame_equal(df2_, df1_)

if __name__ == '__main__':
    unittest.main()
