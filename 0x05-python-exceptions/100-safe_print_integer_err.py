#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    if_int = True
    try:
        print("{:d}".format(value))
    except Exception as err:
        print("Exception:", err, file=sys.stderr)
        if_int = False
    return if_int
