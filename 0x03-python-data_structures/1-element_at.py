#!/usr/bin/python3
def element_at(my_list, idx):
    list_len = len(my_list)
    idx = int(idx)
    if idx < 0 or idx > list_len:
        return None
    else:
        for i in range(list_len):
            if idx == i:
                return my_list[idx]
