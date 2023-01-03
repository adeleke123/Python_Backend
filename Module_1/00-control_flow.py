"""
In python we have logical condition statements which states:
   A logical condition in Python is an expression that evaluates to either True or False. These conditions are often used in control statements such as if, while, and for loops to control the flow of the program based on certain conditions.

Here are some examples of logical conditions in Python:

Equality:
x == y (True if x is equal to y, False otherwise)
x != y (True if x is not equal to y, False otherwise)

Comparison:
x < y (True if x is less than y, False otherwise)
x <= y (True if x is less than or equal to y, False otherwise)
x > y (True if x is greater than y, False otherwise)
x >= y (True if x is greater than or equal to y, False otherwise)

Membership:
x in y (True if x is an element of y, False otherwise)
x not in y (True if x is not an element of y, False otherwise)
Identity:

x is y (True if x and y refer to the same object, False otherwise)
x is not y (True if x and y do not refer to the same object, False otherwise)
We can also use logical operators such as "and," "or," and "not" to combine multiple logical conditions. For example:

x < y and y < z (True if x is less than y and y is less than z, False otherwise)
x < y or y < z (True if either x is less than y or y is less than z, False otherwise)
not x < y (True if x is not less than y, False otherwise)

"""
# Examples

x = 4
y = 7
z = 11
if x > y:
    print("x is greater than y")
else:
    print("oops! x is not greater than y")
"""
oops! x is not greater than y

"""
print("Hurray!") if z > y else print("Nah!")
"""
Hurray
"""
a = int(input('Enter your age: '))
print('Hello, you\'re eligible to vote') if a >= 18 else print('Sorry! you are not eligible to vote')
"""
This line of code prompts the user to enter their age, reads in the age as a string, converts it to an integer, and stores it in the variable a.

Then it uses an if-else statement to check if a is greater than or equal to 18. If it is, the statement print('Hello, you\'re eligible to vote') is executed, which prints out the message "Hello, you're eligible to vote." If a is not greater than or equal to 18, the statement print('Sorry! you are not eligible to vote') is executed, which prints out the message "Sorry! you are not eligible to vote."

The input function is used to read user input from the console, and the int function is used to convert the input (which is a string) to an integer. The 'Enter your age: ' string is passed as an argument to the input function and is used as a prompt to ask the user to enter their age.

The if-else statement consists of a boolean expression (in this case, a >= 18) followed by a colon, and then one or more statements indented under the boolean expression. If the boolean expression evaluates to True, the indented statements under the if clause are executed. If the boolean expression evaluates to False, the indented statements under the else clause are executed.


"""
if x > y:
    print('x box')
elif x == y:
    print('book')
else:
    print('y box')
"""
These lines of code use an if-elif-else statement to check the value of two variables, x and y, and execute different statements depending on the values of x and y.

The if clause is followed by a boolean expression (in this case, x > y) and a colon, and then one or more statements indented under the boolean expression. If the boolean expression evaluates to True, the indented statements under the if clause are executed.

The elif (short for "else if") clause is also followed by a boolean expression (in this case, x == y) and a colon, and then one or more statements indented under the boolean expression. If the boolean expression for the if clause evaluates to False and the boolean expression for the elif clause evaluates to True, the indented statements under the elif clause are executed.

The else clause is followed by a colon and then one or more statements indented under the else clause. If the boolean expressions for both the if and elif clauses evaluate to False, the indented statements under the else clause are executed.

In this case, if x is greater than y, the statement print('x box') is executed. If x is equal to y, the statement print('book') is executed. If x is neither greater than y nor equal to y, the statement print('y box') is executed.

"""
