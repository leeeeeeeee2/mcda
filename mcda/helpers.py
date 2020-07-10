import numpy as np

def normalize_matrix(matrix, method, cost_column_indexes=[]):
    for i in range(matrix.shape[1]):
        if i in cost_column_indexes:
            matrix[:, i] = method(matrix[:,i], cost_criteria=True)
        else:
            matrix[:, i] = method(matrix[:, i])
    return matrix


def normalize_matrix_by_types(matrix, normalization, types):
    cost_column_indexes = np.arange(matrix.shape[1])[types == -1]
    nmatrix = normalize_matrix(matrix.copy(), normalization, cost_column_indexes)
    return nmatrix


def matrix_to_latex_table(rows, column_names, caption='', label=''):
    matrix = rows
    nrow = len(matrix)
    ncol = len(matrix[0])

    print('''\\begin{table}[h!]
    \\centering
    \\begin{tabular}{ |''' + f'{"c|"*ncol}' + '''}
        \hline''')

    print(' & '.join(column_names), '\\\\\n\hline')

    for row in matrix:
        print(' & '.join([str(i) for i in row]), '\\\\', sep='')

    print('''\hline
    \end{tabular}
    \caption{''' + caption + '''}
    \label{''' + label + '''}
\end{table}''')

