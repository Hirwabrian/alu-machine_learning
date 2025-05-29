#!/usr/bin/env python3

"""
Calculates the cofactor matrix of a matrix.
"""


def determinant(matrix):
    """Calculates the determinant of a matrix."""
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if matrix == [[]]:
        return 1
    if len(matrix) == 0 or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a square matrix")
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    
    det = 0
    for i in range(len(matrix)):
        sub = [r[:i] + r[i+1:] for r in matrix[1:]]
        det += matrix[0][i] * determinant(sub) * (-1)**i
    return det

def minor(matrix):
    """Computes the minor matrix of a square matrix."""
    if not isinstance(matrix, list) or matrix == [] or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    if len(matrix) == 1:
        return [[1]]
    
    minors = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix)):
            sub = [r[:j] + r[j+1:] for k, r in enumerate(matrix) if k != i]
            row.append(determinant(sub))
        minors.append(row)
    return minors

def cofactor(matrix):
    """
    Calculates the cofactor matrix of a square matrix.

    Args:
        matrix (list of lists): The input matrix.

    Returns:
        list of lists: The cofactor matrix.
    """
    minors = minor(matrix)
    for i in range(len(minors)):
        for j in range(len(minors)):
            minors[i][j] *= (-1) ** (i + j)
    return minors
