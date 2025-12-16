import numpy as np

# This method ensures the duplicates constraint
#
# For each row, and each column, it collects identical numbers by their value
# It then adds a constraint that n-1 out of n of those values need to be blackened out
def optimised_naive_unique_constraint(n, is_black, m, duplicates):
    horizontal_expressions = np.empty((n, n), dtype=object)
    for i in range(n):
        for j in range(n):
            horizontal_expressions[i][j] = []

    for i in range(n):
        for j in range(n):
            if duplicates[i][j] > 0:
                horizontal_expressions[i][int(duplicates[i][j]) -1].append(1 - is_black[i][j])

    for i in range(n):
        for j in range(n):
            if len(horizontal_expressions[i][j]) > 1:

                expr = horizontal_expressions[i][j][0]
                for v in range(len(horizontal_expressions[i][j]) -1):
                    expr += horizontal_expressions[i][j][v+1]

                m.addConstr(expr <= 1)

    vertical_expressions = np.empty((n, n), dtype=object)
    for i in range(n):
        for j in range(n):
            vertical_expressions[i][j] = []

    for i in range(n):
        for j in range(n):
            if duplicates[j][i] > 0:
                vertical_expressions[i][int(duplicates[j][i]) - 1].append(1 - is_black[j][i])

    for i in range(n):
        for j in range(n):
            if len(vertical_expressions[i][j]) > 1:

                expr = vertical_expressions[i][j][0]
                for v in range(len(vertical_expressions[i][j]) - 1):
                    expr += vertical_expressions[i][j][v + 1]

                m.addConstr(expr <= 1)

    m.update()
