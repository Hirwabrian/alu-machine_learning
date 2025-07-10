#!/usr/bin/env python3
"""
Performs a same convolution on grayscale images using two loops only.
"""
import numpy as np


def convolve_grayscale_same(images, kernel):
    """
    Performs a same convolution on grayscale images.

    Parameters:
    - images: numpy.ndarray of shape (m, h, w)
        Multiple grayscale images.
    - kernel: numpy.ndarray of shape (kh, kw)
        Kernel for the convolution.

    Returns:
    - numpy.ndarray containing the convolved images.
    """
    m, h, w = images.shape
    kh, kw = kernel.shape

    pad_h = (kh - 1) // 2
    pad_w = (kw - 1) // 2

    images_padded = np.pad(
        images,
        ((0, 0), (pad_h, pad_h), (pad_w, pad_w)),
        mode='constant'
    )

    convolved = np.zeros((m, h, w))

    for i in range(h):
        for j in range(w):
            image_slice = images_padded[:, i:i+kh, j:j+kw]
            convolved[:, i, j] = np.sum(image_slice * kernel, axis=(1, 2))

    return convolved
