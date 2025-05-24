#!/usr/bin/env python3

"""
Module for transposing NumPy arrays.
"""


def np_transpose(matrix):
    """
    Returns the transpose of a NumPy array.

    Args:
        matrix (numpy.ndarray): The matrix to transpose.

    Returns:
        numpy.ndarray: The transposed matrix.
    """
    return matrix.T
