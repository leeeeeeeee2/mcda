.. _american_school:

=============
American school
=============



ARAS
=======================

COCOSO
=======================

:class:`COCOSO` is designed to evaluate decision alternatives according to the following steps:

**Step 1.** Definition of a decision matrix of dimension :math:`n \times m`, where :math:`n` is the number of
alternatives, and :math:`m` is the number of criteria (:eq:`equ:mat`).

.. math::
    \begin{equation}
    x_{i j}=\left[\begin{array}{llll}
    x_{11} & x_{12} & \ldots & x_{1 m} \\
    x_{21} & x_{22} & \ldots & x_{2 m} \\
    \ldots & \ldots & \ldots & \ldots \\
    x_{n 1} & x_{n 2} & \ldots & x_{n m}
    \end{array}\right]
    \end{equation}
    :label: equ:mat



**Step 2.** Normalization the decision matrix, where for profit criteria use the equation (:eq:`equ:profit`), and for
cost, criteria use the equation (:eq:`equ:cost`). In this study, The Minimum-Maximum normalization method was used.

.. math::
    \begin{equation}
        r_{ij} = \frac{x_{ij} - \min_{i}{x_{ij}}}{\max_{i}{x_{ij}} - \min_{i}{x_{ij}}}
    \end{equation}
    :label: equ:profit

.. math::
    \begin{equation}
        r_{ij} = \frac{\max_{i}{x_{ij}} - x_{ij}}{\max_{i}{x_{ij}} - \min_{i}{x_{ij}}}
    \end{equation}
    :label: equ:cost


**Step 3.** Calculation of the weighted sum of the comparison sequence and the total power weight of the comparison
sequences for each alternative. The values of :math:`S_i` are based on the grey relationship generation method
(:eq:`equ:SI`), and for :math:`P_i` the values are achieved according to the multiplicative WASPAS setting
(:eq:`equ:PI`).


.. math::
    \begin{equation}
        S_i = \sum_{j=1}^{n} (w_j r_{ij})
    \end{equation}
    :label: equ:SI

.. math::
    \begin{equation}
        P_i = \sum_{j=1}^{n} (r_{ij})^{w_j}
    \end{equation}
    :label: equ:PI


**Step 4.** Computation of the relative weights of alternatives using aggregation strategies. The formulas determine the
strategies (:eq:`equ:s1`)-(:eq:`equ:s3`), where the first strategy expresses the average of the sums of WSM and WPM s
cores (:eq:`equ:s1`), the second strategy expresses the sum of WSM and WPM scores over the best (:eq:`equ:s2`), and the
third strategy expresses the compromise strategy of WSM and WPM by using the :math:`\lambda` value (:eq:`equ:s3`).
In this study, a :math:`\lambda` value of 0.5 was used.

.. math::
    \begin{equation}
    k_{i a}=\frac{P_{i}+S_{i}}{\sum_{i=1}^{m}\left(P_{i}+S_{i}\right)}
    \end{equation}
    :label: equ:s1

.. math::
    \begin{equation}
    k_{i b}=\frac{S_{i}}{\min _{i} S_{i}}+\frac{P_{i}}{\min _{i} P_{i}}
    \end{equation}
    :label: equ:s2

.. math::
    \begin{equation}
    k_{i c}=\frac{\lambda\left(S_{i}\right)+(1-\lambda)\left(P_{i}\right)}{\left(\lambda \max _{i} S_{i}+(1-\lambda) \max _{i} P_{i}\right)} ; \quad 0 \leqslant \lambda \leqslant 1
    \end{equation}
    :label: equ:s3

**Step 5.** Establish the final ranking of alternatives based on :math:`k_i` values defined using the formula
(:eq:`equ:ki`). The higher the :math:`k_i` value, the higher the ranking.

.. math::
    \begin{equation}
    k_{i}=\left(k_{i a} k_{i b} k_{i c}\right)^{\frac{1}{3}}+\frac{1}{3}\left(k_{i a}+k_{i b}+k_{i c}\right)
    \end{equation}
    :label: equ:ki

COPRAS
=======================

EDAS
=======================

:class:`EDAS` is designed to evaluate decision alternatives according to the following steps:

**Step 1.** Define a decision matrix of dimension :math:`n \times m`, where :math:`n` is the number of alternatives,
and :math:`m` is the number of criteria (:eq:`equ:mat2`).

.. math::
    \begin{equation}
    X_{i j}=\left[\begin{array}{llll}
    x_{11} & x_{12} & \ldots & x_{1 m} \\
    x_{21} & x_{22} & \ldots & x_{2 m} \\
    \ldots & \ldots & \ldots & \ldots \\
    x_{n 1} & x_{n 2} & \ldots & x_{n m}
    \end{array}\right]
    \end{equation}
    :label: equ:mat2

**Step 2.** Calculate the average solution for each criterion according to the formula (:eq:`equ:av`).

.. math::
    \begin{equation}
    A V_{j}=\frac{\sum_{i=1}^{n} X_{i j}}{n}
    \end{equation}
    :label: equ:av

**Step 3.** Calculating the positive distance from the mean solution and the negative distance from the mean solution
for the alternatives. When the criterion is of profit type, the negative distance and the positive distance are
calculated using equations (:eq:`equ:ndapr`) and (:eq:`equ:pdapr`), while when the criterion is of cost type, the
distances are calculated using formulas (:eq:`equ:ndacs`) and (:eq:`equ:pdacs`).

.. math::
    \begin{equation}
    PDA_{i j} = \frac{\max \left(0,\left(X_{i j}-A V_{j}\right)\right)}{A V_{j}}
    \end{equation}
    :label: equ:pdapr

.. math::
    \begin{equation}
    NDA_{i j}=\frac{\max \left(0,\left(A V_{j}-X_{i j}\right)\right)}{A V_{j}}
    \end{equation}
    :label: equ:ndapr

.. math::
    \begin{equation}
    P D A_{i j}=\frac{\max \left(0,\left(A V_{j}-X_{i j}\right)\right)}{A V_{j}}
    \end{equation}
    :label: equ:pdacs

.. math::
    \begin{equation}
    N D A_{i j}=\frac{\max \left(0,\left(X_{i j}-A V_{j}\right)\right)}{A V_{j}}
    \end{equation}
    :label: equ:ndacs

**Step 4.** Calculate the weighted sums of :math:`PDA` and :math:`NDA` for each decision variant using equations
(:eq:`equ:wsp`) and (:eq:`equ:wsn`).

.. math::
    \begin{equation}
    \mathrm{A} SP_{i}=\sum_{j=1}^{m} w_{j} P D A_{i j}
    \end{equation}
    :label: equ:wsp

.. math::
    \begin{equation}
    SN_{i}=\sum_{j=1}^{m} w_{j} N D A_{i j}
    \end{equation}
    :label: equ:wsn


**Step 5.** Normalize the weighted sums of negative and positive distances using equations (:eq:`equ:normsp`) and
(:eq:`equ:normsn`).

.. math::
    \begin{equation}
    N S P_{i}=\frac{S P_{i}}{\max _{i}\left(S P_{i}\right)}
    \end{equation}
    :label: equ:normsp

.. math::
    \begin{equation}
    N S N_{i}=1-\frac{S N_{i}}{\max _{i}\left(S N_{i}\right)}
    \end{equation}
    :label: equ:normsn


**Step 6.** Calculate the evaluation score (:math:`AS`) for each alternative using the formula (:eq:`equ:as`). A higher
point value determines a higher ranking alternative.

.. math::
    \begin{equation}
    A S_{i}=\frac{1}{2}\left(N S P_{i}+N S N_{i}\right)
    \end{equation}
    :label: equ:as

MABAC
=======================
:class:`MABAC` is designed to evaluate decision alternatives according to the following steps:


**Step 1.** Define a decision matrix of dimension :math:`n \times m`, where :math:`n` is the number of alternatives,
and :math:`m` is the number of criteria (:eq:`equ:mat4`).

.. math::
    \begin{equation}
    x_{i j}=\left[\begin{array}{llll}
    x_{11} & x_{12} & \ldots & x_{1 m} \\
    x_{21} & x_{22} & \ldots & x_{2 m} \\
    \ldots & \ldots & \ldots & \ldots \\
    x_{n 1} & x_{n 2} & \ldots & x_{n m}
    \end{array}\right]
    \end{equation}
    :label: equ:mat4


**Step 2.** Normalization of the decision matrix, where for criteria of type profit use equation (:eq:`equ:profitma`)
and for criteria of type cost use equation (:eq:`equ:costma`).

.. math::
    \begin{equation}
    n_{i j}=\frac{x_{i j}- \min x_{i}}{\max x_{i}- \min x_{i}}
    \end{equation}
    :label: equ:profitma

.. math::
    \begin{equation}
    n_{i j}=\frac{x_{i j}- \max x_{i}}{\min x_{i} - \max x_{i}}
    \end{equation}
    :label: equ:costma

**Step 3.** Create a weighted matrix based on the values from the normalized matrix according to the formula
(:eq:`equ:wema`).

.. math::
    \begin{equation}
    v_{i j}=w_{i} \cdot\left(n_{i j}+1\right)
    \end{equation}
    :label: equ:wema


**Step 4.** Boundary approximation area (:math:`G`) matrix determination. The Boundary Approximation Area (:math:`BAA`)
for all criteria can be determined using the formula (:eq:`equ:boundma`).

.. math::
    \begin{equation}
    g_{i}=\left(\prod_{j=1}^{m} v_{i j}\right)^{1 / m}
    \end{equation}
    :label: equ:boundma


**Step 5.** Distance calculation of alternatives from the boundary approximation area for matrix elements (:math:`Q`) by
equation (:math:`equ:qma`).

.. math::
    \begin{equation}
    Q=\left[\begin{array}{cccc}
    v_{11}-g_{1} & v_{12}-g_{2} & \ldots & v_{1 n}-g_{n} \\
    v_{21}-g_{1} & v_{22}-g_{2} & \ldots & v_{2 n}-g_{n} \\
    \ldots & \ldots & \ldots & \ldots \\
    v_{m 1}-g_{1} & v_{m 2}-g_{2} & \ldots & v_{m n}-g_{n}
    \end{array}\right]=\left[\begin{array}{cccc}
    q_{11} & q_{12} & \ldots & q_{1 n} \\
    q_{21} & q_{22} & & q_{2 n} \\
    \ldots & \ldots & \ldots & \ldots \\
    q_{m 1} & q_{m 2} & \ldots & q_{m n}
    \end{array}\right]
    \end{equation}
    :label: equ:qma

The membership of a given alternative :math:`A_i` to the approximation area (:math:`G`, :math:`G^{+}` or :math:`G^{-}`)
is established by (:eq:`equ:aproxma`).

.. math::
    \begin{equation}
    A_{i} \in\left\{\begin{array}{lll}
    G^{+} & \text {if } & q_{i j}>0 \\
    G & \text { if } & q_{i j}=0 \\
    G^{-} & \text {if } & q_{i j}<0
    \end{array}\right.
    \end{equation}
    :label: equ:aproxma

**Step 6.** Ranking the alternatives according to the sum of the distances of the alternatives from the areas of
approximation of the borders (:eq:`equ:sima`).

.. math::
    \begin{equation}
    S_{i}=\sum_{j=1}^{n} q_{i j}, \quad j=1,2, \ldots, n, \quad i=1,2, \ldots, m
    \end{equation}
    :label: equ:sima

MAIRCA
=======================

:class:`MAIRCA` is designed to evaluate decision alternatives according to the following steps:

**Step 1.** Define a decision matrix of dimension :math:`n \times m`, where :math:`n` is the number of alternatives,
and :math:`m` is the number of criteria (:eq:`equ:mat3`).

.. math::
    \begin{equation}
    x_{i j}=\left[\begin{array}{llll}
    x_{11} & x_{12} & \ldots & x_{1 m} \\
    x_{21} & x_{22} & \ldots & x_{2 m} \\
    \ldots & \ldots & \ldots & \ldots \\
    x_{n 1} & x_{n 2} & \ldots & x_{n m}
    \end{array}\right]
    \end{equation}
    :label: equ:mat3


**Step 2.** Determining the preference for choosing alternatives using the vector :math:`P_{Ai}` using the formula
(:eq:`equ:pia`).

.. math::
    \begin{equation}
    P_{A i}=\frac{1}{n} ; \sum_{i=1}^{n} P_{A i}=1, i=1,2, \ldots, n
    \end{equation}
    :label: equ:pia

If the decision-maker is neutral in choosing an alternative, the vector :math:`P_{Ai}` should have the same values
(:eq:`equ:pia2`).

.. math::
    \begin{equation}
    P_{A 1}=P_{A 2}=\ldots=P_{A n}
    \end{equation}
    :label: equ:pia2


**Step 3.** Creating a theoretical ranking matrix :math:`T_p`. The elements of this matrix are the multiplied priorities
of alternatives by the criteria weights. The form of this matrix can be represented by the formula (:eq:`equ:tp`).

.. math::
    \begin{equation}
    T_{p}=\left[\begin{array}{cccc}
    t_{p 11} & t_{p 12} & \ldots & t_{p 1 m} \\
    t_{p 21} & t_{p 22} & \ldots & t_{p 2 m} \\
    \ldots & \cdots & \ldots & \ldots \\
    t_{p n 1} & t_{p n 2} & \ldots & t_{p n m}
    \end{array}\right] = \left[\begin{array}{cccc}
    P_{A 1} \cdot w_{1} & P_{A 1} \cdot w_{2} & \ldots & P_{A 1} \cdot w_{m} \\
    P_{A 2} \cdot w_{1} & P_{A 2} \cdot w_{2} & \ldots & P_{A m} \cdot w_{m} \\
    \ldots & \ldots & \ldots & \ldots \\
    P_{A n} \cdot w_{1} & P_{A n} \cdot w_{2} & \ldots & P_{A n} \cdot w_{m}
    \end{array}\right]
    \end{equation}
    :label: equ:tp

When the preferences determined for the alternatives by the decision-maker are equal, the theoretical ranking matrix is
represented by a theoretical ranking vector using the formula (:eq:`equ:tpwe`).

.. math::
    \begin{equation}
    T_p =
    \left[\begin{array}{cccc}
    t_{p 11} & t_{p 12} & \ldots & t_{p 1 n}
    \end{array}\right]=
    \left[\begin{array}{llll}
    p_{A 1} . w_{1} & p_{A 1} \cdot w_{2} & \ldots & p_{A 1} \cdot w_{n}
    \end{array}\right]
    \end{equation}
    :label: equ:tpwe


**Step 4.** Create the real rating matrix, which is shown by the formula (:eq:`equ:tr`).

.. math::
    \begin{equation}
    T_r =
    \left[\begin{array}{cccc}
    t_{r 11} & t_{r 12} & \ldots & t_{r 1 m} \\
    t_{r 21} & t_{r 22} & \ldots & t_{r 2 m} \\
    \ldots & \ldots & \ldots & \ldots \\
    t_{r n 1} & t_{r n 2} & \ldots & t_{r n m}
    \end{array}\right]
    \end{equation}
    :label: equ:tr


The values of the real rating matrix are determined depending on the criterion of profit type or cost type, sequentially
according to the formulas (:eq:`equ:trpr`) and (:eq:`equ:trcs`).

.. math::
    \begin{equation}
    \label{equ:trpr}
    t_{r i j}=t_{p i j} \cdot\left(\frac{x_{i j}-\min x_{j}}{\max x_{j}-\min x_{j}}\right)
    \end{equation}
    :label: equ:trpr

.. math::
    \begin{equation}
    \label{equ:trcs}
    t_{r i j}=t_{p i j} \cdot\left(\frac{x_{i j}-\max x_{j}}{\min x_{j}-\max x_{j}}\right)
    \end{equation}
    :label: equ:trcs

**Step 5.** Calculating the total gap matrix ($G$) by taking the difference between the theoretical grade matrix
(:math:`Tp`) and the actual grade matrix (:math:`Tr`) using the formula (:eq:`equ:gap`).

.. math::
    \begin{equation}
    G=T_{p}-T_{r}= \left[\begin{array}{cccc}
    t_{p 11}-t_{r 11} & t_{p 12}-t_{r 12} & \ldots & t_{p 1 m}-t_{r 1 m} \\
    t_{p 21}-t_{r 21} & t_{p 21}-t_{r 21} & \ldots & t_{p 2 m}-t_{r 2 m} \\
    \ldots & \ldots & \ldots & \ldots \\
    t_{p n 1}-t_{r n 1} & t_{p n 2}-t_{r n 2} & \ldots & t_{p n m}-t_{r n m}
    \end{array}\right]
    \end{equation}
    :label: equ:gap

**Step 6.** Calculating the final values of the criterion functions (:math:`Q_i`) for the alternatives using the sum of
the rows of the gap matrix (:math:`G`) using the formula (:eq:`equ:qima`). The alternative with the lowest value of
:math:`Q_i` has the highest ranking.

.. math::
    \begin{equation}
    \label{equ:qima}
    Q_{i}=\sum_{j=1}^{m} g_{i j} \quad i=1,2, \ldots, n
    \end{equation}
    :label: equ:qima

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