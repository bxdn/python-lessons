# To make an ordered collection of items, called a LIST, use the following syntax:
my_list = [1, 5, 3, 9]  # creates a list called 'my_list' with the numbers 1, 5, 3, and 9, in that order
my_string_list = ["Hello", "World"] # creates a list called 'my_string_list' with the strings "Hello" and "World"

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

# Strings can be thought of lists of single characters.  You can use the same syntax as lists for strings.
my_string = "Hello"
print(my_string[0])     # prints 'H'
print(my_string[1])     # prints 'e'

# Python allows negative indexing.  Negative indices go from the back.
print(my_list[-1])      # prints 9
print(my_list[-2])      # prints ?
print(my_string[-1])    # prints ?