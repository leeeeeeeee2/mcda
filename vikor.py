import numpy as np

def vikor(matrix, weights):
    '''VIKOR MCDM method
    Arguments:
        matrix: Decision matrix.
                Alternative are in rows and Criteria are in columns.
        weights: Weights to criteria
    Returns:
        S, R, Q: Ranking lists
    '''
    w = weights
    fstar = np.max(matrix, axis=0)
    fminus = np.min(matrix, axis=0)
    ff = fstar - fminus

    # Ensure we won't divide on zero
    ff[ff == 0] = 10 ** -10

    S = []
    R = []
    for fi in matrix:
        tmp = w * ((fstar - fi)/ff)
        S.append(sum(tmp))
        R.append(max(tmp))

    Sstar = np.min(S)
    Sminus = np.max(S)
    Rstar = np.min(R)
    Rminus = np.max(R)
    ss = Sminus - Sstar
    rr = Rminus - Rstar
    v = 0.5

    # Ensure we won't divide on zero
    if rr == 0:
        rr = 10 ** -10

    Q = []
    for sj, rj in zip(S, R):
        qj = v * (sj - Sstar)/ss + (1-v)*(rj - Rstar)/rr
        Q.append(qj)

    return S, R, Q
