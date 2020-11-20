import numpy as np

from .. import normalization
from .mcda_method import MCDA_method


class PROMEHTEE_II(MCDA_method):
    def __init__(self, preference_function, q_mod):
        """
Create PROMEHTEE_II method object, using `preference_function` and `q_mod`.

Args:
    `preference_function`: name of the preference function ('usual', 'ushape', 'vshape', 'level', 'vshape_2')
    `q_mod`: multiplyer in the equation of the q
"""
        self.preference_function = preference_function
        self.q_mod = q_mod

    def __call__(self, matrix, weights, types, *args, promethee_I=False, **kwargs):
        """
Rank alternatives from decision matrix `matrix`, with criteria weights `weights` and criteria types `types`.

Args:
    `matrix`: ndarray represented decision matrix.
            Alternatives are in rows and Criteria are in columns.
    `weights`: ndarray, represented criteria weights.
    `types`: ndarray which contains 1 if criteria is profit and -1 if criteria is cost for each criteria in `matrix`.
    `promethee_I`: bool, if True then returns F+ and F- (like in promethee I).
    `*args` and `**kwargs` are necessary for methods which reqiure some additional data.

Returns:
    Ranking of alternatives. Better alternatives have higher values.
"""
        PROMEHTEE_II._validate_input_data(matrix, weights, types)
        Fp, Fm, FI = PROMEHTEE_II._promethee(matrix, weights, types,
                                             self.preference_function, self.q_mod)
        if promethee_I:
            return Fp, Fm
        else:
            return FI

    def _promethee(matrix, weights,
                  criteria_types=None,
                  preference_function='usual',
                  q_mod=1):
        """Arguments:
        matrix - np.array, decision matrix
        weight - np.array, weights for criteria
        criteria_types - list or None,
            -1 if criteria is cost, 1 if criteria is profit,
            if None all criterias are profit
        preference_function - which preference function use:
            Possible values:
            'usual', 'ushape', 'vshape', 'level', 'vshape_2'
        q_mod - multiplier of std when q is calculated
        """
        pf = getattr(PROMEHTEE_II._PreferenceFunctions, preference_function)
        # N - number of alternatives
        # M - number of criteria
        N, M = matrix.shape

        diff_tables = []
        for crit in matrix.T: # Iterate over criteria
            d = np.zeros((N, N))

            for i in range(N):
                for j in range(N):
                    d[i][j] = crit[i] - crit[j]

            diff_tables.append(d)

        if criteria_types is not None:
            for i in range(M):
                diff_tables[i] = diff_tables[i] * criteria_types[i]

        H_tables = []
        for d in diff_tables:
            q = np.mean(d[d > 0]) - (q_mod * np.std(d[d > 0]))
            p = np.mean(d[d > 0]) + (q_mod * np.std(d[d > 0]))
            h = np.zeros((N, N))
            for i in range(N):
                for j in range(N):
                    h[i][j] = pf(d[i][j], q, p)
            H_tables.append(h)

        pi_table = np.zeros((N, N))
        for i in range(N):
            for j in range(N):
                values = np.array([weights[k] * H_tables[k][i][j]
                                   for k in range(M)])
                pi_table[i][j] = sum(values)

        F_plus = np.sum(pi_table, axis=1) / (N-1)
        F_minus = np.sum(pi_table, axis=0) / (N-1)

        FI = F_plus - F_minus

        return F_plus, F_minus, FI


    class _PreferenceFunctions:
        def usual(d, q, p):
            return int(d > 0)

        def ushape(d, q, p):
            return int(d > q)

        def vshape(d, q, p):
            if 0 < d <= p:
                return d/p
            else:
                return int(d > p)

        def level(d, q, p):
            if q < d <= p:
                return 1/2
            else:
                return int(d > p)

        def vshape_2(d, q, p):
            if q < d <= p:
                return (d-q)/(p-q)
            else:
                return int(d > p)
