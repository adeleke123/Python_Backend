"""
Casting in Python is the process of converting one data type to another. For example, converting an integer to a string, or a string to a float. This can be done using the built-in casting functions:
"""
'''
int(): converts a value to an integer
float(): converts a value to a float
str(): converts a value to a string
'''
# Examples:

x = "10.5"
y = int(x) # y will be 10

x = "10"
y = float(x) # y will be 10.0

x = 10
y = str(x) # y will be "10"

# You can also use the eval() function to convert string to the type of the variable, but it is not recommended to use this function as it is a security risk.

x = "10"
y = eval(x) # y will be 10

# Another way to cast is using type-casting, like this:

x = 10
y = float(x) # y will be 10.0

# It's important to note that casting can fail if the value cannot be converted to the specified type. For example, trying to convert a string of non-numeric characters to an integer will raise a ValueError.
