#!/usr/bin/python3
""" Add two integer.
    Args:
        a(int): the first number
        b(int): the second number
    Raises:
        TypeError: if the args not both at same type
"""


def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
