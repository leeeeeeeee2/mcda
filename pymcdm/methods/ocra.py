# Copyright (c) 2021 Bartłomiej Kizielewicz

import numpy as np
from .mcda_method import MCDA_method


def _ocra_normalization(x, cost=False):
    if cost:
        return (np.max(x) - x) / np.min(x)
    return (x - np.min(x)) / np.min(x)


class OCRA(MCDA_method):
    def __init__(self, normalization_function=_ocra_normalization):
        """Create OCRA method object, using normaliztion `normalization_function`.

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
        OCRA._validate_input_data(matrix, weights, types)
        return OCRA._ocra(matrix, weights, types, self.normalization)

    @staticmethod
    def _ocra(martrix, weights, types, normalization):
        n, m = martrix.shape

        # Calculate preference ratings for cost and profit criteria
        I = np.zeros(n)
        O = np.zeros(n)
        for j in range(m):
            if types[j] == -1:
                I += weights[j] * normalization(martrix[:, j], cost=True)
            else:
                O += weights[j] * normalization(martrix[:, j], cost=False)

        # Calculate linear preference ratings for cost and profit criteria
        I -= np.min(I)
        O -= np.min(O)

        # Calculate overall preference rating
        return (I + O) - np.min(I + O)
