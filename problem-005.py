"""

Problem:

2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.
 
What is the smallest number that is evenly divisible by all of the numbers from
1 to 20?

"""

def gcd(a, b):

    """returns Greatest Common Divisor of given two integers 'a' and 'b'"""

    if(b == 0):
        return a

    return gcd(b, a % b)

def lcm(a, b):
    """return Least Common Factor of given two integers 'a' and 'b'"""
    return b * a / gcd(a, b)

ans = 2

for i in range(3, 20):
    ans = lcm(ans, i)

print ans 
