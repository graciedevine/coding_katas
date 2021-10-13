import random


def addtolist(int):
    list2 = []

    i = 0
    while i < int:
        list2.append(random.randint(0, 9))
        i += 1
    print(list2)


addtolist(6)
