# 3: Primality Test: Implement three primality test 
# functions using the two following approaches:

import math

# 3.1: Trial division: For an input n, check if there is a prime number between 2 
# and √n that divides n
def trial(n):

	a = 2
	b = math.ceil(math.sqrt(n))

	while a < b:
		if (n%a == 0):
			a = b + 1
		else:
			a = a + 1

	if a == b:
		print(n, "is a prime number \n")
	else:
		print(n, "is not prime \n") 

# 3.2: Using Sieve of Eratosthenes.
def eratosthenes(n):

	a = 2
	myList = []

	while(a <= n):
		myList.append(a)
		a = a + 1

	c = 2
	d = 3
	while (c < a):
		
		while(d < a):
			if (d%c == 0) and d in myList:
				myList.remove(d)
			d = d + 1

		c = c + 1
		d = c + 1

	i = 0
	while i < len(myList):
		if n%myList[i] == 0 and n != myList[i]:
			print(n, "is not prime")
			i = len(myList) + 1
		else:
			i = i + 1

	if i == len(myList):
		print(n, "is prime")
		

# 3.3: Fermat little theorem BONUS.
def flt(p):
	a = 1

	while a < p:
		if (a**p)%p != a%p:
			print("not prime, a = ", a)
			a = p + 20

		else:
			print("could be prime: a =", a)
			a = a + 1

	if a > p + 10:
		print(p, "is not prime \n")
	else:
		print(p, "is prime \n")
