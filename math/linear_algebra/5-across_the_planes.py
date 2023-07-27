#!/usr/bin/env python3

def add_matrices2D(mat1, mat2):
    """Adds two matrices element-wise"""
    if len(mat1) != len(mat2):
        return None
    if len(mat1[0]) != len(mat2[0]):
        return None
    array = []
    for i in range(len(mat1)):
        sub_array = []
        for j in range(len(mat1[0])):
            sub_array.append(mat1[i][j] + mat2[i][j])
        array.append(sub_array)
    return array
