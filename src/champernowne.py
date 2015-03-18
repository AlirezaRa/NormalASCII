import gmpy2
import math


def digitFinder(n):
    # Champernowne constant is 0.12345678910111213141516...
    # Basically adds the number of digits of all numbers less than argument 'n'
    # together. The math is obvious. Also notice that every sequence of digits
    # would repeat infinitly many times in a normal number and this
    # implementation would not return the index of the first appearance. In
    # other words, if ascii value is 123, the first place that it appears is the
    # first place, it also appears in ...122123124... and also appears in ...
    # 565741225657412356574124... etc. For the sake of simplicity, it'll not
    # return the first appearance since I can't think of any straightforward
    # formula for its closed form. Here, if the ascii representation is 'n', the
    # index of 'n' which is appearing in ...[n-1][n][n+1]... is considered.
    # To get the first apperance, one needs to implement its generator using
    # its infinite series representation which would be too inefficient to
    # consider when one has a closed formula.
    d = long(math.floor(gmpy2.log10(long(n))) + 1)
    i = 1
    result = 0
    while i < d:
        result += (pow(10, i) - pow(10, i - 1))*i
        i += 1
    if i == d:
        result += (long(n) - pow(10, i - 1))*d
    return (result + 1)
