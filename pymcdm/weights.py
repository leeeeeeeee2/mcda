# Copyright (c) 2020 Andrii Shekhovtsov
# Copyright (c) 2021 Bartłomiej Kizielewicz

import numpy as np
from .normalizations import minmax_normalization, sum_normalization, linear_normalization, normalize_matrix
from .correlations import correlation_matrix, pearson
from scipy.linalg import null_space

__all__ = [
    'equal',
    'entropy',
    'standard_deviation',
    'merec',
    'critic',
    'cilos',
    'idocriw',
    'angle'
]


def _fake_normalization(x, cost=False):
    if cost:
        return np.min(x) / x
    else:
        return x


def equal(matrix):
    """Calculate equal weights for given `matrix`.

Parameters
----------
    matrix : ndarray
        Decision matrix / alternatives data.
        Alternatives are in rows and Criteria are in columns.

Returns
-------
    ndarray
        Vector of weights.
"""
    N = matrix.shape[1]
    return np.ones(N) / N


def entropy(matrix):
    """Calculate weights for given `matrix` using entropy method.

Parameters
----------
    matrix : ndarray
        Decision matrix / alternatives data.
        Alternatives are in rows and Criteria are in columns.

Returns
-------
    ndarray
        Vector of weights.
"""
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
    """Calculate weights for given `matrix` using std method.

Parameters
----------
    matrix : ndarray
        Decision matrix / alternatives data.
        Alternatives are in rows and Criteria are in columns.

Returns
-------
    ndarray
        Vector of weights.
"""
    m, n = matrix.shape
    std = np.std(matrix, axis=0)
    return std / np.sum(std)


def merec(matrix, types):
    """Calculate weights for given `matrix` using MEREC method.

    Parameters
    ----------
        matrix : ndarray
            Decision matrix / alternatives data.
            Alternatives are in rows and Criteria are in columns.
        types : ndarray
            Array with definitions of criteria types:
            1 if criteria is profit and -1 if criteria is cost for each criteria in `matrix`.

    Returns
    -------
        ndarray
            Vector of weights.
    """
    n, m = matrix.shape
    nmatrix = normalize_matrix(matrix, linear_normalization, -types)
    S = np.log(1 + (1/m * np.sum(np.abs(np.log(nmatrix)), axis=1)))
    S_prim = np.zeros(nmatrix.shape)
    for j in range(m):
        ex_nmatrix = np.delete(nmatrix, j, axis=1)
        S_prim[:, j] = np.log(1 + (1/m * np.sum(np.abs(np.log(ex_nmatrix)), axis=1)))
    E = np.sum(np.abs(S_prim.T - S), axis=1)
    return E / np.sum(E)


def critic(matrix):
    """Calculate weights for given `matrix` using CRITIC method.

    Parameters
    ----------
        matrix : ndarray
            Decision matrix / alternatives data.
            Alternatives are in rows and Criteria are in columns.

    Returns
    -------
        ndarray
            Vector of weights.
    """
    nmatrix = normalize_matrix(matrix, minmax_normalization, None)
    std = np.std(nmatrix, axis=0, ddof=1)
    coef = correlation_matrix(nmatrix, pearson, True)
    C = std * np.sum(1 - coef, axis=0)
    return C / np.sum(C)


def cilos(matrix, types):
    """Calculate weights for given `matrix` using CILOS method.

    Parameters
    ----------
        matrix : ndarray
            Decision matrix / alternatives data.
            Alternatives are in rows and Criteria are in columns.
        types : ndarray
            Array with definitions of criteria types:
            1 if criteria is profit and -1 if criteria is cost for each criteria in `matrix`.

    Returns
    -------
        ndarray
            Vector of weights.
    """
    nmatrix = normalize_matrix(matrix, _fake_normalization, types)
    nmatrix = normalize_matrix(nmatrix, sum_normalization, None)
    A = nmatrix[np.argmax(nmatrix, axis=0)]
    P = (np.diag(A) - A) / np.diag(A)
    F = P - np.diag(np.sum(P, axis=0))
    q = null_space(F)
    return (q / np.sum(q)).flatten()


def idocriw(matrix, types):
    """Calculate weights for given `matrix` using IDOCRIW method.

    Parameters
    ----------
        matrix : ndarray
            Decision matrix / alternatives data.
            Alternatives are in rows and Criteria are in columns.
        types : ndarray
            Array with definitions of criteria types:
            1 if criteria is profit and -1 if criteria is cost for each criteria in `matrix`.

    Returns
    -------
        ndarray
            Vector of weights.
    """
    W = entropy(matrix)
    q = cilos(matrix, types)
    return (q * W) / np.sum(q * W, axis=0)


def angle(matrix):
    """Calculate weights for given `matrix` using angle method.

    Parameters
    ----------
        matrix : ndarray
            Decision matrix / alternatives data.
            Alternatives are in rows and Criteria are in columns.

    Returns
    -------
        ndarray
            Vector of weights.
    """
    nmatrix = normalize_matrix(matrix, sum_normalization, None)
    n, m = nmatrix.shape
    un = np.zeros(m)
    add_col = np.ones(n) * 1 / m
    for i, vec in enumerate(nmatrix.T):
        un[i] = np.arccos(np.sum(vec / m) / (np.sqrt(np.sum(vec ** 2)) * np.sqrt(np.sum(add_col ** 2))))
    return un / np.sum(un)
