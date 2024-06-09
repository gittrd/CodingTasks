"""
Read a string and make each alternate character into an upper case character and each other alternate character a lower case character.
Using the split() and join() functions will help.
"""

# random string
user_string = input("Please enter a string of your choice: ")
print("")

# printing user input
print(f"The original string is: {user_string}")
print("")

# declaring an empty list and boolean value
upper = True
new_string = []

# for loop to alternate upper and lower case
for letter in user_string:
    if upper:
        new_string.append(letter.lower())
        upper = False
    else:
        new_string.append(letter.upper())
        upper = True
new_string = "".join(new_string)
print(f"The modified string is: {new_string}")

"""
It would be great to get some feedback on how to ignore the blank spaces between each word,
as currently the code is taking into consideration the blank spaces.
Sorry, I just did not know how to implement this.
"""
