"""

Problem:

How many letters would be needed to write all the numbers in words
from 1 to 1000?

"""


def to_word(n):
    """ Return the equivalent word for given number"""

    word_dict = {
          1: "one",
          2: "two",
          3: "three",
          4: "four",
          5: "five",
          6: "six",
          7: "seven",
          8: "eight",
          9: "nine",
         10: "ten",
         11: "eleven",
         12: "twelve",
         13: "thirteen",
         14: "fourteen",
         15: "fifteen",
         16: "sixteen",
         17: "seventeen",
         18: "eighteen",
         19: "nineteen",
         20: "twenty",
         30: "thirty",
         40: "forty",
         50: "fifty",
         60: "sixty",
         70: "seventy",
         80: "eighty",
         90: "ninety",
        100: "hundred",
       1000: "thousand"
    }

    word = ""

    a = [int(i) for i in str(n)[::-1]]

    if (len(a) == 4 and a[3] != 0):
        word = word_dict[a[3]] + " thousand "

    if (len(a) >= 3 and a[2] != 0):
        word += word_dict[a[2]] + " hundred"
        if (len(a) >= 2 and a[1] != 0):
            word += " and"
        elif len(a) >= 1 and a[0] != 0:
            word += " and"
    tens_position_value = 99

    if (len(a) >= 2 and a[1] != 0):
        tens_position_value = int(a[1]) * 10 + a[0]
        if tens_position_value <= 20:
            word += " " + word_dict[tens_position_value]
        else:
            word += " " + word_dict[(a[1] * 10)]

    if (len(a) >= 1 and a[0] != 0 and tens_position_value > 20):
        word += " " + word_dict[a[0]]

    return word.replace(" ", "")


def to_word_length(n):
    """Returns the length of the word"""
    return len(to_word(n))

print sum([to_word_length(i) for i in range(1, 1001)])
