import numpy as np
from .mcda_method import MCDA_method

class COPRAS(MCDA_method):
    def __init__(self):
        """Create COPRAS method object."""
        pass

    def __call__(self, matrix, weights, types, *args, **kwargs):
        """
Rank alternatives from decision matrix `matrix`, with criteria weights `weights` and criteria types `types`.

Args:
    `matrix`: ndarray represented decision matrix.
            Alternatives are in rows and Criteria are in columns.
    `weights`: ndarray, represented criteria weights.
    `types`: ndarray which contains 1 if criteria is profit and -1 if criteria is cost for each criteria in `matrix`.
    `*args` and `**kwargs` are necessary for methods which reqiure some additional data.

Returns:
    Ranking for alternatives. Better alternatives have higher values.
"""
        COPRAS._validate_input_data(matrix, weights, types)
        return COPRAS._copras(matrix, weights, types)

    @staticmethod
    def _copras(matrix, weights, cryteria_types):
        """COPRAS MCDM method
        Arguments:
            matrix: Decision matrix. Normalization is built-in.
                    Alternatives are in rows and Criteria are in columns.
            weights: Weights to criteria
            criteria_types: Numpy array of 1 and -1
                            1 for profit and
                            -1 for cost
        Returns:
            ranks: ranking list
        """
        nmatrix = matrix / np.sum(matrix, axis=0)

        # Difficult normalized decision making matrix
        wmatrix = nmatrix * weights

        Sp = np.sum(wmatrix[:, cryteria_types == 1], axis=1)
        Sm = np.sum(wmatrix[:, cryteria_types == -1], axis=1)

        Q = Sp + ((np.min(Sm) * np.sum(Sm))\
                / (Sm * np.sum(np.min(Sm) / Sm)))

        return Q / np.max(Q)
