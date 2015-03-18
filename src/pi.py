import gmpy2


def generatorFunction():
    d = 1000000
    a = d
    while True:
        yield str(gmpy2.const_pi(a)).strip("3.")
        a += d
