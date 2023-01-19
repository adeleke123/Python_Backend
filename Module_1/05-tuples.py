"""
A tuple is a data structure in Python that is similar to a list, but it is immutable, meaning that the elements within it cannot be modified or replaced once it is created. Tuples are written with round brackets and they are ordered, meaning that the elements within it are in a specific order. They allow duplicate elements.

Here is an example of a tuple:
"""
my_tuple = (1, 2, 3, 4)
print(my_tuple)
# output (1, 2, 3, 4)

"""Some features of tuples are:
Immutable: Once a tuple is created, its elements cannot be modified, added, or removed. For example:
"""
'''my_tuple = (1, 2, 3, 4)
my_tuple[1] = 5  # This will raise a TypeError'''

''' Written with round brackets: Tuples are written with round brackets, like (1, 2, 3, 4) or ('a', 'b', 'c')
Ordered: The elements of a tuple are in a specific order, and that order is maintained when the tuple is modified. For example:'''

my_tuple = (1, 2, 3, 4)
print(my_tuple[1])  # Output: 2

'''Allow duplicate elements: Tuples can contain duplicate elements. For example:'''

my_tuple = (1, 2, 2, 3, 4)
print(my_tuple) # (1, 2, 2, 3, 4)

''' we can also use some of the built-in functions and methods that work with tuples such as len(), min(), max(), count(), index() and slicing.'''
my_tuple = (1, 2, 3, 4)
print(len(my_tuple))  # Output: 4
print(min(my_tuple))  # Output: 1
print(my_tuple.count(2))  # Output: 1
print(max(my_tuple)) # output 4

''' Nested Tuples: You can create nested tuples, where a tuple contains other tuples as its elements. For example:'''
my_tuple = ((1, 2), (3, 4), (5, 6))
print(my_tuple) # ((1, 2), (3, 4), (5, 6))

""" Tuple Unpacking: You can use the tuple unpacking feature to assign the elements of a tuple to separate variables."""
my_tuple = (1, 2, 3)
x, y, z = my_tuple
print(x)  # Output: 1
print(y)  # Output: 2
print(z)  # Output: 3
"""Tuple as a Key in Dictionaries: Tuples can be used as keys in dictionaries since they are immutable, unlike lists which are mutable."""
my_dict = {(1, 2): 'a', (3, 4): 'b'}
print(my_dict[(1, 2)])  # Output: 'a'

"""Use in Function Arguments: You can use tuples as arguments in a function. For example:"""
def add(a, b):
    return a + b

my_tuple = (1, 2)
print(add(*my_tuple))  # Output: 3

"""Concatenation and Repetition: You can concatenate and repeat tuples using the + and * operators, respectively."""
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print(t3)  # Output: (1, 2, 3, 4, 5, 6)

t4 = t1 * 3
print(t4)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

"""Overall, Tuples are a useful data structure in Python, because of its immutability, it can be used in situations where you want to ensure the data integrity and prevent any accidental modification."""

"""Basic tuple operation with examples, len, index, slicing, change value, append, remove, join includes"""

'''len: The len() function is used to determine the number of elements in a tuple. For example:'''

my_tuple = (1, 2, 3, 4)
print(len(my_tuple))  # Output: 4

'''index: The index() method is used to find the index of a specific element in a tuple. For example:'''

my_tuple = (1, 2, 3, 4)
print(my_tuple.index(3))  # Output: 2

'''Slicing: You can slice a tuple by specifying the start and end index. For example:'''
my_tuple = (1, 2, 3, 4)
print(my_tuple[1:3])  # Output: (2, 3)

'''Change Value:tuples are immutable, so you cannot change the value of an element in a tuple. However, you can create a new tuple with the modified values. For example:'''

my_tuple = (1, 2, 3, 4)
new_tuple = my_tuple[:2] + (5,) + my_tuple[3:]
print(new_tuple)  # Output: (1, 2, 5, 4)

'''Append: Tuples are immutable, so you cannot append elements to a tuple. However, you can create a new tuple that contains the original elements as well as the new elements. For example:'''

my_tuple = (1, 2, 3)
new_tuple = my_tuple + (4,)
print(new_tuple)  # Output: (1, 2, 3, 4)

'''Remove: There is no direct method to remove an element from a tuple. However, you can create a new tuple that contains all elements except the one you want to remove. For example:'''

my_tuple = (1, 2, 3, 4)
new_tuple = my_tuple[:1] + my_tuple[2:]
print(new_tuple)  # Output: (1, 3, 4)

'''Join: You can join the elements of a tuple to create a single string using the join() method. For example:'''

my_tuple = ('a', 'b', 'c')
print(''.join(my_tuple))  # Output: 'abc'
'''You can also join the elements of a tuple by a specific separator.'''

my_tuple = ('a', 'b', 'c')
print(', '.join(my_tuple))  # Output: 'a, b, c'

"""It's worth noting that the join method works with strings, and you cannot use it directly on tuples, you have to convert the tuple to a string before using the join method on it.
"""
