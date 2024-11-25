# To make an ordered collection of items, called a LIST, use the following syntax:
my_list = [1, 5, 3, 9]  # creates a list called 'my_list' with the numbers 1, 5, 3, and 9, in that order
my_string_list = ["Hello", "World"] # creates a list called 'my_string_list' with the strings "Hello" and "World"

# To get the length of a list, use the len() function
print(len(my_list))     # prints 4
print(len(my_string_list)) # prints 2

# To add an item to a list, use the "append()" method
my_string_list.append("!")
print(my_string_list)   # prints ["Hello", "World", "!"]

# To remove the last item from a list, use the pop() method, which also returns that last element
x = my_string_list.pop()
print(x)                # prints "!"
print(my_string_list)   # prints ["Hello", "World"]

# To extract a specific item from a list, use [] syntax:
print(my_list[0])       # Since indices begin at 0 in python, my_list[0] is 1, since 1 is the first element of my_list.  Prints 1
print(my_list[1])       # Prints 5
print(my_list[2])       # Prints 3
print(my_list[3])       # Prints 9

print(my_string_list[0] + ' ' + my_string_list[1]) # prints ?

# To overwrite an item in the list, use the same syntax:
my_list[1] = 2
print(my_list[1])       # prints 2
print(my_list)          # now prints [1, 2, 3, 9]

# Strings can SOMETIMES be thought of lists of single characters.  You can SOMETIMES use the same syntax as lists for strings.
my_string = "Hello"
print(my_string[0])     # prints 'H'
print(my_string[1])     # prints 'e'

# The len() function also works with strings.
print(len(my_string))   # prints ?

# Note though, that strings are IMMUTABLE.  That means that strings can not be MUTATED, or altered. 
# Therefore, the following syntax would result in an error:
# my_string[1] = 'i'
# Also note that I am not referring to variable reassignment, but changing attributes of the string itself.  The following is still allowed because 'my_string' is now pointing to an entirely new string.
my_string = "World"

# Python allows negative indexing.  Negative indices count from the back.
print(my_list[-1])      # prints 9
print(my_list[-2])      # prints ?
print(my_string[-1])    # prints ?