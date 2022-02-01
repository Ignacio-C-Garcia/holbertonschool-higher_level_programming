#!/usr/bin/python3
"""module name"""


def read_file(filename=""):
    with open(filename, encoding='utf-8') as text:
        print(text.read())
