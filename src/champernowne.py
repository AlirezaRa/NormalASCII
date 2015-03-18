import gmpy2
import math


def digitFinder(n):
    # Basically adds the number of digits of all numbers less than argument 'n'
    # together. The math is obvious.
    d = long(math.floor(gmpy2.log10(long(n))) + 1)
    i = 1
    result = 0
    while i < d:
        result += (pow(10, i) - pow(10, i - 1))*i
        i += 1
    if i == d:
        result += (long(n) - pow(10, i - 1))*d
    return (result + 1)
