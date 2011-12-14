"""

Problem:

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.

"""


def fib_sequence(max_number):
    """ Generates Fibonacci Sequence as a list, upto given 'maximum' number"""
    first_term = 1
    second_term = 2

    fib_list = []

    while second_term < max_number:
        first_term, second_term = second_term, first_term + second_term
        fib_list.append(first_term)

    return fib_list

print sum([i for i in fib_sequence(4000000) if (i % 2) == 0])
