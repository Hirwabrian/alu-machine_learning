#!/usr/bin/env python3

"""
Calculates the inverse of a matrix.
"""


import importlib
det_mod = importlib.import_module("0-determinant")
adj_mod = importlib.import_module("3-adjugate")

def inverse(matrix):
    """
    Calculates the inverse of a matrix using adjugate and determinant.

    Args:
        matrix (list of lists): The input matrix.

    Returns:
        list of lists: Inverse of the matrix or None if singular.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not a non-empty square matrix.
    """
    if not isinstance(matrix, list) or matrix == [] or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if len(matrix) == 0 or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    det = det_mod.determinant(matrix)
    if det == 0:
        return None

    adj = adj_mod.adjugate(matrix)
    return [[elem / det for elem in row] for row in adj]
