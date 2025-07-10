#!/usr/bin/env python3
"""
Performs max or average pooling on images using two loops only.
"""
import numpy as np


def pool(images, kernel_shape, stride, mode='max'):
    """
    Performs pooling on images.

    Parameters:
    - images: numpy.ndarray (m, h, w, c)
    - kernel_shape: tuple of (kh, kw)
    - stride: tuple of (sh, sw)
    - mode: 'max' or 'avg'

    Returns:
    - numpy.ndarray with pooled results
    """
    m, h, w, c = images.shape
    kh, kw = kernel_shape
    sh, sw = stride

    out_h = int(((h - kh) / sh) + 1)
    out_w = int(((w - kw) / sw) + 1)

    pooled = np.zeros((m, out_h, out_w, c))

    for i in range(out_h):
        for j in range(out_w):
            h_start = i * sh
            w_start = j * sw
            window = images[:, h_start:h_start+kh, w_start:w_start+kw, :]

            if mode == 'max':
                pooled[:, i, j, :] = np.max(window, axis=(1, 2))
            elif mode == 'avg':
                pooled[:, i, j, :] = np.mean(window, axis=(1, 2))

    return pooled
