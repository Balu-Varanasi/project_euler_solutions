'''

Problem:

If 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26,

then what is the sum of the digits of the number 2^1000?


'''

def digits(n):

    """Calculates the sum of digits in the given integer"""

    sum_of_digits = 0

    while n > 0:
        sum_of_digits = sum_of_digits + (n % 10)
        n = n / 10

    return sum_of_digits

print digits(2 ** 1000)
