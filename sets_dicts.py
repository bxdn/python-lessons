# A set is an UNORDERED collection of UNIQUE elements.
# To create a set, use the {} syntax.

my_set = { 5, 2, 4 }

# To add to a set, use the "add()" method

my_set.add(6)
print(my_set)               # prints {2, 4, 5, 6}

# Notice that adding 6 again would do nothing, as 6 is already in the set, and a set is made of UNIQUE elements.
my_set.add(6)
print(my_set)               # still prints {2, 4, 5, 6}

# This line would fail, since a set is unordered. So it would be very silly to ask for the "first" element.
# print(my_set[0])

# You can see if an item is in the set by using the 'in' keyword
print(6 in my_set)          # prints True
print(100 in my_set)        # prints False

# A dictionary is an UNORDERED mapping of UNIQUE KEYS to NON-UNIQUE VALUES.
# To create a dictionary, use the {:} syntax.  Also, an empty {} will create an empty dictionary.

my_dict = {}
print(type(my_dict)) # prints <class 'dict'>
# Here, the string 'one' is a key, and the int 1 is the value corresponding to that key.
my_dict = {'one': 1, 'two': 2, 'three': 3}
print(type(my_dict)) # prints <class 'dict'>

# You can get the value of the dictionary at a specific key by using the standard [] indexing syntax, but keys, rather than indices, are used.
x = my_dict['one']
print(x)                    # prints 1

# This line will fail, as 'four' is not a key in the dictionary
# x = my_dict['four']

# You can add/overwrite a key/value to a dictionary using [] notation
my_dict['four'] = 5
print(my_dict['four'])      # prints 5
my_dict['four'] = 4
print(my_dict['four'])      # prints 4

# You can delete a value from a dictionary using the "del" keyword
del my_dict['four']

# You can similarly use the 'in' keyword to see if a KEY is in the dictionary
print('one' in my_dict)     # prints True
print('four' in my_dict)    # prints False
print(3 in my_dict)         # prints ?