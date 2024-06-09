"""
Task: 
------------------
1. Add another method in the Course class that prints the head office location: Cape Town
2. Create a subclass of the Course class named OOPCourse
3. Create a constructor that initialises the following attributes and assigns these values:
    --- "description" with a value "OOP Fundamentals"
    --- "trainer" with a value "Mr Anon A. Mouse"
4. Create a method in the subclass named "trainer_details" that prints what the 
   course is about and the name of the trainer by using the description and trainer attributes.
5. Create a method in the subclass named "show_course_id" that prints the ID number of the course: #12345
6. Create an object of the subclass called course_1 and call the following methods
   contact_details
   trainer_details
   show_course_id
   These methods should all print out the correct information to the terminal

Note: this task covers single inheritance. Multiple inheritance is also possible in Python and 
we encourage you to do some research on multiple inheritance when you have finished this course.
"""

class Course:
    # class variables declared for name and contact website details
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"

    """Returns the contact details"""
    def contact_details(self) -> str:
        print("Please contact us by visiting", self.contact_website)

    """Returns the location and sets it as default"""
    def head_office(self, location="Cape Town") -> str:
        return f"The location is {location}"



class OOPCourse(Course):
    def __init__(self, description="OOP Fundamentals", trainer="Mr Anon A. Mouse"):
        """ Creating a subclass of Course class.

        Keyword arguments:
        description -- description of course (default OOP Fundamentals)
        trainer -- name of trainer (default Mr Anon A. Mouse)
        """
        super().__init__()
        self.description = description
        self.trainer = trainer

    """Returns a string detailing the subject"""
    def trainer_details(self) -> str:
        return f"The course subject is about {self.description}, the trainer is {self.trainer}"
    
    """Returns a string detailing the course ID"""
    def show_course_id(self, id="#12345") -> str:
        self.id = id
        return f"The course ID is: {self.id}"

# creating an object
course_1 = OOPCourse()

# printing attributes of the object and invoking methods
print(course_1.description)
print(course_1.trainer_details())
print(course_1.show_course_id())
