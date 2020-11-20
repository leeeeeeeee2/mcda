import numpy as np
from itertools import permutations

__all__ = [
    'spearman',
    'pearson',
    'weighted_spearman',
    'rank_similarity_coef',
    'kendall_tau',
    'goodman_kruskal_gamma'
]

def _cov(x, y):
    return np.cov(x, y, bias=True)[0][1]

def spearman(x, y):
    '''r_s
    x, y - rank values
    '''
    return (_cov(x, y)) / (np.std(x) * np.std(y))


def pearson(x, y):
    '''r
    x, y - raw values
    '''
    return (_cov(x, y)) / (np.std(x) * np.std(y))


def weighted_spearman(x, y):
    '''r_w
    x, y - rank values
    '''
    N = len(x)
    n = 6 * np.sum((x-y)**2 * ((N - x + 1) + (N - y + 1)))
    d = N**4 + N**3 - N**2 - N
    return 1 - (n/d)


def rank_similarity_coef(x, y):
    '''WS
    x, y - rank values
    '''
    N = len(x)
    n = np.fabs(x - y)
    d = np.max((np.fabs(1 - x), np.fabs(N - x)), axis=0)
    return 1 - np.sum(2.0**(-1.0 * x) * n/d)


def kendall_tau(x, y):
    '''Kendall Tau
    x, y - rank values
    '''
    n = len(x)
    res = 0
    for j in range(n):
        for i in range(j):
            res += np.sign(x[i] - x[j]) * np.sign(y[i] - y[j])
    return 2/(n*(n-1)) * res


def goodman_kruskal_gamma(x, y):
    '''Goodman and Kruskal gamma
    x, y -  rank values
    '''
    num = 0
    den = 0
    for i, j in permutations(range(len(x)), 2):
        x_dir = x[i] - x[j]
        y_dir = y[i] - y[j]
        sign = np.sign(x_dir * y_dir)
        num += sign
        if sign:
            den += 1
    return num / float(den)
