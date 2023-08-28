#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        sum = fct(*args)
        return sum
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
