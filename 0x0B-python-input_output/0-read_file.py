#!/usr/bin/python3
"""Define text file-reading"""


def read_file(filename=""):
    """read file by utf-8"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
