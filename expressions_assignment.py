# Most valid Python lines contain an expression.
# An expression is any combination of valid python types, operators, and functions that reduce down to a value.
# Expressions follow the order of operations when resolving to a value.
# Here are some examples of valid expressions.  An expression is a valid line by itself.
3                   # Evaluates to 3 (int)
4.2                 # Evaluates to 4.2 (float)
False               # Evaluates to False (bool)
"Oh hi Mark"        # Evaluates to "Oh hi Mark" (str)
"Hello, " + "World!"# Evaluates to "Hello, World!" (str)
3 + 4.2             # Evaluates to 7.2 (float)
3 + 4.0             # Evaluates to 7.0 (float)
6 - 4               # Evaluates to 2 (int)
2 * 6               # Evaluates to 12
6 / 3               # Evaluates to 2.0 (float)
3 ** 2              # Evaluates to 9 (int)
6 // 5              # Evaluates to 1 (int)
6 % 5               # Evaluates to 1 (int)
(4 + 2) ** 2 / 9    # Evaluates to ? (?)

# Here is an example of an invalid expression.
# "7" + 3           # Not valid, Python does not understand how to add strings and numbers.

# You can save the result of expressions to variables.  Variables can be bound to values, then used in place of their values in future expressions.
# Expressions are always to the RIGHT of the equals sign, and the variable name is to the LEFT.
# The expression on the right side is ALWAYS evaluated first, then the variable on the left is bound to the resulting value.
x = 3               # x is now bound to the value 3 (int)
# 3 = x             # invalid since the variable and expression are on the wrong side of the equals sign
y = 3.8 + 4.2       # x is now bound to the value 8.0 (float)
z = x + y           # Since x is bound to 3, and y is bound to 8.0, z is now bound to 11.0 (float)
x = x + 1           # Since the right side is evaluated first, x + 1 evaluates to 4 (int), then x is bound to that value.
z                   # Since z was last calculated in line 27, it is still bound to 11.0 (float)
