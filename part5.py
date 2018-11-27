# 5: Primality Distribution: Now, we are interested in calculating few 
# statistics about prime number distribution.

# 5.1: Collect a prime number dataset, that is the list of prime numbers. Your
# dataset should have at least one million prime numbers.  You can either
# generate it with the functions you created above or download it.

#primes = list of primes (generate 1 million+)

# 5.2.  Calculate the proportion of primes that ends with 1 (1 is the right
# digit)?  with 3?  with 7?  with 9?

# Determines the last digit of a number

def prop1():
	primes = [2,3,5,7,11,13,17,19,23,29]

	prime1 = []
	i = 0
	
	while i < len(primes):
		if primes[i]%10 == 1:
			prime1.append(primes[i])
		i = i + 1

	c = len(prime1)/len(primes)
	print(c)

prop1()

def prop3():
	primes = [2,3,5,7,11,13,17,19,23,29]

	prime3 = []
	i = 0
	
	while i < len(primes):
		if primes[i]%10 == 3:
			prime3.append(primes[i])
		i = i + 1

	c = len(prime3)/len(primes)
	print(c)

prop3()

def prop7():
	primes = [2,3,5,7,11,13,17,19,23,29]

	prime7 = []
	i = 0
	
	while i < len(primes):
		if primes[i]%10 == 7:
			prime7.append(primes[i])
		i = i + 1

	c = len(prime7)/len(primes)
	print(c)

prop7()

def prop9():
	primes = [2,3,5,7,11,13,17,19,23,29]

	prime9 = []
	i = 0
	
	while i < len(primes):
		if primes[i]%10 == 9:
			prime9.append(primes[i])
		i = i + 1

	c = len(prime9)/len(primes)
	print(c)

prop9()

# determines number of twin prime pairs in list of generated primes
def twins():
	# primes generated using sieve of Eratosthenes from Part 2
	primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]   
	i = 0
	j = 0  

	while i < len(primes) - 1:
		if (2 + primes[i]) == primes[i + 1]:
			j = j + 1
		i = i + 1

	print(j, "twin primes")

twins()



