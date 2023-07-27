#!/usr/bin/env python3

def matrix_transpose(matrix):
    """Returns the transpose of a 2D matrix"""
    array = []
    for i in range(len(matrix[0])):
        sub_array = []
        for row in matrix:
            sub_array.append(row[i])
        array.append(sub_array)
    return array
