#!/usr/bin/python3
"""
Module print_square(size)
prints a square with character #
"""
def print_square(size):
    """
    def print_square where size is
    length and width of square.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    
    for _ in range(size):
        print("#" * size)
