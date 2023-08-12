#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    tem_list = my_list[:]
    if idx < 0 or idx > len(tem_list):
        return tem_list
    else:
        for i in range(len(tem_list)):
            if idx == i:
                tem_list[idx] = element
    return tem_list
