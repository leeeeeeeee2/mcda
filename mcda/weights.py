import numpy as np
from .normalization import sum_normalization, normalize_matrix

def entropy(matrix):
    m, n = matrix.shape
    nmatrix = normalize_matrix(matrix, sum_normalization, None)
    entropies = -np.sum(nmatrix * np.log(nmatrix), axis=0) / np.log(m)

    E = 1 - entropies
    return E / np.sum(E)


def standard_deviation(matrix):
    m, n = matrix.shape
    std = np.std(matrix, axis=0)
    return std / np.sum(std)
