# -*- coding: utf-8 -*-

"""Convert to and from Roman numerals"""

import re


# Define exceptions


class RomanError(Exception):
    pass


class OutOfRangeError(RomanError):
    pass


class NotIntegerError(RomanError):
    pass


class InvalidRomanNumeralError(RomanError):
    pass


# Define digit mapping
romanNumeralMap = (
    ('M', 1000),
    ('CM', 900),
    ('D', 500),
    ('CD', 400),
    ('C', 100),
    ('XC', 90),
    ('L', 50),
    ('XL', 40),
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I', 1)
)


def toRoman(n):
    """convert integer to Roman numeral"""
    if not (0 < n < 4000):
        raise OutOfRangeError, "integer should in 1~39999"

    if int(n) is not n:
        raise NotIntegerError, "non-integer can not \
        be converted to Roman integer."
    result = ""
    for numeral, integer in romanNumeralMap:
        while n >= integer:
            result += numeral
            n -= integer
    return result


def fromRoman(s):
    """convert Roman numeral to integer"""
    romanpattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
    if not re.search(romanpattern, s):
        raise InvalidRomanNumeralError, "%s is not a valid roman numeral" % s
    result = 0
    index = 0
    for numeral, integer in romanNumeralMap:
        while s[index:index + len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result


if __name__ == '__main__':
    print fromRoman('I')
