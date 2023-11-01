#!/usr/bin/python3
for i in range(25, -1, -1):
    C = i + ord('A')
    if i % 2 == 1:
        C += 32
    print("{:c}".format(C), end="")
