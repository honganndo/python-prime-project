import math

def trialdivision(num):
    factor = []
    while num % 2 == 0:
        factor.append(2)
        num = num / 2
    for i in range(3, (int(math.sqrt(num)) + 1), 2):
        while num % i == 0:
            factor.append(int(i))
            num = num / i
    if num > 2:
        factor.append(int(num))
    print(*factor, sep = " ")

