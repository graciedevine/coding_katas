"""Write one line of Python that takes this list and makes a new list that has only the even elements
of this list in it."""

# numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# even_numbers = []
# for number in numbers:
#     if number %2 == 0:
#         even_numbers.append(number)
# print(even_numbers)

numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)
