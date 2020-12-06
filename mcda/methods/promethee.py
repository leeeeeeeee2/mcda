from functools import partial
import numpy as np

from .. import normalizations
from .mcda_method import MCDA_method


class PROMEHTEE_II(MCDA_method):
    def __init__(self, preference_function):
        """
Create PROMEHTEE_II method object, using `preference_function` and `q_mod`.

Args:
    `preference_function`: name of the preference function ('usual', 'ushape', 'vshape', 'level', 'vshape_2')
"""
        self.pf = getattr(PROMEHTEE_II._PreferenceFunctions, preference_function)

    def __call__(self, matrix, weights, types, *args, p=None, q=None, promethee_I=False, **kwargs):
        """
Rank alternatives from decision matrix `matrix`, with criteria weights `weights` and criteria types `types`.

Args:
    `matrix`: ndarray represented decision matrix.
            Alternatives are in rows and Criteria are in columns.
    `weights`: ndarray, represented criteria weights.
    `types`: ndarray which contains 1 if criteria is profit and -1 if criteria is cost for each criteria in `matrix`.
    `p`: ndarray with p values for every criterion
    `q`: ndarray with q values for every criterion
    `promethee_I`: bool, if True then returns F+ and F- (like in promethee I).
    `*args` and `**kwargs` are necessary for methods which reqiure some additional data.

Returns:
    Ranking of alternatives. Better alternatives have higher values.
"""
        pf = self.pf
        if p is None and q is None:
            pfs = (partial(pf, p=None, q=None) for i in range(matrix.shape[1]))
        elif p is None and q is not None:
            pfs = (partial(pf, p=None, q=q_) for q_ in q)
        elif p is not None and q is None:
            pfs = (partial(pf, p=p_, q=None) for p_ in p)
        else:
            pfs = (partial(pf, p=p_, q=q_) for p_, q_ in zip(p, q))

        Fp, Fm, FI = PROMEHTEE_II._promethee(matrix, weights, types, pfs)
        if promethee_I:
            return Fp, Fm
        else:
            return FI

    def _promethee(matrix, weights, criteria_types, pref_functions):
        # N - number of alternatives
        # M - number of criteria
        N, M = matrix.shape

        c_tables = (np.tile(crit.reshape(N, 1), (1, N)) for crit in matrix.T)
        diff_tables = ((c - crit if ct == 1 else crit - c)
                       for crit, c, ct in zip(matrix.T, c_tables, criteria_types))

        pi_table = sum(w * pf(d) for w, d, pf in zip(weights, diff_tables, pref_functions))

        F_plus = np.sum(pi_table, axis=1) / (N-1)
        F_minus = np.sum(pi_table, axis=0) / (N-1)

        FI = F_plus - F_minus

        return F_plus, F_minus, FI


    class _PreferenceFunctions:
        def usual(d, q, p):
            return (d > 0).astype(np.int8)

        def ushape(d, q, p):
            return (d > q).astype(np.int8)

        def vshape(d, q, p):
            d_ = d.copy()
            cond = np.logical_and(0 < d, d <= p)
            np.putmask(d_, cond, d/p)
            np.putmask(d_, np.logical_not(cond), d > p)
            return d_

        def level(d, q, p):
            d_ = d.copy()
            cond = np.logical_and(q < d, d <= p)
            np.putmask(d_, cond, 0.5)
            np.putmask(d_, np.logical_not(cond), d > p)
            return d_

        def vshape_2(d, q, p):
            d_ = d.copy()
            cond = np.logical_and(q < d, d <= p)
            np.putmask(d_, cond, (d-q)/(p-q))
            np.putmask(d_, np.logical_not(cond), d > p)
            return d_
