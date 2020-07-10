import numpy as np

def topsis(matrix, weights):
    '''TOPSIS MCDM method
    Arguments:
        matrix: Normalized decision matrix.
                Alternative are in rows and Criteria are in columns.
        weights: Weights to criteria
    Returns:
        ranks: ranking list
    '''
    weighted_matrix = matrix * np.tile(weights, (matrix.shape[0], 1))

    pis = np.max(weighted_matrix, axis=0)
    nis = np.min(weighted_matrix, axis=0)

    Dp = []
    Dm = []
    for vi in weighted_matrix:
        dp = np.sqrt(sum((vi - pis)**2))
        Dp.append(dp)

        dm = np.sqrt(sum((vi - nis)**2))
        Dm.append(dm)

    ranks = []
    for dm, dp in zip(Dm, Dp):
        ranks.append(dm/(dm+dp))

    return np.array(ranks, dtype=float)

