#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return ("None")
    max_integer_in_list = my_list[0]
    for i in my_list:
        if i > max_integer_in_list:
            max_integer_in_list = i
    return (max_integer_in_list)
