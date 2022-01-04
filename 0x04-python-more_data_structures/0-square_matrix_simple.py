#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    _matrix = matrix.copy()

    for i in range(len(_matrix)):
        _matrix[i] = list(map(lambda x: x*x, _matrix[i]))
    return _matrix   
