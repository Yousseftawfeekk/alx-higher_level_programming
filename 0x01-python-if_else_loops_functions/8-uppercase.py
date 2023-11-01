#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        C = ord(str[i])
        if C >= 97 and C <= 122:
            C = C - 32
        print("{}".format(chr(C)), end="")
    print()
