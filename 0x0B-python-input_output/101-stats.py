#!/usr/bin/python3
"""module doc"""


def append_after(filename="", search_string="", new_string=""):
    """append_after doc"""
    with open(filename, 'r+', encoding='utf8') as f:
        replace = ""
        for line in f:
            replace += line
            if search_string in line:
                replace += new_string
        f.seek(0)
        f.write(replace)
