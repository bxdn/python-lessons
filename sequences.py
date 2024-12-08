# To make an ordered collection of items, called a TUPLE, use the following syntax:
my_tuple = 1, 5, 3, 9 # creates a tuple called 'my_tuple' with the numbers 1, 5, 3, and 9, in that order
my_string_tuple = "Hello", "World" # creates a tuple called 'my_string_tuple' with the strings "Hello" and "World"

# To get the length of a tuple, use the len() function
print(len(my_tuple))     # prints 4
print(len(my_string_tuple)) # prints 2

# To extract a specific item from a list, use [] syntax:
print(my_tuple[0])       # Since indices begin at 0 in python, my_list[0] is 1, since 1 is the first element of my_list.  Prints 1
print(my_tuple[1])       # Prints 5
print(my_tuple[2])       # Prints 3
print(my_tuple[3])       # Prints 9

print(my_string_tuple[0] + ' ' + my_string_tuple[1]) # prints ?

# Strings can SOMETIMES be thought of tuples of single characters.  You can SOMETIMES use the same syntax as tuples for strings.
my_string = "Hello"
print(my_string[0])     # prints 'H'
print(my_string[1])     # prints 'e'

# The len() function also works with strings.
print(len(my_string))   # prints ?

# Python allows negative indexing.  Negative indices count from the back.
print(my_tuple[-1])      # prints 9
print(my_tuple[-2])      # prints ?
print(my_string[-1])    # prints ?

# Tuples and strings are examples of IMMUTABLE sequences (cannot be altered)
# A List is a MUTABLE sequence.

my_list = [1, 5, 3, 9] # creates a list called 'my_list' with the numbers 1, 5, 3, and 9, in that order
my_string_list = ["Hello", "World"] # creates a list called 'my_string_list' with the strings "Hello" and "World"

# To add an item to a list, use the "append()" method (A method is just a function associated to a specific object/type)
my_string_list.append("!")
# Note, there was no return type from append() or reassignment of the variable.  This is because the list itself was MUTATED, or changed.
# This is a subtle but important distinction: if ever some other variable was tied to this list, it also would change, because the underlying list changed.
print(my_string_list)   # prints ["Hello", "World", "!"]

# To remove the last item from a list, use the pop() method, which also returns that last element
x = my_string_list.pop()
print(x)                # prints "!"
print(my_string_list)   # prints ["Hello", "World"]

# To overwrite an item in the list, use the same syntax:
my_list[1] = 2
# Note this also mutates the list.
print(my_list[1])       # prints 2
print(my_list)          # now prints [1, 2, 3, 9]

# Be careful!  Other variables (or function arguments) that refer to the same list will ALSO be mutated when it is mutated elsewhere.
my_alias = my_list
my_list[-1] = 10
print(my_list)          # now prints [1 ,2, 3, 10]
print(my_alias)         # now ALSO prints [1 ,2, 3, 10]

def append_zero(lst):
    lst.append(0)

append_zero(my_list)
print(my_list)          # now prints [1 ,2, 3, 10, 0]
print(my_alias)         # now ALSO prints [1 ,2, 3, 10, 0]

# To get a copy of a list, use [:] syntax
my_copy = my_list[:]
my_list.pop()
my_list.pop()
print(my_list)          # now prints [1, 2, 3]
print(my_alias)         # now prints [1, 2, 3]
print(my_copy)          # still prints [1, 2, 3, 10, 0]

# The [:] syntax supports much more than just a full copy.  This is called a SLICE.
# The full syntax follows this schema [start:end:step]
# start - The first index to take - default 0
# end - The index AFTER the last index to take - default len(whatever_you're_slicing)
# step - How much to move forward: 1 is every item, 2 is every other item... - default 1
# You can use the defaults by omitting the numbers in the place they normally go
# So, my_str[:] is equivalent to my_str[0:len(my_str):1], which is a complete copy.
my_str = 'hello'
print(my_str[1:3])  # prints 'el'
print(my_str[2:])   # prints 'llo'
print(my_str[:4])   # prints 'hell'
print(my_str[::2])  # prints 'hlo'
print(my_str[::-1]) # prints 'olleh'