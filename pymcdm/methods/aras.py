# Copyright (c) 2021 Bartłomiej Kizielewicz

import numpy as np
from .. import normalizations
from .mcda_method import MCDA_method


class ARAS(MCDA_method):
    def __init__(self, normalization_function=normalizations.sum_normalization):
        """Create ARAS method object, using normaliztion `normalization_function`.

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
        ARAS._validate_input_data(matrix, weights, types)
        return ARAS._aras(matrix, weights, types, self.normalization)

    @staticmethod
    def _aras(matrix, weights, types, normalization):
        n, m = matrix.shape

        # Extended initial decision matrix
        exmatrix = np.zeros((n + 1, m))
        exmatrix[1:] = matrix

        for i in range(m):
            if types[i] == 1:
                exmatrix[0, i] = np.max(matrix[:, i])
            else:
                exmatrix[0, i] = np.min(matrix[:, i])

        # Every row of nmatrix is multiplayed by weights
        nmatrix = normalizations.normalize_matrix(exmatrix, normalization, types)
        weighted_matrix = nmatrix * weights

        # Values of optimality function
        S = weighted_matrix.sum(axis=1)

        # Utility degree
        K = S[1:] / S[0]

        return K
