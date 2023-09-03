#!/usr/bin/python3
"""
Module add_integer
Adds two integers together
"""

def add_integer(a, b=98):
    """
    add_integers - Adds two integers or floats and returns the result as an integer
    a: first int or float
    b: second int or float(default=98)
    return: sum of a and b as int (SUCCESS)
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    
    return int(a + b)
