'''
Write an algorithm that shows a patter
Use a for loop, that utilises an if-else statement
'''

# declaring a variable that stores the number of rows to be printed
END = 10

# declaring the for loop
# the aim here is for the for loop to iterate between 1 to 9 (not including 10)
for i in range(1, END):

    # if the iteration is less than six, then store the iteration number into count
    if i < 6:
        count = i
    # else once => 6, then take the END variable less the iteration number
    else:
        count = END - i

    # print statement to print the * and multiply by the count variable
    print('*' * count)
