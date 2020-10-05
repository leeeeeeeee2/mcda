# https://www.researchgate.net/publication/344069742_The_SPOTIS_Rank_Reversal_Free_Method_for_Multi-Criteria_Decision-Making_Support

import numpy as np
from .. import normalization
from .mcda_method import MCDA_method

def _euclidean_dist(a, b):
    return np.sqrt((a - b) ** 2)

class SPOTIS(MCDA_method):
    def __init__(self,
                 normalization_function=normalization.minmax_normalization,
                 distance_function=_euclidean_dist):
        """
Create TOPSIS method object, using normaliztion `normalization_function`.

Args:
    `normalization_function`: function or None. If None method won't do any normalization of the input matrix. If function, it would be used for normalize `matrix` columns. It should match signature `foo(x, cost)`, where `x` is a vector which would be normalized and `cost` is a bool variable which says if `x` is a cost or profit criteria.
"""
        self.normalization = normalization_function
        self.distance = distance_function

    def __call__(self, matrix, weights, types, return_type='raw', isp=None):
        SPOTIS._validate_input_data(matrix, weights, types)
        if self.normalization is not None:
            nmatrix = normalization.normalize_matrix(matrix, self.normalization, types)
        else:
            nmatrix = matrix.copy()
        raw_ranks = 1 - SPOTIS._topsis(nmatrix, weights)

        return SPOTIS._determine_result(raw_ranks, return_type)


