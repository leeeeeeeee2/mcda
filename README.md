# PyMCDM

Python 3 library for solving multi-criteria decision-making (MCDM) problems.

___
# Installation

You can download and install `pymcdm` library using pip:

```Bash
pip install pymcdm
```
___
# Available methods

The library contains:
* MCDA methods:
  * TOPSIS
  * VIKOR
  * COPRAS
  * PROMETHEE I and II
  * COMET
  * SPOTIS
  * ARAS
  * COCOSO
  * CODAS
  * EDAS
  * MABAC
  * MAIRCA
  * MARCOS
  * OCRA
  * MOORA


* Weighting methods:
  * Equal weights
  * Entropy method
  * Std method
  * MEREC method
  * CRITIC method
  * CILOS method
  * IDOCRIW method
  * Angle method
  * Gini method
 
 
* Normalization methods:
  * Linear
  * Max
  * Sum
  * Vector
  * Logarithmic
  * Linear
  * Nonlinear
  * Enhanced accuracy


* Correlation coefficients:
    * Spearman
    * Pearson
    * Weighted Spearman
    * Rank Similarity Coefficient
    * Kendall Tau
    * Goodman and Kruskal Gamma


* Helpers
    * rankdata
    * rrankdata

___
# Usage example

Here's a small example of how use this library to solve MCDM problem.
For more examples with explanation see [examples](https://gitlab.com/shekhand/mcda/-/blob/master/examples/examples.ipynb).

```python
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
```

And the output of this example (numbers are rounded):

```bash
3 0.6126
4 0.0
2 0.7829
1 1.0
```

