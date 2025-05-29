"""
Calculates the cofactor matrix of a matrix.
"""
import importlib

minr = importlib.import_module("1-minor")

def cofactor(matrix):
    minors = minr.minor(matrix)
    for i in range(len(minors)):
        for j in range(len(minors)):
            minors[i][j] *= (-1) ** (i + j)
    return minors
