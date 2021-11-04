# write a script that finds and prints all prime numbers up to 100


def print_primes(n):
    for x in range(1, n + 1):
        for y in range(1, x):
            if x % y == 0:
                print(x)


print_primes(21)
