# Copyright (c) 2021 Bartłomiej Kizielewicz

import numpy as np
from .. import normalizations
from .mcda_method import MCDA_method


class MABAC(MCDA_method):
    def __init__(self, normalization_function=normalizations.minmax_normalization):
        """Create MABAC method object, using normaliztion `normalization_function`.

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
        MABAC._validate_input_data(matrix, weights, types)
        if self.normalization is not None:
            nmatrix = normalizations.normalize_matrix(matrix, self.normalization, types)
        else:
            nmatrix = normalizations.normalize_matrix(matrix, normalizations.minmax_normalization, types)
        return MABAC._mabac(nmatrix, weights)

    @staticmethod
    def _mabac(nmatrix, weights):
        n, m = nmatrix.shape
        # Calculation of the elements from the weighted matrix
        weighted_matrix = (nmatrix + 1) * weights

        # Determining the border approximation area matrix
        G = np.product(weighted_matrix, axis=0) ** (1 / n)

        # Calculation of the distance border approximation area
        Q = weighted_matrix - G

        return np.sum(Q, axis=1)
