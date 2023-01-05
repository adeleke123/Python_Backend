"""
Dictionaries are a type of collection that stores key-pairs items in a single variable.
some important features of dictionaries are:-
They are mutable
They are written with curly bracket
They are ordered
They are written as key:value pair
They do not allow duplicates.
Basic dictionaries operations include:-
len, index, add, change value, update, discard, pop, remove, clear, pop item.

"""
'''Dictionaries are a type of collection that stores key-pairs items in a single variable.
some important features of dictionaries includes'''
# They are mutable: which means that that you can change the values of the keys in a dictionary. For example:
my_dict = {'name': 'Adeleke', 'age': 40}
my_dict['age'] = 38
print(my_dict) 
# output {'name': 'Adeleke', 'age': 31}

# Dictionaries are written with curly brackets: To create a dictionary, you enclose a list of key-value pairs in curly brackets. For example:
my_dict = {'name': 'Adeleke', 'age': 40}

# Dictionaries are ordered: In Python 3.7 and later, dictionaries maintain the order in which elements are added. In earlier versions of Python, dictionaries are unordered.

# Dictionaries are written as key-value pairs: Each element in a dictionary consists of a key and a value, separated by a colon. For example:
my_dict = {'name': 'Adeleke', 'age': 40}

# Dictionaries do not allow duplicates: You cannot have two keys with the same name in a dictionary. If you try to add a key that already exists, the value will be updated. For example:
my_dict = {'name': 'Adeleke', 'age': 40}
my_dict['name'] = 'wale'
print(my_dict)
# output {'name': 'Khadijah', 'age': 40}
'''some basic dictionary operations includes the following'''
# len: This returns the number of elements in the dictionary. For example:

my_dict = {'name': 'Adeleke', 'age': 40}
print(len(my_dict))
# output

# index: This returns the value of a key. For example:

my_dict = {'name': 'Adeleke', 'age': 40}
print(my_dict['name'], my_dict['age'])
# output 'Adeleke', 40

# add: To add a new key-value pair to a dictionary, you can use the assignment operator. For example:

my_dict = {'name': 'Adeleke', 'age': 40}
my_dict['country'] = 'Nigeria'
print(my_dict)
# {'name': 'Adeleke', 'age': 40, 'country': 'Nigeria'}

# change value: To change the value of a key in a dictionary, you can use the assignment operator. For example:

my_dict = {'name': 'Adeleke', 'age': 30}
my_dict['age'] = 31
print(my_dict)
# output {'name': 'Adeleke', 'age': 31}

# update: You can use the update method to add multiple key-value pairs to a dictionary at once. For example:

my_dict = {'name': 'Adeleke', 'age': 30}
my_dict.update({'country': 'France', 'gender': 'male'})
print(my_dict)
# output {'name': 'Adeleke', 'age': 30, 'country': 'France', 'gender': 'male'}

# discard: You can use the discard method to remove a key-value pair from a dictionary. If the key does not exist, this method does nothing. For example:
my_dict = {'name': 'Adeleke', 'age': 30}
my_dict.discard('age')
print(my_dict)

# output {'name': 'Adeleke'}

# pop: You can use the pop method to remove a key-value pair from a dictionary and return the value. If the key does not exist, this method returns a default value. For example:

my_dict = {'name': 'wale', 'age': 30}
age = my_dict.pop('age', None)
print(age)

# output 30

# remove: You can use the remove method to remove a key-value pair from a dictionary. If the key does not exist, this method raises a KeyError. For example:

my_dict = {'name': 'wale', 'age': 30}
my_dict.remove('age')
print(my_dict)
# output {'name': 'wale'}

# clear: You can use the clear method to remove all key-value pairs from a dictionary. For example:

my_dict = {'name': 'John', 'age': 30}
my_dict.clear()
print(my_dict)
# output {}

# pop item: You can use the popitem method to remove and return a random key-value pair from a dictionary. If the dictionary is empty, this method raises a KeyError. For example:

my_dict = {'name': 'John', 'age': 30}
item = my_dict.popitem()
print(item)
# output ('age', 30)
