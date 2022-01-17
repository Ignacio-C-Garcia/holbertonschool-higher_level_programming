#!/usr/bin/python3
from tkinter.messagebox import NO
from unittest import result


def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print('Inside result: {}'.format(result))
        return result
