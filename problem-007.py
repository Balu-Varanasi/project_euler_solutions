"""

problem:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?

"""

from math import sqrt

max = 10001

count = 1
number = 3


def is_prime(n):
    """A function that checks whether the given number is prime or not"""
    if(n % 2 == 0):
        return 0
    root = int(sqrt(n))
    for i in range(3, root + 1):
        if(n % i == 0):
            return 0
    return 1

while(1):
    if is_prime(number):
        count += 1
    if count >= max:
        break
    number += 1

print number
