"""
This file is part of NormalASCII.

    NormalASCII is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, Version 2.

    NormalASCII is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with PySchoenberg.  If not, see <http://www.gnu.org/licenses/>.
"""


import gmpy2
import math


def Constants_handler():
    """
    Implements the main interface for dealing with constants. If a constant
    doesn't have a closed form for deriving its digits then the generator
    `digit_finder` is used to sequentially generate them.

    Returns
    -------
    champernowne        str -> int
    pi                  str -> int
    """
    def digit_finder(converted_text, generator_name):
        """
        Searches each iteration of a generator for the string of digits. The
        reason that it is necessary to do two iteration is that it may find the
        digits in the last group of digits of the first iteration of the
        generator where convergence error is not sufficiently low. If it finds
        them in the next iteration, it means that the group of digits indeed
        belongs to the constant at the predicted place.
        Also, we must use a generator since not all constants have a closed form
        to search into.

        Parameters
        ----------
        converted_text          str
                                Castable to a long. Basically, it's the result
                                of replacing every character of a text with its
                                ascii value.
        generator_name          str

        Returns
        -------
        target_index            int
                                The n'th digit of the constant where the text is
                                found where n is `target_index`
        """
        generator = generator_name()
        index_upto_target = None
        while True:
            if converted_text in next(generator):
                try:
                    index_upto_target = next(generator).index(converted_text)
                except ValueError:
                    pass
                finally:
                    if index_upto_target is not None:
                        break
        target_index = index_upto_target + 1
        return target_index

    def champernowne(converted_text):
        """
        Champernowne constant is 0.12345678910111213141516...
        Basically adds the number of digits of all numbers less than argument
        'n' together. The math is obvious. Also notice that every sequence of
        digits would repeat infinitly many times in a normal number and this
        implementation would not return the index of the first appearance. In
        other words, if ascii value is 123, the first place that it appears is
        the first place, it also appears in ...122123124... and also appears in
        ...565741225657412356574124... etc. For the sake of simplicity, it'll
        not return the first appearance since I can't think of any
        straightforward formula for its closed form. Here, if the ascii
        representation is 'n', the index of 'n' which is appearing in
        ...[n-1][n][n+1]... is considered.

        Parameters
        ----------
        converted_text          str
                                Castable to a long. Basically, it's the result
                                of replacing every character of a text with its
                                ascii value.

        Returns
        -------
        target_index            int
        """
        number_of_digits = long(
            math.floor(gmpy2.log10(long(converted_text))) + 1)
        cursor = 1
        index_upto_target = 0
        while cursor < number_of_digits:
            index_upto_target += (pow(10, cursor) -
                                  pow(10, cursor - 1)) * cursor
            cursor += 1
        if cursor == number_of_digits:
            index_upto_target += (long(converted_text) -
                                  pow(10, cursor - 1)) * number_of_digits
        target_index = index_upto_target + 1
        return target_index


    def pi(converted_text):
        """
        Parameters
        ----------
        converted_text          str
                                Castable to a long. Basically, it's the result
                                of replacing every character of a text with its
                                ascii value.

        Returns
        -------
        target_index            int
                                The n'th digit of the constant where the text is
                                found where n is `target_index`
        """
        def pi_digit_generator():
            """
            A generator to sequentially get the digits of pi. Obviously not a
            true python generator but it's better to implement it in form of a
            python generator to use `digit_finder`.

            Yields
            ------
            -                   str
                                Castable to long, a slice of digits of pi except
                                the last couple of digits where it'd be an
                                approximation there.
            """
            d = 1000000
            cursor = d
            while True:
                yield str(gmpy2.const_pi(cursor)).strip("3.")
                cursor += d

        target_index = digit_finder(converted_text, pi_digit_generator)
        return target_index

    return pi, champernowne
