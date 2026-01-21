import numpy as np
from pyscipopt import Model

# Method to extract the solution of an optimisation
#
# Returns uncovered, an array of all variables in is_covered with value = 0
# Returns covered, an array of all variables in is_covered with value = 1
# Returns grid, an n x n grid where 0 means the corresponding tile is uncovered
#               and 1 means the corresponding tile is covered
def var_scipopt_extract_solution(n, m, is_covered, that_one_var):
    uncovered = []
    covered = []
    grid = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                if not m.getVal(that_one_var):
                    uncovered.append(that_one_var)
                    grid[i, j] = 0
                elif m.getVal(that_one_var):
                    covered.append(that_one_var)
                    grid[i, j] = 1
            else:
                if not m.getVal(is_covered[i][j]):
                    # print("Adding var with value", m.getVal(is_covered[i][j]), "to uncovered")
                    uncovered.append(is_covered[i][j])
                    grid[i, j] = 0
                elif m.getVal(is_covered[i][j]):
                    # print("Adding var with value", m.getVal(is_covered[i][j]), "to covered")
                    covered.append(is_covered[i][j])
                    grid[i, j] = 1

    return uncovered, covered, grid
