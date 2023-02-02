"""
A class constructor in Python is a special method __init__ that is automatically called when an object of the class is created. It is used to initialize the attributes of the class.
The __init__ method is defined in the class body and has the following syntax:

class ClassName:
    def __init__(self, [arg1, arg2, ...]):
# Initialize class attributes
self is a reference to the current object being created and is always the first parameter of the __init__ method. The other parameters are used to pass in values for the attributes of the object being created.

Here's a simple example that demonstrates how to use the __init__ method:
"""
class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

student = Student("John Doe", "12345")
print(student.name) # Output: John Doe
print(student.roll_number) # Output: 12345
