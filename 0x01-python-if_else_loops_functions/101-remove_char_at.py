#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    for i, C in enumerate(str):
        if i != n:
            new += C
    return new
