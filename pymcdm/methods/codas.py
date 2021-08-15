# Copyright (c) 2021 Bartłomiej Kizielewicz

import numpy as np
from .. import normalizations
from .mcda_method import MCDA_method


def _psi(x, tau=0.02):
    if np.abs(x) >= tau:
        return 1
    return 0


class CODAS(MCDA_method):
    def __init__(self, normalization_function=normalizations.linear_normalization):
        """Create CODAS method object, using normaliztion `normalization_function`.

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
        CODAS._validate_input_data(matrix, weights, types)
        if self.normalization is not None:
            nmatrix = normalizations.normalize_matrix(matrix, self.normalization, types)
        else:
            nmatrix = normalizations.normalize_matrix(matrix, normalizations.linear_normalization, types)
        return CODAS._codas(nmatrix, weights)

    @staticmethod
    def _codas(nmatrix, weights):
        # Every row of nmatrix is multiplayed by weights
        weighted_matrix = nmatrix * weights
        n, m = weighted_matrix.shape

        # Vector of NIS
        nis = np.min(weighted_matrix, axis=0)

        # Euclidean and Taxicab distances from negative-ideal solution
        E = np.sqrt(np.sum((weighted_matrix - nis) ** 2, axis=1))
        T = np.sum(np.abs(weighted_matrix - nis), axis=1)

        # Construct the relative assessment matrix
        h = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                h[i, j] = (E[i] - E[j]) + (_psi(E[i] - E[j]) * (T[i] - T[j]))

        return np.sum(h, axis=1)