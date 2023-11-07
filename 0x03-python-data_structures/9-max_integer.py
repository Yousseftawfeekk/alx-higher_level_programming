#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    listcpy = my_list.copy()
    listcpy.sort()
    return listcpy[-1]
