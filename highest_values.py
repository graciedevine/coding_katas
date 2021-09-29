# In this kata, your job is to return the two distinct highest values in a list. If there're less than 2 unique values,
# return as many of them, as possible.

# The result should also be ordered from highest to lowest.

# Examples:

# [4, 10, 10, 9]  =>  [10, 9]
# [1, 1, 1]  =>  [1]
# []  =>  []

# My algorithm
# create a new list
# iterate though, look for two highest values max()?
# append two highest values to new list
# create a set from list - order from highest to lowest sort()?


def two_highest(arg1):
    highest_int = max(arg1)
    arg1.remove(highest_int)

    second_highest_int = max(arg1)
    return sorted([highest_int] + [second_highest_int], reverse=True)


print(two_highest([15, 20, 20, 17]), [20, 17])
