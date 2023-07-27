#!/usr/bin/env python3

def mat_mul(mat1, mat2):
    """Multiplies two matrices"""
    if len(mat1[0]) != len(mat2):
        return None
    array = []
    for i in range(len(mat1)):
        sub_array = []
        for j in range(len(mat2[0])):
            sum = 0
            for k in range(len(mat1[0])):
                sum += mat1[i][k] * mat2[k][j]
            sub_array.append(sum)
        array.append(sub_array)
    return array
