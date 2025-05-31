#!/usr/bin/env python3

"""
Calculates the inverse of a matrix.
"""


def determinant(matrix):
    """Calculates the determinant of a matrix."""

    if not isinstance(matrix, list) or not all(isinstance(row, list)
            for row in matrix):
        raise TypeError('matrix must be a list of lists')
    if matrix == [[]]:
        return 1
    if len(matrix) == 0 or any(len(row) != len(matrix) for row in
                               matrix):
        raise ValueError('matrix must be a square matrix')
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    return sum(matrix[0][i] * determinant([r[:i] + r[i + 1:] for r in
               matrix[1:]]) * (-1) ** i for i in range(len(matrix)))


def cofactor(matrix):
    """Calculates the cofactor matrix of a square matrix."""

    if not isinstance(matrix, list) or matrix == [] \
        or not all(isinstance(row, list) for row in matrix):
        raise TypeError('matrix must be a list of lists')
    if any(len(row) != len(matrix) for row in matrix):
        raise ValueError('matrix must be a non-empty square matrix')
    if len(matrix) == 1:
        return [[1]]
    cof = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix)):
            sub = [r[:j] + r[j + 1:] for (k, r) in enumerate(matrix)
                   if k != i]
            row.append(determinant(sub) * (-1) ** (i + j))
        cof.append(row)
    return cof


def adjugate(matrix):
    """Calculates the adjugate of a square matrix."""

    return [list(row) for row in zip(*cofactor(matrix))]


def inverse(matrix):
    """
    Calculates the inverse of a square matrix.

    Args:
        matrix (list of lists): The matrix to invert.

    Returns:
        list of lists or None: Inverted matrix, or None if singular.
    """

    if not isinstance(matrix, list) or matrix == [] \
        or not all(isinstance(row, list) for row in matrix):
        raise TypeError('matrix must be a list of lists')
    if any(len(row) != len(matrix) for row in matrix):
        raise ValueError('matrix must be a non-empty square matrix')

    det = determinant(matrix)
    if det == 0:
        return None
    adj = adjugate(matrix)
    return [[elem / det for elem in row] for row in adj]
