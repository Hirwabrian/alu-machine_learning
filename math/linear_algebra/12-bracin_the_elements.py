#!/usr/bin/env python3

"""
Module for performing element-wise operations on NumPy arrays.
"""


def np_elementwise(mat1, mat2):
    """
    Performs element-wise addition, subtraction, multiplication, and division.

    Args:
        mat1 (numpy.ndarray or scalar): First operand.
        mat2 (numpy.ndarray or scalar): Second operand.

    Returns:
        tuple: (sum, difference, product, quotient), each a NumPy array.
    """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
