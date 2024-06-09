"""
Read the data from the text file named DOB.txt, then
print out in two different sections as per the format:

Name
First Last Name
...

Birthdate
Day Month Year
...

"""

# opening the text file
with open ("DOB.txt", "r") as file:
    content = file.readlines()
    print(f"Original string is as follows: {content}\n")

# declaring empty strings to store elements whilst looping through the content string
name = ""
dob = ""

# for loop that loops through the original string
for line in content:
    split_content = line.split(" ")
    fname = split_content[0]
    name += fname + " "
    lname = split_content[1]
    name += lname + " " + "\n"

    day = split_content[2]
    dob += day + " "
    month = split_content[3]
    dob += month + " "
    year = split_content[4]
    dob += year

print("Name")
print(name)

print("\n")

print("Birthdate")
print(dob)
