import numpy as np
from .. import normalization
from .mcda_method import MCDA_method

class COPRAS(MCDA_method):
    def __init__(self, normalization_function=None):
        """
Create COPRAS method object, using normaliztion `normalization_function`.

Args:
    `normalization_function`: function or None. If None method won't do any normalization of the input matrix. If function, it would be used for normalize `matrix` columns. It should match signature `foo(x, cost)`, where `x` is a vector which would be normalized and `cost` is a bool variable which says if `x` is a cost or profit criteria.
"""
        self.normalization = normalization_function

    def __call__(self, matrix, weights, types, return_type='raw', **kwargs):
        COPRAS._validate_input_data(matrix, weights, types)
        if self.normalization is not None:
            nmatrix = normalization.normalize_matrix(matrix, self.normalization, types)
        else:
            nmatrix = matrix.copy()
        raw_ranks = 1 - COPRAS._copras(nmatrix, weights, types)

        return COPRAS._determine_result(raw_ranks, return_type)

    def _copras(matrix, weights, cryteria_types):
        '''COPRAS MCDM method
        Arguments:
            matrix: Decision matrix. Normalization is built-in.
                    Alternative are in rows and Criteria are in columns.
            weights: Weights to criteria
            criteria_types: Numpy array of 1 and -1
                            1 for profit and
                            -1 for cost
        Returns:
            ranks: ranking list
        '''

        # Normalization
        nmatrix = matrix.copy()
        crit_sums = np.sum(matrix, axis=0)

        for i in range(nmatrix.shape[0]):
            nmatrix[i] = matrix[i] / crit_sums

        # Difficult normalized decision making matrix
        wmatrix = nmatrix * np.tile(weights, (nmatrix.shape[0], 1))

        Sp = np.sum(wmatrix[:, cryteria_types == 1], axis=1)
        Sm = np.sum(wmatrix[:, cryteria_types == -1], axis=1)

        Q = Sp + ((np.min(Sm) * np.sum(Sm))\
                / (Sm * np.sum(np.min(Sm) / Sm)))

        return Q / np.max(Q)
