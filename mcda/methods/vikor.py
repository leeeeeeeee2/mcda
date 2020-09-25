import numpy as np
from .. import normalization
from .mcda_method import MCDA_metod


class VIKOR(MCDA_metod):
    def __init__(self, normalization_function=None):
        """
Create VIKOR method object, using normaliztion `normalization_function`.

Args:
    `normalization_function`: function or None. If None method won't do any normalization of the input matrix. If function, it would be used for normalize `matrix` columns. It should match signature `foo(x, cost)`, where `x` is a vector which would be normalized and `cost` is a bool variable which says if `x` is a cost or profit criteria.
"""
        self.normalization = normalization_function

    def __call__(self, matrix, weights, types, return_type='raw'):
        VIKOR._validate_input_data(matrix, weights, types)
        if self.normalization is not None:
            nmatrix = normalization.normalize_matrix(matrix, self.normalization, types)
        else:
            nmatrix = matrix.copy()
        S, R, Q = VIKOR._vikor(nmatrix, weights)

        return VIKOR._determine_result(np.array(Q), return_type)

    def _vikor(matrix, weights):
        """
VIKOR MCDM method

Arguments:
    matrix: Decision matrix.
            Alternative are in rows and Criteria are in columns.
    weights: Weights to criteria
Returns:
    S, R, Q: Ranking lists
"""
        w = weights
        fstar = np.max(matrix, axis=0)
        fminus = np.min(matrix, axis=0)
        ff = fstar - fminus

        # Ensure we won't divide on zero
        ff[ff == 0] = 10 ** -10

        S = []
        R = []
        for fi in matrix:
            tmp = w * ((fstar - fi)/ff)
            S.append(sum(tmp))
            R.append(max(tmp))

        Sstar = np.min(S)
        Sminus = np.max(S)
        Rstar = np.min(R)
        Rminus = np.max(R)
        ss = Sminus - Sstar
        rr = Rminus - Rstar
        v = 0.5

        # Ensure we won't divide on zero
        if rr == 0:
            rr = 10 ** -10

        Q = []
        for sj, rj in zip(S, R):
            qj = v * (sj - Sstar)/ss + (1-v)*(rj - Rstar)/rr
            Q.append(qj)

        return S, R, Q
