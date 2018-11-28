import time

def printtable(file, table, space):
    for item in table:
        for num in item:
            string = str(num) + " "*((space+1)-len(str(abs(num))))
            file.write(string)
        file.write("\n")

def sieve(num):
    primes = dict()
    for i in range(2, num+1):
        primes[i] = True

    for i in primes:
        multiples = range(i,num+1, i)
        for j in multiples[1:]:
            primes[j] = False

    return [i for i in primes if primes[i] == True]

def generatenums(f, num):
    start_time = time.time()
    numbers = sieve(num)
    chunks = [numbers[x:x+100] for x in range(0, len(numbers), 100)]
    printtable(f, chunks, len(str(abs(numbers[-1]))))

    string = str(len(numbers)) + " primes generated" + "\n"
    f.write(string)
    f.write("Runtime: %.6s sec for primes up to %s" % ((time.time() - start_time), num))





