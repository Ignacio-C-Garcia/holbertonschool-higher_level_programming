#!/usr/bin/python3
"""module"""


def add_attribute(obj, name, value):
    """adentro"""
    if obj.__dict__ == 0:
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)


class MyClass():
    """adentro"""
    pass

mc = MyClass()
add_attribute(mc, "name", "John")
print(mc.name)

try:
    a = "My String"
    add_attribute(a, "name", "Bob")
    print(a.name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
