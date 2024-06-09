"""
Using the following array: [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
● Create a Python script called sort_and_search.py.
Which searching algorithm would be appropriate to use on the given list?
● Implement this search algorithm to search for the number 9. Add a
comment to explain why you think this algorithm was a good choice.
● Research and implement the Insertion sort on this array.
● Implement a searching algorithm you haven’t tried yet in this Task on the
sorted array to find the number 9. Add a comment to explain where you
would use this algorithm in the real world.
"""



"""
Linear search is best used as we know the elements in the list are not in order.
If the elements were in order, we could of used the Binary search algorithm.
"""

# Linear search algorithm
def linear_search(value, my_list):
    # Iterate over items until correct value is found
    # Return value otherwise return none if value is not found
    for i in range(len(my_list)):
        if my_list[i] == value:
            return i

my_list = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
print(linear_search(9, my_list))


# implementing the insertion sort on the array/list
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

my_list = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
insertion_sort(my_list)
print("Sorted array is:", my_list)

# trying out Bubble sort algorithm
def bubble_sort(my_list):
    for i in range(len(my_list) - 1, -1, -1):
        for j in range(1, i + 1):
            if my_list[j-1] > my_list[j]:
                my_list[j - 1], my_list[j] = my_list[j], my_list[j - 1]
    return my_list


print(bubble_sort(my_list))
