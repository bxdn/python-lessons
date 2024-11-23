# To print every element from the list, combine the "for" keyword with the list as follows:
my_list = [3, 6, 2, 10]
for item in my_list:    # set a variable 'item' to each value in the list, then execute the indented block
    print(item)         # prints '3', then '6', then '2', then '10'

# Same goes for strings
my_string = "Hi!"
for char in my_string:
    print(char)         # prints 'H', 'i', '!'

# Combining loops and conditionals can be very powerful
my_list = [2, 10, 11, 6, 15, 1, 8]
for item in my_list:
    if item >= 10:
        print(item)     # prints ?

