#!/usr/bin/env python3

def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenates two matrices along a specific axis"""
    if axis == 0:
        array = []
        for i in range(len(mat1)):
            sub_array = []
            for j in range(len(mat1[0])):
                sub_array.append(mat1[i][j])
            array.append(sub_array)
        for i in range(len(mat2)):
            sub_array = []
            for j in range(len(mat2[0])):
                sub_array.append(mat2[i][j])
            array.append(sub_array)
        return array
    elif axis == 1:
        array = []
        for i in range(len(mat1)):
            sub_array = []
            for j in range(len(mat1[0])):
                sub_array.append(mat1[i][j])
            for j in range(len(mat2[0])):
                sub_array.append(mat2[i][j])
            array.append(sub_array)
        return array
    else:
        return None
