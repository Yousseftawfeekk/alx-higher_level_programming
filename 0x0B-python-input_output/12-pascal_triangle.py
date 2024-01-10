#!/usr/bin/python3
"""Defines Pascal's triangle function."""


def pascal_triangle(n):
    """
    Represent Pascal's Triangle of size n.

    Return list of lists of int triangle.
    """
    if n <= 0:
        return []

    P_triangle = [[1]]
    while len(P_triangle) != n:
        trio= P_triangle[-1]
        temp = [1]
        for i in range(len(trio) - 1):
            temp.append(trio[i] + trio[i + 1])
        temp.append(1)
        P_triangle.append(temp)
    return P_triangle
