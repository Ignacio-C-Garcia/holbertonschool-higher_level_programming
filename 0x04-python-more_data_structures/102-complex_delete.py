#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    b_dictionary = a_dictionary.copy()

    for key, number in b_dictionary.items():
        if number == value:
            a_dictionary.pop(key)
    return (a_dictionary)
