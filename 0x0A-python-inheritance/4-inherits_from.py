#!/usr/bin/python3
""" Inherits from module"""


def inherits_from(obj, a_class):
    """ Check if object instance of class thet \
            inherited (directly or indirectly)
        Args:
            obj: object
            a_class: class
    """

    if type(obj) != a_class and isinstance(obj, a_class):
        return True
    return False
