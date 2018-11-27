# 5: Primality Distribution: Now, we are interested in calculating few 
# statistics about prime number distribution.

# 5.1: Collect a prime number dataset, that is the list of prime numbers. Your
# dataset should have at least one million prime numbers.  You can either
# generate it with the functions you created above or download it.

#primes = list of primes (generate 1 million+)

# 5.2.  Calculate the proportion of primes that ends with 1 (1 is the right
# digit)?  with 3?  with 7?  with 9?

# primes generated using sieve of Eratosthenes from Part 2
# this generates the first 1.5 million prime numbers (23,879,519 is 1.5 millionth prime)
primes = sieve(23879519) 

def prop1():
	primes = sieve(23879519)
	prime1 = []
	i = 0
	
	while i < len(primes):
		if primes[i]%10 == 1:
			prime1.append(primes[i])
		i = i + 1

	c = len(prime1)/len(primes)
	print(c, "of the first 1.5 million primes end in," 1)
prop1()

def prop3():
	primes = sieve(23879519)
	prime3 = []
	i = 0
	
	while i < len(primes):
		if primes[i]%10 == 3:
			prime3.append(primes[i])
		i = i + 1

	c = len(prime1)/len(primes)
	print(c, "of the first 1.5 million primes end in," 3)	
prop3()

def prop7():
	primes = sieve(23879519)
	prime7 = []
	i = 0
	
	while i < len(primes):
		if primes[i]%10 == 1:
			prime7.append(primes[i])
		i = i + 1

	c = len(prime1)/len(primes)
	print(c, "of the first 1.5 million primes end in," 7)
prop7()

def prop9():
	primes = sieve(23879519)
	prime9 = []
	i = 0
	
	while i < len(primes):
		if primes[i]%10 == 1:
			prime9.append(primes[i])
		i = i + 1

	c = len(prime9)/len(primes)
	print(c, "of the first 1.5 million primes end in," 9)
prop9()

# 5.3 Calculates proportions of primes ending in some digit a followed by primes ending in some digit b
def ends(a,b):     
	primes = sieve(23879519)   
	i = 0
	j = 0  

	while i < len(primes) - 1:
		if primes[i]%10 == a and primes[i + 1]%10 == b:
			j = j + 1
		i = i + 1

	d = j/len(primes)
	print(d, "of the first 1.5 million primes ending with", a, "are followed by prime ending with", b)

ends(1,1)
ends(1,3)
ends(1,7)
ends(1,9)

ends(3,1)
ends(3,3)
ends(3,7)
ends(3,9)

ends(7,1)
ends(7,3)
ends(7,7)
ends(7,9)

ends(9,1)
ends(9,3)
ends(9,7)
ends(9,9)


# determines number of twin prime pairs in list of generated primes
def twins():
	primes = sieve(23879519) 
	i = 0
	j = 0  

	while i < len(primes) - 1:
		if (2 + primes[i]) == primes[i + 1]:
			j = j + 1
		i = i + 1

	print(j, "twin primes")

twins()



