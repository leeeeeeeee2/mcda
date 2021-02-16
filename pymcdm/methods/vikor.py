# Copyright (c) 2020 Andrii Shekhovtsov

import numpy as np
from .. import normalizations
from .mcda_method import MCDA_method

def _fake_normalization(x, cost=False):
    if cost:
        return np.max(x) - x
    else:
        return x


class VIKOR(MCDA_method):
    def __init__(self, normalization_function=None):
        """Create VIKOR method object, using normaliztion `normalization_function`.

Parameters
----------
    normalization_function : None or callable
        Function which should be used to normalize `matrix` columns. It should match signature `foo(x, cost)`, where `x` is a vector which should be normalized and `cost` is a bool variable which says if `x` is a cost or profit criterion.
"""
        if normalization_function is None:
            self.normalization = _fake_normalization
        else:
            self.normalization = normalization_function

    def __call__(self, matrix, weights, types, *args, v=0.5, return_all=False, **kwargs):
        """Rank alternatives from decision matrix `matrix`, with criteria weights `weights` and criteria types `types`.

Parameters
----------
    matrix : ndarray
        Decision matrix / alternatives data.
        Alternatives are in rows and Criteria are in columns.

    weights : ndarray
        Criteria weights. Sum of the weights should be 1. (e.g. sum(weights) == 1)

    types : ndarray
        Array with definitions of criteria types:
        1 if criteria is profit and -1 if criteria is cost for each criteria in `matrix`.

    v : float
        Weight of the strategy (see VIKOR algorithm explanation).

    return_all : bool
        If True, all three ranking (S, R, Q) would be returned.

    *args and **kwargs are necessary for methods which reqiure some additional data.

Returns
-------
    if `return_all` is False
    ndarray
        Q preference values for alternatives. Better alternatives have smaller values.

    if `reeturn_all` is True
    ndarray, ndarray, ndarray
        S, R, Q preference values (see VIKOR algorithm explanation).
"""
        VIKOR._validate_input_data(matrix, weights, types)
        nmatrix = normalizations.normalize_matrix(matrix, self.normalization, types)
        S, R, Q = VIKOR._vikor(nmatrix, weights, v)
        if return_all:
            return S, R, Q
        else:
            return Q

    @staticmethod
    def _vikor(matrix, weights, v=0.5):
        """
VIKOR MCDM method

Arguments:
    matrix: Decision matrix.
            Alternative are in rows and Criteria are in columns.
    weights: Weights to criteria
Returns:
    S, R, Q: Ranking lists
"""
        fstar = np.max(matrix, axis=0)
        fminus = np.min(matrix, axis=0)

        if np.any(fstar == fminus):
            eq = np.arange(fstar.shape[0])[fstar == fminus]
            raise ValueError(
                f'Criteria with indexes {eq} contains equal values for all alternatives. VIKOR method could not be applied in this case. Consider removing this criteria from the decision matrix or use another MCDA method.'
            )

        weighted_ff = weights * ((fstar - matrix)/(fstar - fminus))
        S = np.sum(weighted_ff, axis=1)
        R = np.max(weighted_ff, axis=1)

        Sstar = np.min(S)
        Sminus = np.max(S)
        Rstar = np.min(R)
        Rminus = np.max(R)

        Q = v * (S - Sstar)/(Sminus - Sstar)\
          + (1 - v) * (R - Rstar)/(Rminus - Rstar)

        return S, R, Q
