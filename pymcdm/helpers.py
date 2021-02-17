# Copyright (c) 2021 Andrii Shekhovtsov

import numpy as np
from collections import Counter

__all__ = [
    'rankdata',
    'rrankdata'
]

def rankdata(a, reverse=False):
    """
    Assign ranks to data in vector `a`.

    Ranks begin at 1. Tied elements get average rank (see Examples below).

    Ranking starts from smaller values, e.g. the smaller element get
    the first position. The `reverse` argument reverse posisions, e.g.
    the largest element get first position.

    Parameters
    ----------
    a : iterable
        The array of values to be ranked.

    reverse : bool, optional
        If True, larger elements get first posisions in ranking.
        If False, smaller elements get first positions in ranking.

    Returns
    -------
    ndarray
        An array of rank scores for the input data.

    Examples
    --------
    >>> from pymcdm.helpers import rankdata
    >>> rankdata([0, 3, 2, 5])
    array([1, 3, 2, 4])
    >>> rankdata([0, 3, 2, 5], reverse=True)
    array([4, 2, 3, 1])
    >>> rankdata([0, 3, 2, 3])
    array([1. , 3.5, 2. , 3.5])
    >>> rankdata([0, 3, 2, 3], reverse=True)
    array([4. , 1.5, 3. , 1.5])
    """
    c = Counter(a)
    rv = {}
    i = 1
    for k in sorted(c.keys(), reverse=reverse):
        if c[k] == 1:
            rv[k] = i
            i += 1
        else:
            v = c[k]
            rv[k] = (2*i + v - 1)/2
            i += v
    return np.array([rv[k] for k in a], dtype='float')


def rrankdata(a):
    """Alias to `rankdata(a, reverse=True)`. See `rankdata` for details."""
    return rankdata(a, reverse=True)
