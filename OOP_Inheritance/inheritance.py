"""
* Take the user inputs and ask for their name, age, hair colour and eye colour.
* Then create an Adult class with the following attributes and method:
Attributes: name, age, eye_colour and hair_colour
Method: can_drive() which prints the name of the person and
stating that they can drive as they are old enough.
* Create a subclass of the Adult class named Child that has the same
attributes, but overrides the can_drive() method to print the person's
name and that they are too young to drive.
* Create logic that determines if the person is 18 or older and create
an instance of the Adult class if this is true. Otherwise, create an instance
of the Child class. Once the object has been created, call the can_drive() method
to print out whether the person is old enough to drive or not.
"""

# prompting the user for input
name_input = str(input("What is your name? "))
age_input = int(input("How old are you? "))
hair_colour_input = str(input("What is the colour of your hair? "))
eye_colour_input = str(input("What is the colour of your eyes? "))



class Adult:
    def __init__(self, name=str, age=int, eye_colour=str, hair_colour=str):
        """Instantiating the Adult class
        
        Keyword arguments:
        name -- name of the person
        age -- age of the person
        eye_colour -- colour of the eyes
        hair_colour -- colour of the hair
        """
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour

    """Returns a string with name and statement"""
    def can_drive(self):
        return f"{self.name} can drive as he or she is 18 years old."



class Child(Adult):
    """Instantiating the Child class, inheriting from Adult"""
    def __init__(self, name=str, age=int, eye_colour=str, hair_colour=str):
        super().__init__(name, age, eye_colour, hair_colour)

    """Returns a string with name and statement"""
    def can_drive(self):
        return f"{self.name} cannot drive as her or she is not 18 years old."


# logic to determine if the person is 18 and creating objects
if age_input >= 18:
    adult_1 = Adult(name_input, age_input, eye_colour_input, hair_colour_input)
    print(adult_1.can_drive())
else:
    child_1 = Child(name_input, age_input, eye_colour_input, hair_colour_input)
    print(child_1.can_drive())
