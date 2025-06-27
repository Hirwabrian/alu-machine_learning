#!/usr/bin/env python3
"""Calculates a correlation matrix from a covariance matrix."""

import numpy as np


def correlation(C):
    """
    Calculates the correlation matrix from a covariance matrix C.

    Parameters:
    - C: np.ndarray of shape (d, d)

    Returns:
    - np.ndarray of shape (d, d)

    Raises:
    - TypeError: if C is not a numpy.ndarray
    - ValueError: if C is not a 2D square matrix
    """
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")
    if C.ndim != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")

    std = np.sqrt(np.diag(C))
    denom = np.outer(std, std)
    corr = C / denom

    return corr
