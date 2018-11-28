# 5: Primality Distribution: Now, we are interested in calculating few
# statistics about prime number distribution.

# 5.1: Collect a prime number dataset, that is the list of prime numbers. Your
# dataset should have at least one million prime numbers.  You can either
# generate it with the functions you created above or download it.

# primes = list of primes (generate 1 million+)

from part2 import *

# 5.2.  Calculate the proportion of primes that ends with 1 (1 is the right
# digit)?  with 3?  with 7?  with 9?
def prop1(primes):
    prime1 = []
    i = 0
    while i < len(primes):
        if primes[i] % 10 == 1:
            prime1.append(primes[i])
        i = i + 1

    c = len(prime1) / len(primes)
    print("%.5s" % c, "of the first 1.5 million primes end in,", 1)

def prop3(primes):
    prime3 = []
    i = 0

    while i < len(primes):
        if primes[i] % 10 == 3:
            prime3.append(primes[i])
        i = i + 1

    c = len(prime3) / len(primes)
    print("%.5s" % c, "of the first 1.5 million primes end in,", 3)

def prop7(primes):

    prime7 = []
    i = 0

    while i < len(primes):
        if primes[i] % 10 == 1:
            prime7.append(primes[i])
        i = i + 1

    c = len(prime7) / len(primes)
    print("%.5s" % c, "of the first 1.5 million primes end in,", 7)

def prop9(primes):

    prime9 = []
    i = 0

    while i < len(primes):
        if primes[i] % 10 == 1:
            prime9.append(primes[i])
        i = i + 1

    c = len(prime9) / len(primes)
    print("%.5s" % c, "of the first 1.5 million primes end in,", 9)

# 5.3 Calculates proportions of primes ending in some digit a followed by primes ending in some digit b
def ends(primes, a, b):
    i = 0
    j = 0

    while i < len(primes) - 1:
        if primes[i] % 10 == a and primes[i + 1] % 10 == b:
            j = j + 1
        i = i + 1

    d = j / len(primes)
    print("%.5s" % d, "of the first 1.5 million primes ending with", a, "are followed by prime ending with", b)

# determines number of twin prime pairs in list of generated primes
def twins(primes):
    i = 0
    j = 0

    while i < len(primes) - 1:
        if (2 + primes[i]) == primes[i + 1]:
            j = j + 1
        i = i + 1

    print(j, "twin primes")

#Combines all stats generated in 5.2-5.4
# primes generated using sieve of Eratosthenes from Part 2
# this generates the first 1.5 million prime numbers (23,879,519 is 1.5 millionth prime)
def part5stats():
    print("generating 1 million primes...will take about two minutes")
    primes = sieve(23879519)
    prop1(primes)
    prop3(primes)
    prop7(primes)
    prop9(primes)
    ends(primes,1, 1)
    ends(primes,1, 3)
    ends(primes,1, 7)
    ends(primes,1, 9)

    ends(primes,3, 1)
    ends(primes,3, 3)
    ends(primes,3, 7)
    ends(primes,3, 9)

    ends(primes,7, 1)
    ends(primes,7, 3)
    ends(primes,7, 7)
    ends(primes,7, 9)

    ends(primes,9, 1)
    ends(primes,9, 3)
    ends(primes,9, 7)
    ends(primes,9, 9)

    twins(primes)





