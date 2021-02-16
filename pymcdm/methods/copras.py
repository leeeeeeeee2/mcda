# Copyright (c) 2020 Andrii Shekhovtsov

import numpy as np
from .mcda_method import MCDA_method

class COPRAS(MCDA_method):
    def __init__(self):
        """Create COPRAS method object."""
        pass

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
        COPRAS._validate_input_data(matrix, weights, types)
        if np.all(types == 1.0):
            raise ValueError('types array contains only profit criteria. COPRAS method requires at least one cost criteria.')
        return COPRAS._copras(matrix, weights, types)

    @staticmethod
    def _copras(matrix, weights, cryteria_types):
        nmatrix = matrix / np.sum(matrix, axis=0)

        # Difficult normalized decision making matrix
        wmatrix = nmatrix * weights

        Sp = np.sum(wmatrix[:, cryteria_types == 1], axis=1)
        Sm = np.sum(wmatrix[:, cryteria_types == -1], axis=1)

        Q = Sp + ((np.min(Sm) * np.sum(Sm))\
                / (Sm * np.sum(np.min(Sm) / Sm)))

        return Q / np.max(Q)
