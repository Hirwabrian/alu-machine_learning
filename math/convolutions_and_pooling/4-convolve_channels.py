#!/usr/bin/env python3
"""
Performs a convolution on images with multiple channels.
"""
import numpy as np
from math import floor, ceil


def convolve_channels(images, kernel, padding='same', stride=(1, 1)):
    """
    Performs a convolution on RGB images (with channels).

    Parameters:
    - images: numpy.ndarray of shape (m, h, w, c)
    - kernel: numpy.ndarray of shape (kh, kw, c)
    - padding: 'same', 'valid', or tuple of (ph, pw)
    - stride: tuple of (sh, sw)

    Returns:
    - numpy.ndarray of shape (m, new_h, new_w) with convolved output
    """
    m, h, w, c = images.shape
    kh, kw, kc = kernel.shape
    sh, sw = stride

    if padding == 'same':
        ph = int(ceil(((h - 1) * sh + kh - h) / 2.))
        pw = int(ceil(((w - 1) * sw + kw - w) / 2.))
    elif padding == 'valid':
        ph, pw = 0, 0
    else:
        ph, pw = padding

    padded = np.pad(images, ((0, 0), (ph, ph), (pw, pw), (0, 0)),
                    mode='constant')

    out_h = int(((h + 2 * ph - kh) / sh) + 1)
    out_w = int(((w + 2 * pw - kw) / sw) + 1)

    output = np.zeros((m, out_h, out_w))

    for i in range(out_h):
        for j in range(out_w):
            h_start = i * sh
            w_start = j * sw
            img_slice = padded[:, h_start:h_start+kh, w_start:w_start+kw, :]
            output[:, i, j] = np.sum(img_slice * kernel, axis=(1, 2, 3))

    return output
