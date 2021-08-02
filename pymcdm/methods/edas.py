# Copyright (c) 2021 Bartłomiej Kizielewicz

import numpy as np
from .mcda_method import MCDA_method


class EDAS(MCDA_method):
    def __init__(self):
        """Create EDAS method object."""
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
        EDAS._validate_input_data(matrix, weights, types)
        return EDAS._edas(matrix, weights, types)

    @staticmethod
    def _edas(matrix, weights, types):
        _, m = matrix.shape
        amatrix = np.mean(matrix, axis=0)

        pda = np.zeros(matrix.shape)
        nda = np.zeros(matrix.shape)

        for j in range(m):
            if types[j] == -1:
                pda[:, j] = (amatrix[j] - matrix[:, j]) / amatrix[j]
                nda[:, j] = (matrix[:, j] - amatrix[j]) / amatrix[j]

            else:
                pda[:, j] = (matrix[:, j] - amatrix[j]) / amatrix[j]
                nda[:, j] = (amatrix[j] - matrix[:, j]) / amatrix[j]

        pda = np.where(pda >= 0, pda, 0)
        nda = np.where(nda >= 0, nda, 0)

        sp = np.sum(weights * pda, axis=1)
        sn = np.sum(weights * nda, axis=1)

        nsp = sp / np.max(sp, axis=0)
        nsn = 1 - sn / np.max(sn, axis=0)

        return (nsp + nsn) / 2
