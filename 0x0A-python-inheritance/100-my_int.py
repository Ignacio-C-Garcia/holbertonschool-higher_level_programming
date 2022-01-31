#!/usr/bin/python3
"""module"""


class MyInt(int):
    """adentro"""
    def __eq__(self, object):
        """adentro"""
        return not super().__eq__(object)

    def __ne__(self, object):
        """adentro"""
        return not self == object
