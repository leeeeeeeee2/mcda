.. _american_school:

=============
American school
=============



ARAS
=======================

COCOSO
=======================

COPRAS
=======================

EDAS
=======================

MABAC
=======================

MAIRCA
=======================

MARCOS
=======================

MOORA
=======================

OCRA
=======================

SPOTIS
=======================

TOPSIS
=======================

:class:`TOPSIS` is designed to evaluate decision alternatives according to the following steps:

**Step 1.** Normalize the decision matrix by using min-max normalization. The values of benefit type criteria are
normalized using the (:eq:`sumProfit`) formula, while the values of cost type criteria are normalized using the
(:eq:`sumCost`) formula.

.. math::
    \begin{equation}
        r_{ij} = \frac{x_{ij} - \min(x_j)}{\max(x_j) - \min(x_j)}\
    \end{equation}
    :label: sumProfit

.. math::
    \begin{equation}
        r_{ij} = \frac{\max(x_j) - x_{ij}}{\max(x_j) - \min(x_j)}
    \end{equation}
    :label: sumCost

**Step 2.** Building a decision matrix :math:`v_{ij}` subjected to a weighting and normalization process using the
Equation (:eq:`weighted`).

.. math::
    \begin{equation}
        v_{ij} = w_{j}r_{ij} \label{weighted}
    \end{equation}
    :label: weighted

**Step 3.** Derive a positive ideal solution :math:`PIS` and a negative ideal solution :math:`NIS`. The ideal positive
solution is calculated as the maximum value for each criterion (:eq:`pis`), while the ideal negative solution is
calculated as the least value for each criterion (:eq:`nis`).

.. math::
    \begin{equation}
        v_{j}^{+} =  \{v_{1}^{+},  v_{2}^{+},  \dots,  v_{n}^{+} \} = \{\max_{j}(v_{ij}) \}
    \end{equation}
    :label: pis

.. math::
    \begin{equation}
        v_{j}^{-} = \{v_{1}^{-},  v_{2}^{-},  \dots,  v_{n}^{-} \}=  \{\min_{j}(v_{ij}) \}
    \end{equation}
    :label: nis

**Step 4.** Determine the Euclidean distance for each normalized weighted alternative from the :math:`PIS` (:eq:`sqrtPIS`)
and :math:`NIS` (:eq:`sqrtNIS`) solution.

.. math::
    \begin{equation}
        D_{i}^{+} = \sqrt{\sum_{j=1}^{n}(v_{ij}-v_{j}^{+})^{2}}
    \end{equation}
    :label: sqrtPIS

.. math::
    \begin{equation}
        D_{i}^{-} = \sqrt{\sum_{j=1}^{n}(v_{ij}-v_{j}^{-})^{2}}
    \end{equation}
    :label: sqrtNIS

VIKOR
=======================