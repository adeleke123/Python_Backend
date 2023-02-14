""" In Python, a module is a file containing Python definitions and statements. 

The file name is the module name with the suffix ".py" appended to it.

When you import a module, you can access its functions, classes, and variables in your program.

Here's an example of a simple module named my_module.py:
# my_module.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

pi = 3.14159

In the example above, my_module.py contains two functions, add() and subtract(), and a variable pi. To use these functions and variable in another Python file, you can import the module as follows:
"""
import my_module

print(my_module.add(1, 2))    # Output: 3
print(my_module.subtract(5, 2))    # Output: 3
print(my_module.pi)    # Output: 3.14159

'''You can also import specific functions and variables from a module using the from keyword:'''

from my_module import add, pi

print(add(1, 2))    # Output: 3
print(pi)    # Output: 3.14159

'''In addition, you can give a module a different name when you import it using the as keyword:'''
import my_module as mm

print(mm.add(1, 2))    # Output: 3
print(mm.pi)    # Output: 3.14159

'''Python also has built-in modules that you can use in your programs. For example, the math module provides many mathematical functions and constants, such as sin(), cos(), sqrt(), and pi. To use the math module, you can import it as follows:'''

import math

print(math.sin(math.pi/2))    # Output: 1.0
print(math.sqrt(25))    # Output: 5.0

