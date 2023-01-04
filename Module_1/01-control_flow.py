"""
There are main two types of loop in python.They are
1. for loops and
2. while loops
A for loop is used to iterate over a sequence (such as a list, tuple, or string) or other iterable object.
A while loop is used to repeat a block of code as long as a certain condition is met.

"""
# Examples
# The for loop will execute the code block for each item in the sequence.
for number in [1, 2, 3, 4, 5]:
    print(number)
"""
This will list the numbers 1 through 5 on separate lines.
"""
# The while loop will continue to execute the code block as long as the condition is True. For example:
i = 0
while i < 5:
    print(i)
    i += 1

"""
This will list the numbers 0 through 4 on separate lines.
"""
'''The break and continue statements are used to control the flow of a loop in Python.'''

# The break statement is used to exit a loop prematurely. When the break statement is encountered inside a loop, it will cause the loop to terminate immediately, and the program will continue with the next statement after the loop. For example:

for number in range(1, 10):
    if number == 5:
        break
    print(number)

'''In this example, the loop will iterate over the numbers 1 through 9, but it will stop and exit the loop when it reaches the number 5. The output of this code will be: 1, 2, 3, 4.'''

# The continue statement is used to skip the remainder of the current iteration of a loop and move on to the next iteration. When the continue statement is encountered inside a loop, it will cause the loop to skip the rest of the code in the current iteration and move on to the next one. For example:

for number in range(1, 10):
    if number % 2 == 0:
        continue
    print(number)

'''In this example, the loop will iterate over the numbers 1 through 9, but it will skip printing the even numbers (2, 4, 6, 8) and only print the odd numbers (1, 3, 5, 7, 9). The output of this code will be: 1, 3, 5, 7, 9.'''
