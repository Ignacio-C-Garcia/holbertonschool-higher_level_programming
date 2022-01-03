#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for number in list:
            print("{:d}".format(number), end='')
            if number != list[-1]:
                print(' ', end='')
        print("")
