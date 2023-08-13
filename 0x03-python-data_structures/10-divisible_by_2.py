#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    copy_list = my_list[:]
    for i in range(len(my_list)):
        if i % 2 == 0:
            copy_list[i] = True
        else:
            copy_list[i] = False
    return(copy_list)
