"""
set are a type of collection that stores multiple items in a single variable
some important features of sets are:-
1. A set is immutable, meaning that its contents cannot be changed once it has been created.
2. Sets are written with curly brackets {}.
3. Sets are unordered, meaning that the items in a set are not stored in a specific order.
4. Sets are unindexed, meaning that items in a set cannot be accessed using an index like in a list or tuple.
5. Sets do not allow duplicate items, meaning that if an item is added to a set more than once, it will only appear once in the set.

Basic sets operations include:-
len, index, type, add, change value, update, discard, pop, remove, clear, making a set constructor, joining two sets
"""
# Here are some examples of basic set operations:
'''To get the length of a set, you can use the len() function:'''
my_set = {1, 2, 3, 4, 5}
print(len(my_set)) # Output: 5

'''To add an item to a set, you can use the add() method:'''
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set) # Output: {1, 2, 3, 4, 5, 6}

'''To update a set with the items from another set or iterable, you can use the update() method:'''
my_set = {1, 2, 3, 4, 5}
my_set.update([6, 7, 8])
print(my_set) # Output: {1, 2, 3, 4, 5, 6, 7, 8}

'''To remove an item from a set, you can use the discard() or remove() method:'''
my_set = {1, 2, 3, 4, 5}
my_set.discard(4) # removes 4 from the set
print(my_set) # Output: {1, 2, 3, 5}

my_set = {1, 2, 3, 4, 5}
my_set.remove(4) # removes 4 from the set
print(my_set) # Output: {1, 2, 3, 5}

'''To clear a set of all items, you can use the clear() method:'''

my_set = {1, 2, 3, 4, 5}
my_set.clear()
print(my_set) # Output: set()

'''This will remove all items from the set, leaving it empty. Note that the set is still present, but it is empty and contains no items.'''


'''To create a set using the set constructor, you can use the set() function:'''
my_set = set([1, 2, 3, 4, 5])
print(my_set) # Output: {1, 2, 3, 4, 5}

'''To join two sets together, you can use the union() or | operator:'''
set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
set_3 = set_1.union(set_2) # {1, 2, 3, 4, 5}
set_4 = set_1 | set_2 # {1, 2, 3, 4, 5}

# list other set operations with examples
'''Here are some additional set operations that you can perform in Python, along with examples:'''

# To create a new set that contains items from both sets, but only the items that are common to both sets, you can use the intersection() method or the & operator:
set_1 = {1, 2, 3, 4, 5}
set_2 = {3, 4, 5, 6, 7}
set_3 = set_1.intersection(set_2) # {3, 4, 5}
set_4 = set_1 & set_2 # {3, 4, 5}

# To create a new set that contains all items from both sets, but only the items that are not common to both sets, you can use the difference() method or the - operator:
set_1 = {1, 2, 3, 4, 5}
set_2 = {3, 4, 5, 6, 7}
set_3 = set_1.difference(set_2) # {1, 2}
set_4 = set_1 - set_2 # {1, 2}

# To create a new set that contains all items from both sets, but removes any items that are common to both sets, you can use the symmetric_difference() method or the ^ operator:
set_1 = {1, 2, 3, 4, 5}
set_2 = {3, 4, 5, 6, 7}
set_3 = set_1.symmetric_difference(set_2) # {1, 2, 6, 7}
set_4 = set_1 ^ set_2 # {1, 2, 6, 7}

# To check if a set is a subset of another set, meaning that all items in the first set are also present in the second set, you can use the issubset() method:
set_1 = {1, 2, 3, 4, 5}
set_2 = {1, 2, 3}
set_3 = {1, 2, 3, 4}

print(set_2.issubset(set_1)) # True
print(set_3.issubset(set_1)) # True
print(set_1.issubset(set_2)) # False

# To check if a set is a superset of another set, meaning that all items in the second set are also present in the first set, you can use the issuperset() method:
set_1 = {1, 2, 3, 4, 5}
set_2 = {1, 2, 3}
set_3 = {1, 2, 3, 4}

print(set_1.issuperset(set_2)) # True
print(set_1.issuperset(set_3)) # True
print(set_2.issuperset(set_1)) # False
