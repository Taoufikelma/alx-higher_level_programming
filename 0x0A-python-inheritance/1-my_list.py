#!/usr/bin/python3
""" Mylist module"""


class MyList(list):
    """ Mylist class """

    def print_sorted(self):
        """ Print sorted list """
        print(sorted(self))
