"""
Writing unit tests for one of the prior practical tasks.
Using Recursion Task 13 below as my implementation.
"""

# importing
import unittest
from my_module import largest_number

# defining a class for unit testing
class LargestNum(unittest.TestCase):
    
    # testing with multiple values
    def test_find_largest_num(self):
        # Arrange
        my_list = [1, 2, 5, 100, 1000, 35]
        # Act
        my_result = largest_number(my_list)
        # Assert
        self.assertEqual(my_result, 1000)

    # testing with one value
    def test_find_largest_num_two(self):
        # Arrange
        my_list = [1]
        # Act
        my_result = largest_number(my_list)
        # Assert
        self.assertEqual(my_result, 1)

    # testing with negative value
    def test_find_largest_num_three(self):
        # Arrange
        my_list = [-1]
        # Act
        my_result = largest_number(my_list)
        # Assert
        self.assertEqual(my_result, -1)

if __name__ == '__main__':
    unittest.main()
