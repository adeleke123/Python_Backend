'''In Python, strings are sequences of characters and are used to represent text. There are several operations that can be performed on strings, including:'''

# Concatenation: Joining two or more strings together using the + operator.

x = "Hello"
y = "world"
z = x + " " + y  # z will be "Hello world"

# Repetition: Creating a new string by repeating an existing string a certain number of times using the * operator.

x = "Hello"
y = x * 3  # y will be "HelloHelloHello"

# Indexing: Accessing individual characters in a string using square brackets [].

x = "Hello"
print(x[1]) # Output 'e'

# Slicing: Accessing a range of characters in a string using square brackets [] and a colon :.

x = "Hello"
print(x[1:4]) # Output 'ell'

# Membership: Checking if a character or a substring is present in a string using the in keyword.

x = "Hello"
print("e" in x) # Output True

# Comparison: Comparing two strings to check if they are equal or not using == operator or != operator.

x = "Hello"
y = "hello"
print(x == y) # Output False

'''String Methods: Python provides several built-in methods that can be used on strings. Some of the most commonly used methods include:'''

.lower(): Converts a string to lowercase.
.upper(): Converts a string to uppercase.
.replace(old, new): Replaces all occurrences of a substring with a new substring.
.strip(): Removes whitespace characters from the beginning and end of a string.
.split(delimiter): Splits a string into a list of substrings based on a delimiter.
.join(iterable): Joins all elements in an iterable (e.g. list, tuple) into a string, using the string as a separator.

x = " Hello World! "
print(x.strip()) # Output "Hello World!"

# These are some of the common string operations, but there are many more and all of them are widely used in Python applications.
