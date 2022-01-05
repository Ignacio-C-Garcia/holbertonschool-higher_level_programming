#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    b_dictionary = a_dictionary.copy()

    if not a_dictionary:
        return (None)

    for key, number in b_dictionary.items():
        if number == value:
            b_dictionary.pop(key)
    return (b_dictionary)
