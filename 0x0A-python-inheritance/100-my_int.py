#!/usr/bin/python3
"""module"""


class MyInt(int):
    def __eq__(self, object):
        return not super().__eq__(object)

    def __ne__(self, object):
        return not self == object
