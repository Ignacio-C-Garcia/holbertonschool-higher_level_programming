#!/usr/bin/python3
"""modulo"""


def matrix_divided(matrix, div):
    """divide all numbers of a matrix"""
    if type(matrix) != list:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    for element in matrix:
        if type(element) != list:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    for lista in matrix:
        for element in lista:
            if type(element) != int and type(element) != float:
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if len(set(map(len, matrix))) != 1:
        raise TypeError('Each row of the matrix must have the same size')

    """div conditions:"""
    if type(div) != int or type(div) != float:
        TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    return list(map(lambda x: list(map(lambda y: round(y/div, 2),x)), matrix))

