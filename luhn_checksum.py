def sum_digits(n):
    n = str(n)
    li = [n]
    list_separated = "".join(li)
    list_digits = int(list_separated)
    return sum(list_digits)


print(sum_digits(176248))
