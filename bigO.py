# An algorithm (just a specialized program to deal with data)
# can be said to have a 'time complexity' which we quantify using "big O" notation.
# An algorithm can be said to be O(n) where n is the length of some input
# when the algorithm takes at most a * n instructions to execute, where a is a constant number every time the algorithm is called.
# That means the following algorithms are O(n):

def find_index(my_list, to_find):
    for i, item in enumerate(my_list):
        if item == to_find:
            return i
        
def is_present(my_list, to_find):
    for item in my_list:
        if item == to_find:
            return True
    return False

# Note this is still O(n), even though the loop happens twice.
def double_check(my_list, to_find):
    first_check = False
    second_check = False
    for item in my_list:
        if item == to_find:
            first_check = True
    for item in my_list:
        if item == to_find:
            second_check = True
    return first_check and second_check

# An algorithm is O(n^2) when there is a nested loop of the same list, because there are at most a * n * n instructions.
def find_summing_indices(my_list, goal):
    for i, first in enumerate(my_list):
        for j, second in enumerate(my_list):
            if first + second == goal:
                return (i, j)
    return None

# An algorithm is O(n * m) when there is a nested loop of different lists, one of length n and one of length m, because there are at most a * m * n instructions.
def find_shared_item(l1, l2):
    for l1_item in l1:
        for l2_item in l2:
            if l1_item == l2_item:
                return l1_item
    return None

# An algorithm is O(n + m) when there are non-nested loops of both lists, because there are at most a * (m + n) instructions
def is_present_in_either(l1, l2, to_find):
    for item in l1:
        if item == to_find:
            return True
    for item in l2:
        if item == to_find:
            return True
    return False

# An algorithm is O(1) when there are no loops in the algorithm dependant on the length of the input.
def is_contained_in_first_5(my_list, to_find):
    for i in range(min(len(my_list), 5)): # This loop does not count towards the time complexity because the loop's iteration count caps at 5, which is not impacted by the length of the list
        if my_list[i] == to_find:
            return True
    return False

# An algorithm's time complexity is only dependent on the highest order part, so for instance, the following algorithm's time complexity is O(n^2), not O((n^2) + n)
def remove_instance_of_first_duplicated_value(my_list):
    to_remove = None
    # This nested loop is O(n^2)
    for i, item in enumerate(my_list):
        for j, other in enumerate(my_list):
            if item == other and i != j:
                to_remove = item
                break
    if to_remove:
        # Even though list.remove() is O(n), because the above loop is of a higher order, it is ignored in determining the time complexity.
        my_list.remove(to_remove)

# Common data structures and their operations' time complexities:
# 
# LIST:
# .append() - O(1)
# .pop() (no argument provided) - O(1)
# .pop(0) - O(n)
# + - O(n)
# .extemd() - O(m) - time complexity is based on length of argument
# [:::] - O(n) - time complexity is based on the number of elements sliced
# len() - O(1)
# in - O(n)
# index(), insert(), remove(), clear(), count() - O(n)
# del - O(n)
# 
# STRING:
# + - O(n)
# lower(), upper(), capitalize(), etc - O(n)
# .join() - O(n * m) - time complexity is based on length of argument * length of original string
# [:::] - O(n) - time complexity is based on the number of elements sliced
# len() - O(1)
# in - O(n)
#
# SET:
# set() - O(m) - time complexity is based on length of argument
# .add() - O(1)
# .remove() - O(1)
# &, <=, - - O(n)
# |, ^ - O(n + m) - time complexity is based on the sum of both sets' lengths
# len() - O(1)
# in - O(1)
#
# DICT:
# x = d[key], .get() - O(1)
# d[key] = x - O(1)
# len() - O(1)
# in - O(1)
# del - O(1)