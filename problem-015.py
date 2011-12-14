"""

Problem:

Starting in the top left corner of a 2x2 grid, there are 6 routes
(without backtracking) to the bottom right corner.

How many routes are there through a 20x20 grid?

Logic:

    For a MxN grid there are (M+N) available positions and we need
    to choose N or M positions. Note choosing either M or N results
    in the same result:

    (m + n)! / n! (m + n - n)! = (m + n)! / m! (m + n - m)!
    => (m + n)! / n!m! = (m + n)! / m!n!

"""


def factorial(n):
    """Function which calculates the Factorial of given number"""
    if n == 0:
        fact = 1
    else:
        fact = n * factorial(n - 1)
    return fact

print factorial(20 + 20) / (factorial(20) * factorial(20))
