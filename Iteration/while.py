'''
Prompt the user to enter a number continuously
If the user enters -1, then the program should stop asking the user to enter a number
Then we must calculate the average of all the input from the user, excluding -1
'''
# declaring variables to store the total and number of times the user types in a value
total = 0
inputs_typed = 0

# prompt the user to add a value
user_input = int(input("Please type a number (-1 to exit) "))

# while loop for the logic
while user_input != -1:
    total += user_input
    inputs_typed += 1
    # total / inputs_typed

    user_input = int(input("Please type a number (-1 to exit) "))

    if user_input == -1:
        print(f"Total based on user input is: {total}")
        print(f"Number of times the user added an input is: {inputs_typed}")
        print(f"The average is: {total / inputs_typed}")
        break
