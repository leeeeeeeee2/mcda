import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

from .. import normalization
from .mcda_method import MCDA_method


class PROMEHTEE_II(MCDA_method):
    def __init__(self, preference_function, q_mod):
        """
Create PROMEHTEE_II method object, using `preference_function` and `q_mod`.

Args:
    `preference_function`: name of the preference function ('usual', 'ushape', 'vshape', 'level', 'vshape_2')
    `q_mod`: multiplyer in the equation of the q
"""
        self.preference_function = preference_function
        self.q_mod = q_mod

    def __call__(self, matrix, weights, types, return_type='raw'):
        PROMEHTEE_II._validate_input_data(matrix, weights, types)
        Fp, Fm, FI = promethee(matrix, weights, types,
                               self.preference_function, self.q_mod)
        return PROMEHTEE_II._determine_result(1 - FI, return_type)

def promethee(matrix, weights,
              criteria_types=None,
              preference_function='usual',
              q_mod=1):
    """Arguments:
    matrix - np.array, decision matrix
    weight - np.array, weights for criteria
    criteria_types - list or None,
        -1 if criteria is cost, 1 if criteria is profit,
        if None all criterias are profit
    preference_function - which preference function use:
        Possible values:
        'usual', 'ushape', 'vshape', 'level', 'vshape_2'
    q_mod - multiplier of std when q is calculated
    """
    pf = getattr(PreferenceFunctions, preference_function)
    # N - number of alternatives
    # M - number of criteria
    N, M = matrix.shape

    diff_tables = []
    for crit in matrix.T: # Iterate over criteria
        d = np.zeros((N, N))

        for i in range(N):
            for j in range(N):
                d[i][j] = crit[i] - crit[j]

        diff_tables.append(d)

    if criteria_types is not None:
        for i in range(M):
            diff_tables[i] = diff_tables[i] * criteria_types[i]

    H_tables = []
    for d in diff_tables:
        q = np.mean(d[d > 0]) - (q_mod * np.std(d[d > 0]))
        p = np.mean(d[d > 0]) + (q_mod * np.std(d[d > 0]))
        h = np.zeros((N, N))
        for i in range(N):
            for j in range(N):
                h[i][j] = pf(d[i][j], q, p)
        H_tables.append(h)

    pi_table = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            values = np.array([weights[k] * H_tables[k][i][j]
                               for k in range(M)])
            pi_table[i][j] = sum(values)

    F_plus = np.sum(pi_table, axis=1)
    F_minus = np.sum(pi_table, axis=0)

    FI = F_plus - F_minus

    return F_plus/(N-1),\
           F_minus/(N-1),\
           FI/(N-1)


class PreferenceFunctions:
    def usual(d, q, p):
        return int(d > 0)

    def ushape(d, q, p):
        return int(d > q)

    def vshape(d, q, p):
        if 0 < d <= p:
            return d/p
        else:
            return int(d > p)

    def level(d, q, p):
        if q < d <= p:
            return 1/2
        else:
            return int(d > p)

    def vshape_2(d, q, p):
        if q < d <= p:
            return (d-q)/(p-q)
        else:
            return int(d > p)


def save_show_helper(filename, show):
    if filename:
        filename = filename.lower().replace(' ', '_').replace('.', '')
        plt.savefig(f'sprawozdanie/images/{filename}.pdf', bbox_inches='tight')
    if show:
        plt.show()
    else:
        plt.close()


def promethee_I_visualization(Fp, Fm, filename=None, show=True):
    fig, ax = plt.subplots()
    ax.set_xlim(-0.51, 0.51)
    ax.set_ylim(-0.51, 0.51)
    ax.axis('off')

    ax.plot([0.5, 0.5], [-0.5, 0.5], 'k', linewidth=3)
    ax.plot([-0.5, -0.5], [-0.5, 0.5], 'k', linewidth=3)
    ax.plot([0, 0], [-0.5, 0.5], 'k',
            alpha=0.5, linewidth=1, linestyle='--')

    ax.text(-0.61, 0, 'Phi+', fontsize='large')
    ax.text(-0.56, 0.5, '1.0')
    ax.text(-0.56, -0.5, '0.0')

    ax.text(0.52, 0, 'Phi-', fontsize='large')
    ax.text(0.51, -0.5, '1.0')
    ax.text(0.51, 0.5, '0.0')

    for i, (fp, fm) in enumerate(zip(Fp, Fm)):
        ax.plot([-0.5, 0.5], [-0.5 + fp, 0.5 - fm], label=f'A{i+1}')
        ax.text(-0.55, -0.5 + fp, f'A{i+1}')
        ax.text(0.51, 0.5 - fm, f'A{i+1}')
    plt.legend()

    save_show_helper(filename, show)


def promethee_II_vizualization(Fi, filename=None, show=True):
    fig, ax = plt.subplots()
    ax.set_xlim(-0.51, 0.51)
    ax.set_ylim(-0.51, 0.51)
    ax.axis('off')

    ax.plot([0, 0], [-0.5, 0.5], 'k', linewidth=5)
    ax.text(0.02, 0.5, '1.0')
    ax.text(0.02, 0, '0.0')
    ax.text(0.02, -0.5, '-1.0')

    for i in np.arange(-0.5, 0.51, 0.25):
        ax.plot([-0.02, 0.02], [i, i], 'k')

    for i, fi in enumerate(Fi):
        ax.plot([-0.1, 0.1], [fi/2, fi/2], label=f'A{i+1}')
        ax.text(-0.15, fi/2, f'{fi:0.2f}')
        ax.text(0.1, fi/2, f'A{i+1}')
    plt.legend()

    save_show_helper(filename, show)


def check_pref(fp1, fm1, fp2, fm2):
    '''Returns:
    1 if preference
    0 if indifference
    -1 if incomparability
    '''
    if fp1 == fp2 and fm1 == fm2:
        return 0 # Indifference

    elif (fp1 > fp2 and fm1 < fm2)\
            or (fp1 == fp2 and fm1 < fm2)\
            or (fp1 > fp2 and fm1 == fm2):
        return 1
    else:
        return -1


def promethee_I_graph(Fp, Fm, filename=None, show=True):
    G = nx.DiGraph()

    for i in range(len(Fp)):
        G.add_node(f'A{i+1}')

    for i in range(len(Fp)):
        for j in range(len(Fp)):
            if check_pref(Fp[i], Fm[i], Fp[j], Fm[j]) == 1:
                G.add_edge(f'A{i+1}', f'A{j+1}')

    nx.draw(G, with_labels=True, font_weight='bold',
            width=2, arrowsize=20, node_size=400)

    save_show_helper(filename, show)


