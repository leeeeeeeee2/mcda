from functools import reduce
import math as m
import numpy as np

def minmax_normalization(x, cost_criteria=False):
    if min(x) == max(x): # If all values are equal
        return np.ones(x.shape)

    if cost_criteria:
        return (max(x) - x) / (max(x) - min(x))
    return (x - min(x)) / (max(x) - min(x))


def max_normalization(x, cost_criteria=False):
    if cost_criteria:
        return 1 - x/max(x)
    return x / max(x)


def sum_normalization(x, cost_criteria=False):
    if cost_criteria:
        return (1/x) / sum(1/x)
    return x / sum(x)


def square_root_of_sum_normalization(x, cost_criteria=False):
    if cost_criteria:
        return 1 - (x / np.sqrt(sum(x ** 2)))
    return x / np.sqrt(sum(x ** 2))


def logaritmic_normalization(x, cost_criteria=False):
    prod = reduce(lambda a, b: a*b, x)
    if cost_criteria:
        return (1 - (np.log(x) / m.log(prod))) / (len(x) - 1)
    return np.log(x) / m.log(prod)
