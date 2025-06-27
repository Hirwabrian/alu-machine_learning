#!/usr/bin/env python3
"""Multivariate normal distribution class."""

import numpy as np


class MultiNormal:
    """Represents a Multivariate Normal distribution."""

    def __init__(self, data):
        """
        Initialize MultiNormal instance.
        """
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        d, n = data.shape
        if n < 2:
            raise ValueError("data must contain multiple data points")

        self.mean = np.mean(data, axis=1, keepdims=True)
        X_centered = data - self.mean
        self.cov = np.dot(X_centered, X_centered.T) / (n - 1)

    def pdf(self, x):
        """
        Calculates the PDF at data point x.
        """
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")

        if x.shape != self.mean.shape:
            d = self.mean.shape[0]
            raise ValueError("x must have the shape ({}, 1)".format(d))

        d = self.mean.shape[0]
        x_m = x - self.mean

        cov_inv = np.linalg.inv(self.cov)
        cov_det = np.linalg.det(self.cov)

        norm_const = 1. / (np.sqrt((2 * np.pi) ** d * cov_det))
        exponent = -0.5 * np.dot(np.dot(x_m.T, cov_inv), x_m)

        return float(norm_const * np.exp(exponent))
