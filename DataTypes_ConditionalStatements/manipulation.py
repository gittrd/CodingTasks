'''
Ask the user to eneter a sentence by using the input() function
Save the user input into a variable called str_manip
Calculate and display the length of the string that was stored within the variable str_manip
Find the last letter in the string that was saved to str_manip sentence
Then based on this last letter that was found, replace every occurence with "@"
'''

# storing the users input
string = input("Please enter your name: ")
print(string)

# finding the length of the string and returning the last occurence in the string
print(len(string))
print(string[-1:])

# replacing last occurence with "@"
str_manip = string.replace("n", "@")
print(str_manip)
