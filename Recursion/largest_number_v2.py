"""
Follow these steps:
● In a file called largest_number.py, create a function that returns the
largest number in a list of integers taken as an argument. The problem
needs to be solved recursively without using loops.
Examples of input and output:
largest_number([1, 4, 5, 3])
=> 5
largest_number([3, 1, 6, 8, 2, 4, 5])
=> 8
"""

def largest_number(array):
    if len(array) == 1:
        return array[0]
    else:
        lm = largest_number(array[1:])

        if lm > array[0]:
            return lm
        else:
            return array[0]

def test_largest_number_1():
    print(largest_number([1, 4, 5, 3]))

def test_largest_number_2():
    print(largest_number([3, 1, 6, 8, 2, 4, 5]))

def test_largest_number_3():
    print(largest_number([3, 20, 25, 1000, 5]))

test_largest_number_1()
test_largest_number_2()
test_largest_number_3()
