from abc import ABC
from scipy.stats import rankdata

class MCDA_metod(ABC):
    def __call__(self, matrix, weights, types, return_type='raw'):
        """
Rank alternatives from decision matrix `matrix`, with criteria weights `weights` and criteria types `types`. Return values are determined by `return_type` argument.

Args:
    `matrix`: ndarray represented decision matrix.
            Alternative are in rows and Criteria are in columns.
    `weights`: ndarray, represented criteria weights.
    `types`: iterable object (e.g. list or tuple) which contains 1 if criteria is profit and -1 if criteria is cost for each criteria in `matrix`.
    `return_type`: str, 'raw', 'ranks' or 'both' (see below)

Returns:
    if `return_type` is 'raw', then raw values would be returned.
    if `return_type` is 'ranks', then rank values would be returned. Rank values created using scipy.stats.rankdata function.
    if `return_type` is 'both', both raw and rank values would be returned (e.g. return raw, ranks)
"""
        pass

    def _determine_result(raw_ranks, return_type):
        if return_type == 'raw':
            return raw_ranks
        elif return_type == 'ranks':
            return rankdata(raw_ranks)
        elif return_type == 'both':
            return raw_ranks, rankdata(raw_ranks)
        else:
            raise ValueError(f'return_type argument should be "raw", "ranks" or "both", but it was "{return_type}"')
