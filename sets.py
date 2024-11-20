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