def two_highest(arg1):
    return sorted(set(arg1), reverse=True)[:2]


print(two_highest([15, 20, 20, 17]))
