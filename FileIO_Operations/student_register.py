"""
The main aim of the program should enable the user to register students for an exam.
Firstly, ask the user how many students are being registered for the exam.
Secondly, use a for loop that runs for that number of students.
Thirdly, each time the loop runs, propmt the user for the next student ID.
Finally, take each student ID input and write it to a text file "reg_form.txt".
Also add a dotted line after each student ID as it is used as a register.
"""

# prompting the user to declare how many students are being entered for the exam
num_students = int(input("How many students are registering for the exam? "))
# print(f"Number of students registering for the exam is: {num_students}")

# log to store the students ID that registered for the exam
register_students = ""

# logic of the core program
for student in range(0, num_students):
    if student < num_students:
        register_students += str(input("Please enter the student ID number:")) + " .............." + "\n"
    else:
        pass

with open ("reg_form.txt", "w") as file:
    file.write(register_students)

print("The registration form is as follows:")
print(register_students)
