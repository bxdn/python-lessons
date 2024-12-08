# To print every element from a sequence, combine the "for" keyword with the list as follows:
my_tuple = 3, 6, 2, 10
for item in my_tuple:       # set a variable 'item' to each value in the list, then execute the indented block
    print(item + 1)         # prints 4, then 7, then 3, then 11

# Remember, strings are sequences
my_string = "Hi!"
for char in my_string:
    print('*' + char + '*') # prints '*H*', '*i*', '*!*'

# Combining loops and conditionals can be very powerful
my_tuple = [2, 10, 11, 6, 15, 1, 8]
for item in my_tuple:
    if item >= 10:
        print(item)         # prints ?

# To do something n times, use the range(n) function:
for i in range(5): # i will equal 0, 1, 2, 3, 4
    print('This will print 5 times!  Time #' + str(i)) # prints this message 5 times, with the time # increasing by 1 each iteration.

# range() supports arguments formatted much like the slicing [::] syntax: 
# If you want every other value going backward from 10 to 2 (2 not being included), you would use range(10, 2, -2), just as in slicing from index 10 to 2 every other item you would use [10:2:-2]
for i in range(10, 2, -2):
    print(i)