# Data fits into memory in different forms, or TYPES.  There are many types in Python, but here are some important ones
# Expressions always resolve to a type.
# Variables are always one specific type at a time.

# 1. Integer    - Whole numbers - ex. -2, -1, 0, 1, 2, ...
# 2. Float      - Decimal numbers - ex. -1.0, -0.5, 0.1, 0.11, 5.32, ...  
# 3. Boolean    - True/False - ex. True, False
# 4. String     - A "string" of characters (Examples of characters: 'a', 'b', '7', '!').  Basically a chunk of text. - ex. "hi", "7", "2 Tusked Walruses"
# 5. List       - An ordered collection of items.  Shares a lot in common with strings, which can be thought of as ordered collections of characters.
# 6. Set        - An unordered collection of unique items.
# 7. Dictionary - An unordered collection of unique keys mapped to corresponding values

# To get the type of a variable or expression, wrap it in the type() function.

# Examples:

x = 1 + 2       # Expression on the right evaluates to 3, an integer, and then assigns x to that value.
print(type(x))  # prints <class 'int'>, which means it's an integer

x = 1.5 + 2.3   # Expression on the right evaluates to 3.8, a float, and then assigns x to that value.
print(type(x))  # prints <class 'float'>

x = 1 + 2.3     # Expressions combining floats and ints generally evaluate to floats
print(type(x))  # prints <class 'float'>

x = 5 / 2       # In Python, an int divided by another int that is not divisible results in a float.
print(type(x))  # prints <class 'float'>

x = 5 // 2      # HOWEVER, integer division between 2 ints forces the result to be an integer (rounded down)
print(type(x))  # prints <class 'int'>

# x = "5" + 7     # This line will error, since Python does not know what you mean by this nonsense.  This is one of the most common issues new programmers face when dealing with strings and ints/floats, not keeping track of the types involved.

# An important extra type is the None type.  This is a special type that is reserved to mean a type that does not represent anything.
x = None
print(type(x))  # prints <class 'NoneType'>