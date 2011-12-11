"""

Problem:

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

n = 0

for a in range(100, 999):
    for b in range(100, a):
        x = a * b
        if x > n:
            s = str(a * b)
            if s == s[::-1]:
                n = a * b

print n