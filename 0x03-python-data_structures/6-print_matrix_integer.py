#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    a = 0
    counter = 0
    for i in matrix:
        counter = 0
        for k in i:
            a = len(i)
            if counter < a-1:
                print("{:d} ".format(k), end="")
            else:
                print(k)
            counter += 1
