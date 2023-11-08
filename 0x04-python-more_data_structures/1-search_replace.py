#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda R: replace if R == search else R, my_list))
