# 3: Primality Test: Implement three primality test
# functions using the two following approaches:

import math

# 3.1: Trial division: For an input n, check if there is a prime number between 2
# and √n that divides n
def trial(n):

	a = 2
	b = math.ceil(math.sqrt(n))

	while a <= b:
		if (n%a == 0):
			a = b + 2
		else:
			a = a + 1

	if a == b + 1:
		print(n, "is prime \n")
	else:
		print(n, "is not prime \n")

# 3.2: Using Sieve of Eratosthenes.

# Helper function for eratosthenes that works like trial(n) but does not print anything
def trial_erat(n):

	a = 2
	b = math.ceil(math.sqrt(n))

	while a <= b:
		if (n%a == 0):
			a = b + 2
		else:
			a = a + 1

	if a == b + 1:
		return True
	else:
		return False

def eratosthenes(n):

	c = 2
	d = math.ceil(math.sqrt(n))
	myList = []

	while(c <= d):
		if (trial_erat(c) == True):
			myList.append(c)
		c = c + 1

	i = 0
	while i < len(myList):
		primey = myList[i]

		if n%primey == 0:
			print(n, "is not prime \n")
			i = len(myList) + 20
		else:
			i = i + 1

	if i <= len(myList):
		print(n, "is prime \n")

# 3.3: Fermat little theorem BONUS.
def flt(p):
	a = 1

	while a < p:
		if (a**p)%p != a%p:
		#	print("not prime, a = ", a)
			a = p + 20

		else:
	#		print("could be prime: a =", a)
			a = a + 1

	if a > p + 10:
		print(p, "is not prime \n")
	else:
		print(p, "is prime \n")
