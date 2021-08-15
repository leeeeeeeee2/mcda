# Copyright (c) 2021 Bartłomiej Kizielewicz

import numpy as np
from .. import normalizations
from .mcda_method import MCDA_method


def _marcos_normalization(x, cost=False):
    if cost:
        return x[-2] / x
    return x / x[-2]


class MARCOS(MCDA_method):
    def __init__(self, normalization_function=_marcos_normalization):
        """Create MARCOS method object, using normaliztion `normalization_function`.

        Parameters
        ----------
            normalization_function : callable
                Function which should be used to normalize `matrix` columns. It should match signature `foo(x, cost)`,
                where `x` is a vector which should be normalized and `cost` is a bool variable which says if `x` is a
                cost or profit criterion.
        """
        self.normalization = normalization_function

    def __call__(self, matrix, weights, types, *args, **kwargs):
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

            *args and **kwargs are necessary for methods which reqiure some additional data.

        Returns
        -------
            ndarray
                Preference values for alternatives. Better alternatives have higher values.
        """
        MARCOS._validate_input_data(matrix, weights, types)
        return MARCOS._marcos(matrix, weights, types, self.normalization)

    @staticmethod
    def _marcos(matrix, weights, types, normalization):
        n, m = matrix.shape

        # Extended initial decision matrix
        exmatrix = np.zeros((n + 2, m))
        exmatrix[:-2] = matrix

        max_maxes = matrix.max(axis=0)
        min_values = matrix.min(axis=0)

        for i in range(m):
            if types[i] == 1:
                exmatrix[-2, i] = max_maxes[i]
                exmatrix[-1, i] = min_values[i]
            else:
                exmatrix[-2, i] = min_values[i]
                exmatrix[-1, i] = max_maxes[i]

        # Normalization
        n_exmatrix = normalizations.normalize_matrix(exmatrix, normalization, types)

        # Weighting
        weighted_matrix = n_exmatrix * weights

        # Utility degree
        S = weighted_matrix.sum(axis=1)
        k_neg = (S / S[-1])[:-2]
        k_pos = (S / S[-2])[:-2]

        # Utility functions
        f_k_pos = k_neg / (k_pos + k_neg)
        f_k_neg = k_pos / (k_pos + k_neg)
        f_k = (k_pos + k_neg) / (1 + (1 - f_k_pos) / f_k_pos + (1 - f_k_neg) / f_k_neg)

        return f_k
