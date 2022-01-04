#!/usr/bin/python3
def uniq_add(my_list=[]):
    suma = 0
    for number in set(my_list):
        suma = suma + number
    return suma
