#!/usr/bin/env python3

"""
Module for performing matrix multiplication using NumPy.
"""


import numpy as np


def np_matmul(mat1, mat2):
    """
    Performs matrix multiplication using NumPy.

    Args:
        mat1 (numpy.ndarray): First matrix.
        mat2 (numpy.ndarray): Second matrix.

    Returns:
        numpy.ndarray: The matrix product of mat1 and mat2.
    """
    return np.matmul(mat1, mat2)
