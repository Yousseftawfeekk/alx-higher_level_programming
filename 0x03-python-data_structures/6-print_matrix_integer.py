#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for subMat in matrix:
        if len(subMat) == 0:
            print()
        for i in range(len(subMat)):
            print("{:d}".format(subMat[i]),
                  end="\n" if i is len(subMat) - 1 else " ")
