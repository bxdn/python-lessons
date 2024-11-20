# Strings can be manipulated through methods, or functions.
# To transform a string to upper case, use the 'upper()' method
x = 'hi'
x = x.upper()
print(x) # prints "HI"

# To transform a string to lower case, use the 'lower()' method
x = 'HI'
x = x.lower()
print(x)

# To split a string into subcomponents, use the 'split()' method.  
# This method returns a list of strings that are split up by the argument.
# If no argument is provided, the string will be split on any white space (any spaces, tabs, or new lines)
x = "This is a string"
x = x.split()
print(x) # prints ['This', 'is', 'a', 'string']
x = 'This.is.a.string'
x = x.split('.')
print(x) # also prints ['This', 'is', 'a', 'string']

# To remove leading and trailing whitespace, use the 'strip()' method.
x = '   This is a string with space around       '
x = x.strip()
print(x) # prints 'This is a string with space around'