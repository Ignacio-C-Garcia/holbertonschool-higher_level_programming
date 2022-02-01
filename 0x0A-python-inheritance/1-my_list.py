#!/usr/bin/python3
"""module"""


class MyList(list):
    """adentro"""
    def print_sorted(self):
        for item in self:
            if type(item) != int:
                raise TypeError("must be a list of integers")
        print(sorted(self))
