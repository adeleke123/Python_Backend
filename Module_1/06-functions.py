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

"""Functions in python also can take variable number of arguments, you can use *args for taking variable number of non-keyword arguments, and **kwargs for variable number of keyword argument."""

def test_function(arg1, *args, **kwargs):
    print(arg1)
    print(args)
    print(kwargs)
test_function(1, 2, 3, 4, a=5, b=6)
""" Functions in Python are a powerful feature, they allow you to organize your code and make it more readable and maintainable. They can take arguments, return values, have default values for arguments, and support variable number of arguments.

You can also use lambda function, which is small anonymous function, with or without arguments and a single expression. This function can be used wherever function objects are required."""
add = lambda x, y : x + y
print(add(2,3)) 
# output 5
"""
You can also use the built-in functions like map(), filter(), and reduce() to perform operations on lists, Tuples and other data structures with functions.

In short, functions are a fundamental building block of Python programming, they help you to organize your code, make it more readable, and allow you to reuse your code multiple times throughout your program."""

