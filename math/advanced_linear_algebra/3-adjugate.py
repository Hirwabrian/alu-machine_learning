"""
Calculates the adjugate (adjoint) matrix of a matrix.
"""
import importlib
cof = importlib.import_module("2-cofactor")

def adjugate(matrix):
    if not isinstance(matrix, list) or matrix == [] or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if len(matrix) == 0 or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    cofactor_matrix = cof.cofactor(matrix)
    return [list(row) for row in zip(*cofactor_matrix)]
