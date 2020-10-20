import numpy as np
from .. import normalization
from .mcda_method import MCDA_method


class TOPSIS(MCDA_method):
    def __init__(self, normalization_function=normalization.minmax_normalization):
        """
Create TOPSIS method object, using normaliztion `normalization_function`.

Args:
    `normalization_function`: function which should be used to normalize `matrix` columns. It should match signature `foo(x, cost)`, where `x` is a vector which would be normalized and `cost` is a bool variable which says if `x` is a cost or profit criterion.
"""
        self.normalization = normalization_function

    def __call__(self, matrix, weights, types, return_type='raw', **kwargs):
        """
Rank alternatives from decision matrix `matrix`, with criteria weights `weights` and criteria types `types`.

Args:
    `matrix`: ndarray represented decision matrix.
            Alternatives are in rows and Criteria are in columns.
    `weights`: ndarray, represented criteria weights.
    `types`: ndarray which contains 1 if criteria is profit and -1 if criteria is cost for each criteria in `matrix`.
    `*args` and `**kwargs` are necessary for methods which reqiure some additional data.

Returns:
    Ranking of alternatives. Better alternatives have higher values.
"""
        TOPSIS._validate_input_data(matrix, weights, types)
        if self.normalization is not None:
            nmatrix = normalization.normalize_matrix(matrix, self.normalization, types)
        else:
            nmatrix = matrix.astype('float')
        return TOPSIS._topsis(nmatrix, weights)

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

