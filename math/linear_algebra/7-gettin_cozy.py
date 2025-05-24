#!/usr/bin/env python3

"""
Module for concatenating two 2D matrices along a given axis.
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two 2D matrices along a specified axis.

    Args:
        mat1 (list of lists): First matrix.
        mat2 (list of lists): Second matrix.
        axis (int): 0 for vertical (row-wise), 1 for horizontal (column-wise).

    Returns:
        list of lists or None: Concatenated matrix or None if shapes are incompatible.
    """
    # Concatenate vertically (add more rows)
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        result = []
        for row in mat1:
            result.append(row[:])
        for row in mat2:
            result.append(row[:])
        return result

    # Concatenate horizontally (add more columns to each row)
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        result = []
        for i in range(len(mat1)):
            result.append(mat1[i] + mat2[i])
        return result

    return None
