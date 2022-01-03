#!/usr/bin/python3
def no_c(my_string):
    copy_str = ""
    for letter in my_string:
        if letter != 'c' and letter != 'C':
            copy_str = copy_str + letter
    return copy_str
    