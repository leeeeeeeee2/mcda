import numpy as np
from .normalizations import sum_normalization, normalize_matrix

__all__ = [
    'equal',
    'entropy',
    'standard_deviation',
]

def equal(matrix):
    N = matrix.shape[1]
    return np.ones(N) / N

def entropy(matrix):
    m, n = matrix.shape
    nmatrix = normalize_matrix(matrix, sum_normalization, None)
    entropies = np.empty(n)
    # Iterate over all criteria
    for i, col in enumerate(nmatrix.T):
        if np.any(col == 0):
            entropies[i] = 0
        else:
            entropies[i] = -np.sum(col * np.log(col))
    entropies = entropies / np.log(m)

    E = 1 - entropies
    return E / np.sum(E)


def standard_deviation(matrix):
    m, n = matrix.shape
    std = np.std(matrix, axis=0)
    return std / np.sum(std)
