#!/usr/bin/python3
"""module name"""


def read_file(filename=""):
    """name"""
    with open(filename, mode='r', encoding='utf-8') as text:
        for line in text:
            print(line,end='')
