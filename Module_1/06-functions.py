"""
A function in Python is a block of code that can be reused multiple times throughout a program. Functions are used to perform specific tasks and can be called upon to execute when needed. Functions can take zero or more arguments, and can return zero or one values. In Python, the def keyword is used to define a function.
Here's an example of a simple function that takes no arguments and returns no values:
"""
def greet():
    print("Hello, World!")

greet()  
# Output: Hello, World!

"""
Functions can also take arguments, which are values passed to the function when it is called. The arguments are placed within the parentheses of the function definition. Here's an example of a function that takes one argument:
"""
def func(name):
    print("Hello, " + name + "!")

func("Adeleke")

# Output: Hello, Adeleke!

"""
Functions can also return values. The return statement is used to return a value from a function. Here's an example of a function that takes two arguments and returns their sum:"""

def add(a, b):
    return a + b

result = add(2, 3)
print(result)  # Output: 5

""" Additionally, functions can have default values for their arguments, which means if a value is not passed to that argument when the function is called, it will use the default value. Here's an example of a function that has a default value for one of its arguments:"""

def greet(name, greeting="Hello"):
    print(greeting + ", " + name + "!")

greet("Adeleke")   # Output: Hello, Adeleke!
greet("Adeleke", "Hi")   # Output: Hi, Adeleke!


