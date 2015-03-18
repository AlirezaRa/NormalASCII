import gmpy2


def generatorFunction():
    # produces more digits of Pi after each iteration. Please notice that this
    # is not exactly a python generator function since it does not start where
    # it was in the last iteration. The reason is that implementing Chudnovsky's
    # algorithm in python in order to efficiently use the generator capabilities
    # is less efficient that implementing it in C (which is done here by gmpy2).
    # The reason that this is in the form of generatorFunction is that if in the
    # future I want to add another constant which is not implemented yet and is
    # to be approximated with infinite series, generator functions are the best
    # way to do that and I don't want to rewrite the digitFinderApprox in
    # main.py again and treat "pi" differently than others!
    d = 1000000
    a = d
    while True:
        yield str(gmpy2.const_pi(a)).strip("3.")
        a += d
