#!/usr/bin/python3
def element_at(my_list, idx):
    list_len = int(len(my_list))
    idx = int(idx)
    if idx > 0 or idx < list_len:
        print("Element at index {} is {}".idx, format(list_len))
    else:
        return None
