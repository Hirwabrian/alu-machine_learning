#!/usr/bin/env python3

"""
Module for element-wise addition of two 2D matrices.
"""


def add_matrices2D(mat1, mat2):
    """
    Adds two 2D matrices element-wise.

    Args:
        mat1 (list of lists): First matrix.
        mat2 (list of lists): Second matrix.

    Returns:
        list of lists or None: The resulting matrix or None if shapes differ.
    """
    if len(mat1) != len(mat2):
        return None

    for i in range(len(mat1)):
        if len(mat1[i]) != len(mat2[i]):
            return None

    result = []
    for i in range(len(mat1)):
        row_sum = []
        for j in range(len(mat1[i])):
            row_sum.append(mat1[i][j] + mat2[i][j])
        result.append(row_sum)

    return result
