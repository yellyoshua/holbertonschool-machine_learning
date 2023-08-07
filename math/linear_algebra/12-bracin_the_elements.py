#!/usr/bin/env python3

def np_elementwise(mat1, mat2):
    """ elementwise addition, subtraction, multiplication, division
    Args:
        mat1: Given matrix
        mat2: Given matrix
    Return:
        tuple containing sum, difference, product, quotient
    """
    sum = mat1 + mat2
    difference = mat1 - mat2
    product = mat1 * mat2
    quotient = mat1 / mat2
    return sum, difference, product, quotient
