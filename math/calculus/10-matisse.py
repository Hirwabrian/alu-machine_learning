"""
Returns the derivative of a polynomial represented by a list.
"""

def poly_derivative(poly):
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    if not all(isinstance(c, (int, float)) for c in poly):
        return None
    if len(poly) == 1:
        return [0]

    return [poly[i] * i for i in range(1, len(poly))]
