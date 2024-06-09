"""
Auto-graded Task 2
In a newly created Python script called merge_sort.py:
● Modify the Merge sort algorithm to order a list of strings by string length
from the longest to the shortest string.
● Run the modified Merge sort algorithm against 3 string lists of your
choice. Please ensure that each of your chosen lists is not sorted and has a
length of at least 10 string elements.
"""

# sorts from smallest to largest algo

def merge_sort(items):
    n = len(items)
    temporary_storage = [None] * n
    size_of_subsections = 1


    while size_of_subsections < n:
        for i in range(0, n, size_of_subsections * 2):
            i1_start, i1_end = i, min(i + size_of_subsections, n)
            i2_start, i2_end = i1_end, min(i1_end + size_of_subsections, n)
            sections = (i1_start, i1_end), (i2_start, i2_end)
            merge(items, sections, temporary_storage)
        size_of_subsections *= 2


    return items

def merge(items, sections, temporary_storage):
    (start_1, end_1), (start_2, end_2) = sections
    i_1 = start_1
    i_2 = start_2
    i_t = 0


    while i_1 < end_1 or i_2 < end_2:
        if i_1 < end_1 and i_2 < end_2:
            if items[i_1] < items[i_2]:
                temporary_storage[i_t] = items[i_1]
                i_1 += 1
            else: # the_list[i_2] >= items[i_1]
                temporary_storage[i_t] = items[i_2]
                i_2 += 1
                i_t += 1


        elif i_1 < end_1:
                for i in range(i_1, end_1):
                    temporary_storage[i_t] = items[i_1]
                    i_1 += 1
                    i_t += 1


        else: # i_2 < end_2
                for i in range(i_2, end_2):
                    temporary_storage[i_t] = items[i_2]
                    i_2 += 1
                    i_t += 1
        for i in range(i_t):
            items[start_1 + i] = temporary_storage[i]
