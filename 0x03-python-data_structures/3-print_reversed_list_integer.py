#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for number in reversed(my_list):
        print("{:d}".format(number))
    if my_list == []:
        print("")
