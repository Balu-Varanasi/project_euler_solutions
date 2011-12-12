"""

Problem:

Find the sum of digits in 100!

"""

def digits(n):
    """Function which calculates the number of digits in a given number"""
    nd = 0  # Let the number of digits in the given number is zero.
    while n > 0:
        nd = (n % 10) + nd
        n = n / 10
    return nd

def factorial(n):
    """Function which calculates the Factorial of given number"""
    if n == 0:
        fact = 1
    else:
        fact = n * factorial(n-1)

    return fact

print "The number of digits in 100! is ... %s" % digits(factorial(100))
