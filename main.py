import time
import sys
from part1 import *
from part2 import *
from part3 import *
from part4 import *

def main():
    file = open('output.txt', 'w')
    print("starting Discrete Math Prime Numbers Project")
    print("Choose from the following options:")
    print("1 - GCD of two integers")
    print("2 - Prime number generation up to user input n")
    print("3 - Primality test")
    print("4 - Prime factorization")
    print("5 - who the fuck knows")
    print("q - quit")
    choice = input("Choice: ")
    if(choice == '1'):
        print("You have chosen GCD function")
        numinput1 = input("Enter your first number: ")
        numinput2 = input("Enter your second number: ")
        gcd(int(numinput1), int(numinput2))
    elif(choice == '2'):
        print("You have chosen prime number generation")
        numinput = input("Enter a integer n to generate primes up to: ")
        print("Outputting primes and table to output.txt")
        generatenums(file, int(numinput))
    elif(choice == '3'):
        print("You have chosen the primality test")
        print("Choose which option for the primality test you want to use")
        print("1 - Trial division")
        print("2 - Sieve of Eratosthenes")
        userinput = input("Your choice: ")
        if(userinput == '1'):
            num = input("Enter number to check: ")
            trial(int(num))
        elif(userinput == '2'):
            num = input("Enter number to check: ")
            eratosthenes(int(num))
        else:
            print("Enter valid input")
    elif(choice == '4'):
        print("You chose prime factorization")
        uinput = input("Enter num: ")
        trialdivision(int(uinput))
    #elif(choice == 5):
        #maybe maybe not
    elif(choice == 'q'):
        print("Quitting program")
        sys.exit()
    else:
        print("Enter a valid choice")

if __name__ == '__main__':
    main()