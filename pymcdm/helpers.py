import numpy as np
from collections import Counter

__all__ = [
    'rankdata'
]

def rankdata(a, reverse=False):
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
    return np.array([rv[k] for k in a])
