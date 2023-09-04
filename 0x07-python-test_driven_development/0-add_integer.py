#!/usr/bin/python3
"""
Module add-integer
Adds two integer together

"""


def add_integer(a, b=98):
    """Returns the addition of a and b,
    or an error if a and b are not integers or floats
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    return int(a + b)
