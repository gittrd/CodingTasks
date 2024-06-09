"""
Create a function that takes a list of integers and 
a single integer as arguments. The single integer will
represent an index point. The function needs to add the 
sum of all the numbers in the list up until and including 
the given index point by making use of recursion rather than loops.
"""

# defining a list of integers and index point
my_list = [1, 2, 3, 4, 5]
#idx = 4

# defining the recursive function 
def adding_up_to(lst, idx):
	"""Recursive function to sum up the list up to index point"""
	
    # if statement to check if the lst is blank
	if len(lst) == 0: 
		return 0
	
    # else statement to returning the recursion
	else: 
		return lst[0] + adding_up_to(lst[1:idx+1], idx) 

# Calculate the sum using the function above
total_sum = adding_up_to(my_list, 4) 

print(f"The total sum including the index is: {total_sum}") 

def test_adding_up_to_1():
    print(adding_up_to([1, 4, 5, 3],3))

def test_adding_up_to_2():
    print(adding_up_to([3, 1, 6, 8, 2, 4, 5],1))

def test_adding_up_to_3():
    print(adding_up_to([3, 20, 25, 1000, 5],3))

test_adding_up_to_1()
test_adding_up_to_2()
test_adding_up_to_3()
