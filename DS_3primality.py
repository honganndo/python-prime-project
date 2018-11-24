# 3: Primality Test: Implement three primality test 
# functions using the two following approaches:

import math
import numpy as np

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

trial(8)
trial(827)
trial(83)


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

	print(myList, "\n")

eratosthenes(5)
eratosthenes(20)
eratosthenes(37)

# 3.3: Fermat little theorem BONUS.
#def flt()



