#!/usr/bin/env python3

"""
Calculates the cofactor matrix of a matrix.
"""


import importlib
minr = importlib.import_module("1-minor")

def cofactor(matrix):
    """
    Computes the cofactor matrix from a given matrix.

    Args:
        matrix (list of lists): The input matrix.

    Returns:
        list of lists: The cofactor matrix.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not a non-empty square matrix.
    """
    minors = minr.minor(matrix)
    for i in range(len(minors)):
        for j in range(len(minors)):
            minors[i][j] *= (-1) ** (i + j)
    return minors
