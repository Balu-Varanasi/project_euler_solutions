"""
Problem:

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

import math

def is_prime(n):
    """A function that checks wheather a given number is prime or not"""
    if(n%2 == 0):
        return 0
    for i in range(3,int(math.sqrt(n))+1):
        if(n%i == 0):
            return 0
    return 1

sum = 2

for i in range(3, 2000000):
    if is_prime(i):
        sum += i

print sum