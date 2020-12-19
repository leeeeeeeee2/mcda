import numpy as np
from .. import normalizations
from .mcda_method import MCDA_method

class VIKOR(MCDA_method):
    def __init__(self, normalization_function=None):
        """
Create VIKOR method object, using normaliztion `normalization_function`.

Args:
    `normalization_function`: function or None. If None method won't do any normalization of the input matrix. If function, it would be used for normalize `matrix` columns. It should match signature `foo(x, cost)`, where `x` is a vector which would be normalized and `cost` is a bool variable which says if `x` is a cost or profit criteria.
"""
        self.normalization = normalization_function

    def __call__(self, matrix, weights, types, *args, v=0.5, return_all=False, **kwargs):
        """
Rank alternatives from decision matrix `matrix`, with criteria weights `weights` and criteria types `types`.

Args:
    `matrix`: ndarray represented decision matrix.
            Alternatives are in rows and Criteria are in columns.
    `weights`: ndarray, represented criteria weights.
    `types`: ndarray which contains 1 if criteria is profit and -1 if criteria is cost for each criteria in `matrix`.
    `v`: weight of the strategy (see VIKOR algorithm explanation)
    `return_all`: if True, returns all three rankings (S, R, Q) instead of Q
    `*args` and `**kwargs` are necessary for methods which reqiure some additional data.

Returns:
    Q ranking. Better alternatives have lower values.
"""
        VIKOR._validate_input_data(matrix, weights, types)
        if self.normalization is not None:
            nmatrix = normalization.normalize_matrix(matrix, self.normalization, types)
        else:
            nmatrix = matrix.astype('float')
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
