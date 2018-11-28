import time
import sys
import random
from part1 import *
from part2 import *
from part3 import *
from part4 import *
from part5 import *

def timetable(f, function, *args):
    print("----------Generating table in output.txt-------------")
    i = 1
    numbers = [("input", "runtime (sec)")]
    item = args[0]
    while (i <= item):
        starttime = time.time()
        if(len(args) == 1):
            int1 = random.randint(i, i*10)
            function(int1)
            leftovertime = time.time() - starttime
            numbers.append((int1, '%.9f' % leftovertime))
        elif(len(args) == 2):
            int1 = random.randint(i, i*10)
            int2 = random.randint(i, i*10)
            function(int1, int2)
            s = str(int1) + ", " + str(int2)
            leftovertime = time.time() - starttime
            numbers.append((s, '%.9f' % leftovertime))
        i = i*10
    f.write("\n")
    for ele1, ele2 in numbers:
        f.write("{:<23}{:<15}".format(ele1, ele2))
        f.write("\n")

def main():
    file = open('output.txt', 'w')
    print("starting Discrete Math Prime Numbers Project")
    print("Choose from the following options:")
    print("1 - GCD of two integers")
    print("2 - Prime number generation up to user input n")
    print("3 - Primality test")
    print("4 - Prime factorization")
    print("5 - Statistics")
    print("q - quit")
    choice = input("Enter Choice: ")
    if(choice == '1'):
        print("You have chosen GCD function")
        numinput1 = input("Enter your first number: ")
        numinput2 = input("Enter your second number: ")
        gcd(int(numinput1), int(numinput2))
        timetable(file, gcd, 100000000, 100000000)
    elif(choice == '2'):
        print("You have chosen prime number generation")
        numinput = input("Enter a integer n to generate primes up to: ")
        print("Outputting primes and table to output.txt")
        generatenums(file, int(numinput))
        timetable(file, sieve, 1000000)
    elif(choice == '3'):
        print("You have chosen the primality test")
        print("Choose which option for the primality test you want to use")
        print("1 - Trial division")
        print("2 - Sieve of Eratosthenes")
        print("3 - Fermat little theorem")
        userinput = input("Your choice: ")
        if(userinput == '1'):
            num = input("Enter number to check: ")
            trial(int(num))
            timetable(file, trial, 100000000000)
        elif(userinput == '2'):
            num = input("Enter number to check: ")
            eratosthenes(int(num))
            timetable(file, eratosthenes, 10000000000)
        elif(userinput == '3'):
            num = input("Enter number to check: ")
            flt(int(num))
            timetable(file, flt, 1000000000)
        else:
            print("Enter valid input")
    elif(choice == '4'):
        print("You chose prime factorization")
        uinput = input("Enter num: ")
        trialdivision(int(uinput))
        timetable(file, trialdivision, 1000000000000000)
    elif(choice == 5):
        print("You chose generate statistics for primes")
        part5stats()
    elif(choice == 'q'):
        print("Quitting program")
        sys.exit()
    else:
        print("Enter a valid choice")

    file.close()

if __name__ == '__main__':
    main()