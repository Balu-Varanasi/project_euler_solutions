"""

Problem:

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum.

"""

from math import pow

n = 100

sum_of_squares = n * (n + 1) * (2 *  n + 1) / 6
square_of_sum = pow(n * (n + 1) / 2, 2)

print int(square_of_sum - sum_of_squares)