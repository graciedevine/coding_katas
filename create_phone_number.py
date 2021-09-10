# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a
# phone number.

# Example
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"


def create_phone_number(n):
    # x = len(int(n[""]))
    # if x != 10:
    #     return False
    phone_number = []
    phone_number.append(n)
    print(phone_number)


create_phone_number("7572409402")
# input array
# check length of input
# check that input is int
# add () around first three numbers
# add space after ()
# seven numbers separated by "-" after ()
