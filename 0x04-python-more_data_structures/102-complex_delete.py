#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    b_dictionary = a_dictionary.copy()

    for key, number in a_dictionary.items():
        if number == value:
            b_dictionary.pop(key)
    return (b_dictionary)
