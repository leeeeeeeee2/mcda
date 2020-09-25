import numpy as np
from .. import normalization
from .mcda_method import MCDA_metod


class TOPSIS(MCDA_metod):
    def __init__(self, normalization_function=normalization.minmax_normalization):
        """
Create TOPSIS method object, using normaliztion `normalization_function`.

Args:
    `normalization_function`: function or None. If None method won't do any normalization of the input matrix. If function, it would be used for normalize `matrix` columns. It should match signature `foo(x, cost)`, where `x` is a vector which would be normalized and `cost` is a bool variable which says if `x` is a cost or profit criteria.
"""
        self.normalization = normalization_function

    def __call__(self, matrix, weights, types, return_type='raw'):
        TOPSIS._validate_input_data(matrix, weights, types)
        if self.normalization is not None:
            nmatrix = normalization.normalize_matrix(matrix, self.normalization, types)
        else:
            nmatrix = matrix.copy()
        raw_ranks = 1 - TOPSIS._topsis(nmatrix, weights)

        return TOPSIS._determine_result(raw_ranks, return_type)

    def _topsis(matrix, weights):
        """
TOPSIS MCDM method

Args:
    matrix: ndarray represented normalized decision matrix.
            Alternative are in rows and Criteria are in columns.
    weights: Weights to criteria

Returns:
    ranks: raw rank values
"""
        weighted_matrix = matrix * np.tile(weights, (matrix.shape[0], 1))

        pis = np.max(weighted_matrix, axis=0)
        nis = np.min(weighted_matrix, axis=0)

        Dp = []
        Dm = []
        for vi in weighted_matrix:
            dp = np.sqrt(sum((vi - pis)**2))
            Dp.append(dp)

            dm = np.sqrt(sum((vi - nis)**2))
            Dm.append(dm)

        ranks = []
        for dm, dp in zip(Dm, Dp):
            ranks.append(dm/(dm+dp))

        return np.array(ranks, dtype=float)

