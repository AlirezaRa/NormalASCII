import champernowne
import pi
import constantList

constants = constantList.approx | constantList.closed


def text2digit(t):
    # Returns a string equivalent of mapping each charachter of t to its ascii
    # value. Notice that the mapping is not necessarily bijective.
    return ''.join(map((lambda x: str(ord(x))), list(str(t))))


def digitFinderApprox(text, constant):
    # Searches each iteration of a generator for the string of digits. The
    # reason that it is necessary to do two iteration is that it may find the
    # digits in the last group of digits of the first iteration of the generator
    # where convergence error is not sufficiently low. If it find them the next
    # iteration, it means that the group of digits indeed belongs to the
    # constant at the predicted place.
    txt = text2digit(text)
    generator = pi.generatorFunction()
    index = None
    while True:
        if txt in next(generator):
            try:
                index = next(generator).index(txt)
            except ValueError:
                pass
            finally:
                if index is not None:
                    break
    return (index + 1)


if __name__ == "__main__":
    text = str(raw_input("Anything more than around 4-5 letters for constants" +
                         " in approx categeory may take quite a while to " +
                         "compute. Also, for them, using uppercase letters " +
                         "increases the probability of reaching the result " +
                         "in an acceptable amount of time since number of " +
                         "digits would be lower according to ascii table\n" +
                         "\nConsidering above, Enter your text: "))
    cte = None
    while cte not in constants:
        cte = str(raw_input("The implemented approx constants are " +
                            ", ".join(["'" + str(e) + "'"
                                       for e in constantList.approx]) +
                            " and the implemented closed constants are " +
                            ", ".join(["'" + str(e) + "'"
                                       for e in constantList.closed]) +
                            "." + "\nEnter your choice from above: "))
    print ("Computing...")
    if cte in constantList.approx:
        r = digitFinderApprox(text, cte)
    elif cte in constantList.closed:
        # r basically calls the module.digitFinder(d) by the string name of that
        # module.
        d = text2digit(text)
        r = globals()[cte].digitFinder(d)
    print (str(text) + " is found on " + str(r) + "th digit after " + str(cte) +
           "'s decimal point!")
