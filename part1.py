
# 1: Euclid's Algorithm. The below program uses Euclid's algorithm to compute
# the GCD of two integers

import numpy as np

def gcd(a, b):
        x = a
        y = b

        if a >= b:
                r = a - b

        else:
                r = a

        while r >= 0:
                print("a =", a, "b =", b, "r =", r)
                r = a % b

                if r != 0:
                        a = b
                        b = r

                else:
                        r = -1

        print("The gcd of ", x, "and", y, "is equal to", b,"\n")
