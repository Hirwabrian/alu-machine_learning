#!/usr/bin/env python3

"""
Module to compute the shape of a nested list matrix.
"""


def matrix_shape(matrix):
    """
    Calculates the shape of a matrix represented as nested lists.

    Args:
        matrix (list): A nested list representing the matrix.

    Returns:
        list of int: The dimensions of the matrix.
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0] if matrix else []
    return shape
