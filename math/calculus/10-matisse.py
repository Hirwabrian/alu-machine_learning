#!/usr/bin/env python3

"""
Returns the derivative of a polynomial represented by a list.
"""


def poly_derivative(poly):
    """
    calculates the derivative of the given polynomial
    """
    if type(poly) is not list or len(poly) < 1:
        return None
    for coefficient in poly:
        if type(coefficient) is not int and type(coefficient) is not float:
            return None
    for power, coefficient in enumerate(poly):
        if power is 0:
            derivative = [0]
            continue
        if power is 1:
            derivative = []
        derivative.append(power * coefficient)
    while derivative[-1] is 0 and len(derivative) > 1:
        derivative = derivative[:-1]
    return derivative
