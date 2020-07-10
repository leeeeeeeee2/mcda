import numpy as np

from .helpers import normalize_matrix
from .copras import copras
from .topsis import topsis
from .vikor import vikor
from .promethee import promethee


def copras_wrapper(*args):
    return 1 - copras(*args)


def create_topsis_wrapper(normalization):
    def topsis_wrapper(matrix, weights, types):
        cost_column_indexes = np.arange(matrix.shape[1])[types == -1]
        nmatrix = normalize_matrix(matrix.copy(), normalization, cost_column_indexes)
        return 1 - topsis(nmatrix, weights)
    return topsis_wrapper


def create_vikor_wrapper(normalization=None):
    def vikor_wrapper(matrix, weights, types):
        cost_column_indexes = np.arange(matrix.shape[1])[types == -1]
        if normalization is not None:
            matrix = normalize_matrix(matrix.copy(), normalization, cost_column_indexes)
        S, R, Q = vikor(matrix, weights)
        return np.array(Q)
    return vikor_wrapper


def create_promethee_wrapper(preference_function, q_mod):
    def promethee_wrapper(matrix, weights, types):
        Fp, Fm, FI = promethee(matrix, weights, types,
                               preference_function, q_mod)
        return 1 - FI
    return promethee_wrapper
