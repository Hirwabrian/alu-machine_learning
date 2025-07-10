#!/usr/bin/env python3
"""
Performs a convolution on images using multiple kernels.
"""
import numpy as np


def convolve(images, kernels, padding='same', stride=(1, 1)):
    """
    Performs a convolution on images with multiple kernels.

    Parameters:
    - images: numpy.ndarray (m, h, w, c)
    - kernels: numpy.ndarray (kh, kw, c, nc)
    - padding: 'same', 'valid', or tuple (ph, pw)
    - stride: tuple (sh, sw)

    Returns:
    - numpy.ndarray (m, new_h, new_w, nc)
    """
    m, h, w, c = images.shape
    kh, kw, kc, nc = kernels.shape
    sh, sw = stride

    if padding == 'same':
        ph = int(np.ceil(((h - 1) * sh + kh - h) / 2.))
        pw = int(np.ceil(((w - 1) * sw + kw - w) / 2.))
    elif padding == 'valid':
        ph, pw = 0, 0
    else:
        ph, pw = padding

    padded = np.pad(images, ((0, 0), (ph, ph), (pw, pw), (0, 0)),
                    mode='constant')

    out_h = int(((h + 2 * ph - kh) / sh) + 1)
    out_w = int(((w + 2 * pw - kw) / sw) + 1)
    output = np.zeros((m, out_h, out_w, nc))

    for i in range(out_h):
        for j in range(out_w):
            h_start = i * sh
            w_start = j * sw
            img_slice = padded[:, h_start:h_start+kh, w_start:w_start+kw, :]

            for k in range(nc):
                output[:, i, j, k] = np.sum(
                    img_slice * kernels[:, :, :, k], axis=(1, 2, 3))

    return output
