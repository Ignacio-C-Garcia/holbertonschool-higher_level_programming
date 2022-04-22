#!/usr/bin/python3
"""comment of module"""
def find_peak(list_of_integers):
    """comment of function"""
    if list_of_integers is None:
        return None
    if len(list_of_integers) == 0:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]