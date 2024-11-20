# To repeat an action, use the "for" keyword:
for i in range(3): # execute with i having number values 0, then 1, then 2
    print(i)            # prints '0', then '1', then '2'

# To print every element from the list, combine the "for" keyword with the list as follows:
my_list = [3, 6, 2, 10]
for item in my_list:    # set a variable 'item' to each value in the list, then execute the indented block
    print(item)         # prints '3', then '6', then '2', then '10'

# Combining for and if structures can be very powerful
my_list = [2, 10, 11, 6, 15, 1, 8]
for item in my_list:
    if item >= 10:
        print(item)     # prints ?