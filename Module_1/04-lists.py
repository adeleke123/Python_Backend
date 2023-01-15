"""
A list is a collection of arbitrary objects, somewhat akin to an array in many other programming languages but more flexible.

Lists are defined in Python by enclosing a comma-separated sequence of objects in square brackets ([]), as shown below:

"""
a = ['belts', 'rollers', 'gears', 'motors']
print(a)
# output ['belts', 'rollers', 'gears', 'motors']

''' The important characteristics of Python lists are as follows:

Lists are ordered.
Lists can contain any arbitrary objects.
List elements can be accessed by index.
Lists can be nested to arbitrary depth.
Lists are mutable.
Lists are dynamic.
Each of these features is examined in more detail below.

Lists Are Ordered

A list is not merely a collection of objects. It is an ordered collection of objects. 

The order in which you specify the elements when you define a list is an innate characteristic of that list and is maintained for that list’s lifetime.

A list with a single object is sometimes referred to as a singleton list

Lists that have the same elements in a different order are not the same:'''

a = ['belts', 'rollers', 'gears', 'motors']

b = ['ddu', 'stacker', 'ms', 'magneta']
print(a==b)
# output false

'''Lists Can Contain Arbitrary Objects

A list can contain any assortment of objects. The elements of a list can all be the same type:'''
a = [2, 1, 4, 5]
print(a)
# output [2, 1, 4, 5]

mixed = [1, 'cat', 3.14, [5, 6]]
print(mixed)
# output [1, 'cat', 3.14, [5, 6]
'''List Elements Can Be Accessed by Index Individual elements in a list can be accessed using an index in square brackets.

This is exactly analogous to accessing individual characters in a string. List indexing is zero-based as it is with strings.'''

components = ['belts', 'rollers', 'gears', 'motors', 'bearings', 'clips']
index = components.index('motors')
print(index)
# output 3

''' Virtually everything about string indexing works similarly for lists. For example, a negative list index counts from the end of the list:'''
print(components[2:3])
# output gears
print(components[-4:4])
#output gears, motors

fruits = ['apple', 'banana', 'orange', 'mango', 'kiwi']
print(fruits[-3:-1]) # prints ['orange', 'mango']

