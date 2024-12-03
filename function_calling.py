# A function is a piece of reusable code.  It is like a variable, but instead of a value, it is bound to a set of instructions.

# To use a function, use its name with () like the following: 
# do_stuff()
# A function call will resolve into a value, and therefore is also an expression.
# Some functions have inputs, or agruments.
# The following function has 3 arguments: "hi", 3 + 5, which resolves to 8, and the result of a call to another function, do_other_stuff.
# do_stuff("hi", 3 + 5, do_other_stuff())

# There are a number of functions built into Python.  One we will learn now is print()
# The print() function will print information into the terminal.  It will take any data type as input.
print("Hello, World!")

# Some function don't just DO something, but ANSWER something.
# These functions have what's called a RETURN value.  
# This is the value that the function call expression resolves to.

# Another function built into Python is the abs() function.  It takes a number as input, and then RETURNS the absolute value of that number.
print(abs(-2))          # prints 2
print(abs(1 + 1))       # prints 2
print(abs(-5) + abs(2 + 2)) # prints 9

# The max() function will return the maximum value of all values passed to it as input.
print(max(4, 5, 6))     # prints 6
print(max(1,2,10) - max(5,2,4)) # prints ?
print(abs(-5) + max(3, -5, -1, 0)) # prints ?

# The min() function will do the same, but for the minimum.
print(min(4,3))         # prints 3

# The len() function will return the length of a string
print(len("Hello"))     # prints 5

