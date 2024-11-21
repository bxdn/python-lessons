# To define a piece of reusable code, create a function using the 'def' keyword
def my_function():          # defines a function called 'my_function' that prints the number 6 followed by the number 7
    print(6)    
    print(7)

# To use the function (also called CALLING the function), use the name like a variable, but add () to the end of the name.
my_function()               # CALLS my_function, running the code inside it
my_function()               # twice, printing 6, then 7, then 6, then 7

# To define a function that has an unknown at the time of writing (called a 'parameter' or 'argument'), use the following syntax
def make_sparkly(txt):      # defines a function called 'make_sparkly' that has an ARGUMENT called 'txt'.  Prints the ARGUMENT surrounded by asterisks
    print('*' + txt + '*')

# To CALL a function with ARGUMENTS, use the name like a variable, but insert the ARGUMENTS into the parentheses following this pattern (arg1, arg2, arg3)
make_sparkly('hi')          # prints *hi*
make_sparkly('omg')     # prints *omg*

# To define a function that has an unknown at the time of writing (called a 'parameter' or 'argument'), use the following syntax
def add_print(num1, num2):  # defines a function called 'add_print' that has 2 ARGUMENTs called 'num1' and 'num2'.  Prints the sum of the arguments
    print(num1 + num2)

add_print(1, 3)             # prints 4
add_print(-5, -10)          # prints -15

# To define a function that doesn't just *DO* something but *ANSWERS* something, use the 'return' keyword
def plus_5(num):            # defines a function called 'plus_5' that has 1 ARGUMENT called 'num' and returns 5 plus the number provided
    return num + 5

x = plus_5(5)               # calls plus_5, taking the RETURN value (10) and assigning x to it
print(x)                    # prints 10
print(plus_5(5))            # also prints 10, but skips the variable, directly taking the RETURN value from plus_5 and printing it