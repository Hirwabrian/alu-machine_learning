"""
Calculates the minor matrix of a matrix.
"""
import importlib

det = importlib.import_module("0-determinant")

def minor(matrix):
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if len(matrix) == 0 or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    if len(matrix) == 1:
        return [[1]]

    minor_mat = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix)):
            sub = [r[:j] + r[j+1:] for idx, r in enumerate(matrix) if idx != i]
            row.append(det.determinant(sub))
        minor_mat.append(row)
    return minor_mat
