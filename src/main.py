import champernowne
import pi

approxConstants = set(["pi"])
closedConstants = set(["champernowne"])
constants = approxConstants | closedConstants


def text2digit(t):
    return ''.join(map((lambda x: str(ord(x))), list(str(t))))


def digitFinderApprox(text, constant):
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
    text = str(raw_input("Anything more than around 4-5 letters may quite a " +
                         "while to compute. Also, using uppercase letters " +
                         "increases the probability of reaching the result " +
                         "in an acceptable amount of time since number of " +
                         "digits would be lower according to ascii table\n" +
                         "\nConsidering above, Enter your text: "))
    cte = None
    while cte not in constants:
        cte = str(raw_input("The implemented constants are " +
                            ", ".join([str(e) for e in constants]) + "." +
                            "\nEnter your choice from above: "))
    print ("Computing...")
    if cte in approxConstants:
        r = digitFinderApprox(text, cte)
    elif cte in closedConstants:
        d = text2digit(text)
        r = globals()[cte].digitFinder(d)
    print (str(text) + " is found on " + str(r) + "th digit after " + str(cte) +
           "'s decimal point!")
