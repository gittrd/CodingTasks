"""
Writing unit tests for one of the prior practical tasks.
Using Recursion Task 13 below as my implementation.
"""

# defining the recursion function to find the largest number
def largest_number(array):
    if len(array) == 1:
        return array[0]
    else:
        lm = largest_number(array[1:])

        if lm > array[0]:
            return lm
        else:
            return array[0]
