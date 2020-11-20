import numpy as np


def minmax_normalization(x, cost=False):
    if np.min(x) == np.max(x): # If all values are equal
        return np.ones(x.shape)

    if cost:
        return (np.max(x) - x) / (np.max(x) - np.min(x))
    return (x - np.min(x)) / (np.max(x) - np.min(x))


def max_normalization(x, cost=False):
    if cost:
        return 1 - x/np.max(x)
    return x / np.max(x)


def sum_normalization(x, cost=False):
    if cost:
        return (1/x) / np.sum(1/x)
    return x / np.sum(x)


def vector_normalization(x, cost=False):
    if cost:
        return 1 - (x / np.sqrt(sum(x ** 2)))
    return x / np.sqrt(np.sum(x ** 2))


def logaritmic_normalization(x, cost=False):
    prod = np.prod(x)
    if cost:
        return (1 - (np.log(x) / np.log(prod))) / (x.shape[0] - 1)
    return np.log(x) / np.log(prod)


def normalize_matrix(matrix, method, criteria_types):
    """
Normalize each column in `matrix`, using `normalization` function according `criteria_types`.

Args:
    `matrix`: numpy ndarray which represents decision matrix. The rows are considered as alternatives and the columns are considered as criteria.
    `normalization`: function which would be used for normalize `matrix` columns. It should match signature `foo(x, cost)`, where `x` is a vector which would be normalized and `cost` is a bool variable which says if `x` is a cost or profit criteria.
    `criteria_types`: None or iterable object (e.g. list or tuple) which contains 1 if criteria is profit and -1 if criteria is cost for each criteria in `matrix`. If None all criteria are considered as profit

Returns:
    Normalized copy of the input matrix.

Raises:
    ValueError: if `criteria_types` and `matrix` has different number of criteria.
"""
    if criteria_types is None:
        nmatrix = matrix.astype('float')
        for i in range(matrix.shape[1]):
            nmatrix[:,i] = method(matrix[:,i], cost=False)
        return nmatrix

    if matrix.shape[1] != len(criteria_types):
        raise ValueError(f'Matrix has {matrix.shape[1]} criteria and criteria_types has {len(criteria_types)}. This values must be equal.')

    nmatrix = matrix.astype('float')
    for i, type in enumerate(criteria_types):
        if type == 1: # If profit
            nmatrix[:,i] = method(matrix[:,i], cost=False)
        else:
            nmatrix[:,i] = method(matrix[:,i], cost=True)
    return nmatrix

