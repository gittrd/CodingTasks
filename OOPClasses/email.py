import numpy as np

### --- OOP Email Simulator --- ###
# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
    # Declare the class variable, with default value, for emails. 
    # Initialise the instance variables for emails.
    # Create the method to change 'has_been_read' emails from False to True.

class Email():
    """ Instantiating the main class Email, outlining the methods and properties.
    """
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    """ Marking the email as being read.
    """
    def mark_as_read(self):
        self.has_been_read = True

# --- Lists --- #
# Initialise an empty list to store the email objects.

inbox = list()

# --- Functions --- #
# Build out the required functions for your program.
# Create 3 sample emails and add it to the Inbox list.

def populate_inbox():
    email_one = Email(
                    input("Please enter your email: "), 
                    input("Please enter a subject line for your email: "),
                    input("Please enter your email content: "))
    
    inbox.append(email_one)

    email_two = Email(
                    input("Please enter your email: "),
                    input("Please enter a subject line for your email: "),
                    input("Please enter your email content: "))
    
    inbox.append(email_two)

    email_three = Email(
                    input("Please enter your email: "),
                    input("Please enter a subject line for your email: "),
                    input("Please enter your email content: "))
    
    inbox.append(email_three)

populate_inbox()
print(f"Inbox list populated by the user: {inbox}")

# Create a function which prints the email’s subject_line, along with a corresponding number.

print("Email's subject lines:")
def list_emails():
    for num, element in enumerate(inbox):
        print(num, element.subject_line)

list_emails()

# Create a function which displays a selected email. 
# Once displayed, call the class method to set its 'has_been_read' variable to True.

email_choice = int(input("Please enter the email index (0 to n) that you would like to view: "))

def read_email(index):
    choice_of_user = inbox[index]
    print(choice_of_user.email_address)
    print(choice_of_user.subject_line)
    print(choice_of_user.email_content)
    choice_of_user.mark_as_read()

read_email(email_choice)

# --- Email Program --- #
# Call the function to populate the Inbox for further use in your program.
# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
    
    # logic to read an email
    if user_choice == 1:
        list_emails()
        email_selected = int(input("Which email would you like to read? "))
        read_email(email_selected)
    
    # logic to view unread emails
    elif user_choice == 2:
        for element in inbox:
            if element.has_been_read == False:
                print(element.subject_line)

    # logic to quit application 
    elif user_choice == 3:
        break

    else:
        print("Oops - incorrect input.")
