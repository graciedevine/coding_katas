# Define a function that removes duplicates from an array of numbers and returns it as a result.
# The order of the sequence has to stay the same.

# create empty array
# iterate through each value
# if duplicate pop()
# return the value


def distinct(seq):
    new_list = []
    for elem in seq:
        if not elem in new_list:
            new_list.append(elem) # append, not pop. We don't need to delete anything.
    return new_list


print(distinct([1, 2, 3, 4, 5, 2, 3, 4, 7, 9, 5]))
