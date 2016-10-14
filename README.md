# NormalASCII
Locate texts in numbers after the decimal point of a normal number

One could find any sequence of digits in base b in a [Normal Number](https://en.wikipedia.org/wiki/Normal_number) in base of at least b.

I originally wrote this script after reading new-age nonsenses on Quora  [(+)](https://www.quora.com/Since-the-base-10-expansion-of-pi-is-infinite-and-nonrepeating-does-every-possible-sequence-of-digits-exist-somewhere-in-it) about how all the information in the universe is encoded in $pi$ and how it's so special etc. Assuming the encoding scheme is mapping a digit to its ASCII value, one could show any possible number is by definition within a constant as trivial as Champernowne's which means there's nothing intrinsically/uniquely interesting about $pi$ with respect to information being encoded in it!

---

<h3> Implemented Constants: </h3>
- [Pi](https://en.wikipedia.org/wiki/Pi)
- [Champernowne constant](https://en.wikipedia.org/wiki/Champernowne_constant)


---
<h3> Dependencies </h3>
Assuming presence of Python 2.7 and a C compiler on the system:
- [gmpy2](https://pypi.python.org/pypi/gmpy2) and all of its dependencies.

<b>Remark:</b> If you're on Ubuntu or a Debian based distro, do `$sudo apt-get install python-gmpy2` instead of pip.

---
<h3> How to work with it </h3>
Clone this project and give executable permission to the main script and then run it.
