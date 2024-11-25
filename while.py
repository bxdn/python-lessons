# To continue doing things while a condition is true, use the "while" keyword.
# "while" can be thought of like an "if", but instead of continuing with the code after execution, until the condition in the "while" is false, the program will jump back to the beginning of the block.
# The following block will print 5 since x is > 2, then assign x to 4.
x = 5
if x > 2:           
    print(x)           
    x = x - 1 

# However, this block will execute as follows:
# print 5, since x > 2.
# Assign x to 4
# print 4, since x > 2.
# Assign x to 3
# print 3, since x > 2.
# Assign x to 2.
# Continue on, since x is now not greater than 2.
x = 5
while x > 2:            # while this condition is true, execute the intented block
    print(x)            # prints 5, then 4, then 3
    x = x - 1           # subtract 1 from x and set x to that result

# This block will print all numbers up to 10
x = 1
while x <= 10:
    print(x)
    x = x + 1
