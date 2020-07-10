import numpy as np

def copras(matrix, weights, cryteria_types):
    '''COPRAS MCDM method
    Arguments:
        matrix: Decision matrix. Normalization is built-in.
                Alternative are in rows and Criteria are in columns.
        weights: Weights to criteria
        criteria_types: Numpy array of 1 and -1
                        1 for profit and
                        -1 for cost
    Returns:
        ranks: ranking list
    '''

    # Normalization
    nmatrix = matrix.copy()
    crit_sums = np.sum(matrix, axis=0)

    for i in range(nmatrix.shape[0]):
        nmatrix[i] = matrix[i] / crit_sums

    # Difficult normalized decision making matrix
    wmatrix = nmatrix * np.tile(weights, (nmatrix.shape[0], 1))

    Sp = np.sum(wmatrix[:, cryteria_types == 1], axis=1)
    Sm = np.sum(wmatrix[:, cryteria_types == -1], axis=1)

    Q = Sp + ((np.min(Sm) * np.sum(Sm))\
            / (Sm * np.sum(np.min(Sm) / Sm)))

    return Q / np.max(Q)
