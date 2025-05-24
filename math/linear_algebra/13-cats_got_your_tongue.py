#!/usr/bin/env python3

"""
Module for concatenating NumPy arrays.
"""


import numpy as np

def np_cat(mat1, mat2, axis=0):
    """
    Concatenates two NumPy arrays along a specified axis.

    Args:
        mat1 (numpy.ndarray): First matrix.
        mat2 (numpy.ndarray): Second matrix.
        axis (int): Axis to concatenate along (0 or 1).

    Returns:
        numpy.ndarray: Concatenated matrix.
    """
    return np.concatenate((mat1, mat2), axis=axis)
