#!/usr/bin/env python3

"""
Returns the integral of a polynomial with optional constant of integration.
"""


def poly_integral(poly, C=0):
    if not isinstance(poly, list) or not isinstance(C, (int, float)):
        return None
    if not all(isinstance(c, (int, float)) for c in poly):
        return None

    result = [C]
    for i in range(len(poly)):
        val = poly[i] / (i + 1)
        result.append(int(val) if val.is_integer() else val)
    return result
