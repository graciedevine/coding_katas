import math


def print_primes(n):
    for x in range(1, n + 1):
        prime = True
        for y in range(2, x):
            if x % y == 0:
                prime = False
        if prime:
            print(x)


print_primes(15)
