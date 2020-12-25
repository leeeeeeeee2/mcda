# Copyright (c) 2020 Andrii Shekhovtsov

import numpy as np
from .. import normalizations
from .mcda_method import MCDA_method


class SPOTIS(MCDA_method):
    def __init__(self):
        """Create SPOTIS method object."""
        pass

    def __call__(self, matrix, weights, types, *args, bounds=None, **kwargs):
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

    bounds : None or ndarray
        One row should contain min and max values for one criterion.
        If None bounds of criteria (min and max) would be extracted from decision matrix.

    *args and **kwargs are necessary for methods which reqiure some additional data.

Returns
-------
    ndarray
        Preference values for alternatives. Better alternatives have smaller values.
"""
        SPOTIS._validate_input_data(matrix, weights, types)

        # If bounds is not given, determine it based on decision matrix
        if bounds is None:
            bounds = np.array((np.min(matrix, axis=0), np.max(matrix, axis=0))).T

        # Determine Ideal Solution Point based on criteria bounds
        isp = bounds[np.arange(bounds.shape[0]), ((types+1)//2).astype('int')]
        return SPOTIS._spotis(matrix, weights, isp, bounds)

    @staticmethod
    def _spotis(matrix, weights, isp, bounds):
        nmatrix = matrix.astype(float)
        # Normalized distances matrix (d_{ij})
        nmatrix = np.abs((nmatrix - isp)/
                         (bounds[:,0] - bounds[:,1]))
        # Distances to ISP (smaller means better alt)
        raw_scores = np.sum(nmatrix * weights, axis=1)
        return raw_scores
