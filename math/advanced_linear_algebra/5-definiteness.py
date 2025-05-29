#!/usr/bin/env python3

"""
Determines the definiteness of a numpy matrix.
"""

import numpy as np

def definiteness(matrix):
    """
    Determines the definiteness of a matrix using its eigenvalues.

    Args:
        matrix (numpy.ndarray): A square NumPy array.

    Returns:
        str: One of the following strings:
            - "Positive definite"
            - "Positive semi-definite"
            - "Negative definite"
            - "Negative semi-definite"
            - "Indefinite"
            - None (if not a valid square matrix)

    Raises:
        TypeError: If matrix is not a numpy.ndarray
    """
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1] or matrix.size == 0:
        return None

    eigenvalues = np.linalg.eigvals(matrix)
    if np.all(eigenvalues > 0):
        return "Positive definite"
    elif np.all(eigenvalues >= 0):
        return "Positive semi-definite"
    elif np.all(eigenvalues < 0):
        return "Negative definite"
    elif np.all(eigenvalues <= 0):
        return "Negative semi-definite"
    else:
        return "Indefinite"
