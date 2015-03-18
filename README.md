# NormalASCII
Locate texts in numbers after the decimal point of a normal number

One could find any sequence of digits in base b in a [Normal Number](https://en.wikipedia.org/wiki/Normal_number) in base of at least b.
Considering above, This is a fun little project for finding information in form of text (each character mapped to its ascii value, hence the name) inside the numbers after the decimal point of a normal number in base 10.

It was originally motivated after reading new-age nonsense on the internet [+](https://www.quora.com/Since-the-base-10-expansion-of-pi-is-infinite-and-nonrepeating-does-every-possible-sequence-of-digits-exist-somewhere-in-it)about how all the information on the universe is encoded in $pi$ and how it's so special and all that jazz. Well, it really is something special, but not necessarily for that reason since every other normal number also behaves that way and almost all numbers are normal, notwithstanding some of them are also proved to be normal number whereas $pi$ is conjectured to be.

---

<h3> Implemented Constants: </h3>
- [Pi](https://en.wikipedia.org/wiki/Pi)
- [Champernowne constant](https://en.wikipedia.org/wiki/Champernowne_constant)


---
<h3> Dependencies </h3>
Assuming presence of Python 2.7 and a C compiler on the system:
- [gmpy2](https://pypi.python.org/pypi/gmpy2) and all of its dependencies.

<b>Remark:</b> If you're on Ubuntu `$sudo apt-get install python-gmpy2` does the job. 

<b>Remark:</b> This program has only been tested on Ubuntu, though theoretically it should work on Linux or OS X. Windows also, iff there's no wierd python problems in there!

---
<h3> How to work with it </h3>
Clone this project or download it as zip (link to your right). Then ``` cd ~/PATH-TO-MAIN-FOLDER/NormalASCII/src/ ``` then ``` python main.py```.
