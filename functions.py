# A function is a piece of reusable code.  It is like a variable, but instead of a value, it is bound to a set of instructions.
# To define a piece of reusable code, create a function using the 'def' keyword
def my_function():          # defines a function called 'my_function' assigns x to 6, and y to 7.
    x = 6   
    y = 7

# To use the function (also called CALLING the function), use the name like a variable, but add () to the end of the name.
my_function()               # CALLS my_function, running the code inside it
my_function()               # CALLS my_function again.

# The lines above will result in the following lines actually being run:
# x = 6   
# y = 7
# x = 6   
# y = 7

# To define a function that has an unknown at the time of writing (called a 'parameter' or 'argument'), use the following syntax
def make_sparkly(txt):      # defines a function called 'make_sparkly' that has an ARGUMENT called 'txt'.  Assigns x to the ARGUMENT surrounded by asterisks
    x = '*' + txt + '*'

# To CALL a function with ARGUMENTS, use the name like a variable, but insert the ARGUMENTS into the parentheses following this pattern (arg1, arg2, arg3)
make_sparkly('hi')          # assigns x to "*hi*"
make_sparkly('sparkles')    # assigns x to "*sparkles*"

# To define a function that has multiple arguments, use the following syntax
def add(num1, num2):        # defines a function called 'add' that has 2 ARGUMENTs called 'num1' and 'num2'.  Adds the 2 arguments and assigns them to x
    x = num1 + num2

add(1, 3)                   # assigns x to 4
add("Whats ", "up?")        # assigns x to "What's up?"

# There are a number of functions already built into Python.  One we will learn now is print()
# The print() function will print information into the terminal.
print("Hello, World!") 

# To define a function that doesn't just *DO* something but *ANSWERS* something, use the 'return' keyword
def plus_5(num):            # defines a function called 'plus_5' that has 1 ARGUMENT called 'num' and returns 5 plus the number provided
    return num + 5

x = plus_5(5)               # calls plus_5, taking the RETURN value (10) and assigning x to it
print(x)                    # prints 10
print(plus_5(5))            # also prints 10, but skips the variable, directly taking the RETURN value from plus_5 and printing it