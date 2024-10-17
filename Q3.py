#The prime factors of 13195 are 5, 7, 13 and 29.
import math
#What is the largest prime factor of the given number?


def is_Prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    sqrt_num = math.ceil(math.sqrt(number))
    for i in range(3, sqrt_num+1, 2):
        if not number%i:
            return False
    return True

def largePrimeNumber(number):
    for i in range(number, 0, -2):
        if is_Prime(i) and number%i == 0:
            return i


print(largePrimeNumber(2))

