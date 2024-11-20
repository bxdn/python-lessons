# Recall booleans only can have 1 of 2 values, True, or False.
# Expressions resolving to booleans can be thought of as "Tests".
# These expressions resolve to either being True or False.

x = 7 > 3
print(x)    # prints True

x = 7 < 3
print(x)    # prints False

x = 3 == 3  # This is the Equality test, since a single '=' means assignment
print(x)    # prints True

x = 3 == 4
print(x)    # prints False

x = 3 != 4  # This is the non-equality test.
print(x)    # prints True

x = 3 != 3
print(x)    # prints False

# You can use 'and', 'or' and 'not' to create more complicated boolean expressions
x = 3 > 2 and 4 > 3 # evaluates as True since ALL statements '3>2' and '4>3' are True
print(x)    # prints True
x = 3 > 2 or 4 > 3 # evaluates as True since AT LEAST 1 of the statements '3>2' and '4>3' are True
print(x)    # prints True
x = 3 > 2 and 3 > 4 # evaluates as False since AT LEAST 1 of the statements '3>2' and '3>4' are False
print(x)    # prints False
x = 3 > 2 or 3 > 4 # evaluates as True since AT LEAST 1 of the statements '3>2' and '3>4' are True
print(x)    # prints True
x = 2 > 3 and 3 > 4 # evaluates as False since AT LEAST 1 of the statements '2>3' and '3>4' are False
print(x)    # prints False
x = 2 > 3 or 3 > 4 # evaluates as False since None of the statements '2>3' and '3>4' are True
print(x)    # prints False
x = not 3 > 2 # evaluates as False since 3 > 2 is True
print(x)    # prints False
x = not (3 > 2 or 3 > 4)
print(x)    # prints ?

