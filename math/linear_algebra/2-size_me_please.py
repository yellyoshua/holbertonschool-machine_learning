#!/usr/bin/env python3

def matrix_shape(matrix):
    """OK"""
    shape = []
    while type(matrix) == list:
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
