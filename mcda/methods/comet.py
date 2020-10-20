from itertools import product
import numpy as np
from .topsis import TOPSIS
from .mcda_method import MCDA_method


def _TFN(a, m, b):
    def tfn(x):
        if x < a or x > b:
            return 0.0
        if x == m:
            return 1.0
        elif x < m:
            return (x - a) / (m - a)
        else:
            return (b - x) / (b - m)
    return tfn


class COMET(MCDA_method):
    def __init__(self, cvalues, ranking_method=None, weights=None, types=None):
        """
Initialize COMET model. It creates CO and rank them using `ranking_method`.

Args:
    `cvalues`:  ndarray, each row represent characteristic values for each criteria.
    `rankings_method`: MCDA method instance which should be used for ranking.
    `weights`: ndarray or None. Weight vector for `ranking_method`,
               if None `ranking_method` would use equal weights.
    `types`: ndarray or None. Should contain 1 for profit criteria
             and -1 for cost criteria.
             If None all criteria considered as profit.
"""
        co = product(*cvalues)
        co = np.array(list(co))

        N = co.shape[1]
        if weights is None:
            weights = np.ones(N) / N

        if types is None:
            types = np.ones(N)

        sj = ranking_method(co, weights, types, return_type='raw')

        k = len(np.unique(sj))

        delta = 1 / (k - 1)

        p = np.zeros(len(sj))
        for i in range(1, k):
            ind = sj == np.max(sj)
            p[ind] = (k - i) / (k - 1)
            sj[ind] = 0

        self.cvalues = cvalues
        self.p = p
        self.tfns = [COMET._make_tfns(chv) for chv in cvalues]
        self.mej = None

    def __call__(self, matrix, weights, types, return_type='raw', **kwargs):
        raw_ranks = 1 - self.rate_alt_list(matrix)

        return COMET._determine_result(raw_ranks, return_type)

    def rate_alt(self, alt):
        """
Calculate preference for the alternative `alt`

Args:
    `alt`: np.array with criteria values for this alternative

Returns:
    Preference for the alternative `alt`
"""
        tfns = self.tfns
        # Calculate preference function for each tfn created from cvalues
        preference_levels = [[tfn(ialt) for tfn in tfns_icrit]
                             for tfns_icrit, ialt in zip(tfns, alt)]
        co = product(*preference_levels)
        co = np.array(list(co))
        # Add p vector to co matrix
        cop = np.hstack((co, self.p.reshape(-1, 1)))

        return np.sum(np.prod(cop, axis=1))

    def rate_alt_list(self, alt_set):
        return np.array([self.rate_alt(alt) for alt in alt_set])

    def get_MEJ(self):
        if self.mej is not None:
            return self.mej

        p = self.p
        lenp = len(p)
        mej = np.diag(np.ones(lenp)/2)
        for i in range(lenp):
            for j in range(i+1, lenp):
                if p[i] < p[j]:
                    mej[i, j] = 0.0
                    mej[j, i] = 1.0
                elif p[i] == p[j]:
                    mej[i, j] = 0.5
                    mej[j, i] = 0.5
                else:
                    mej[i, j] = 1.0
                    mej[j, i] = 0.0
        self.mej = mej
        return mej


    def _make_tfns(chv):
        tfns = []
        # First TFN
        tfns.append(_TFN(chv[0], chv[0], chv[1]))

        for i in range(1, len(chv)-1):
            tfns.append(_TFN(chv[i-1], chv[i], chv[i+1]))

        # Last TFN
        tfns.append(_TFN(chv[-2], chv[-1], chv[-1]))

        return tfns

