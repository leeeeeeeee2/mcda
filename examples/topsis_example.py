import numpy as np
from pymcdm.methods import TOPSIS
from pymcdm.helpers import rrankdata

# Define decision matrix (2 criteria, 4 alternative)
alts = np.array([
    [4, 4],
    [1, 5],
    [3, 2],
    [4, 2]
    ], dtype='float')

# Define weights and types
weights = np.array([0.5, 0.5])
types = np.array([1, -1])

# Create object of the method
topsis = TOPSIS()

# Determine preferences and ranking for alternatives
pref = topsis(alts, weights, types)
ranking = rrankdata(pref)

for r, p in zip(ranking, pref):
    print(r, p)
