#!/usr/bin/python3
def print_list_integer(my_list=[]):
    len_list = int(len(my_list))
    for i in range(len_list):
        print("{:d}".format(my_list[i]))
