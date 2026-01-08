import numpy as np

# Method to extract the solution of an optimisation
#
# Returns uncovered, an array of all variables in is_covered with value = 0
# Returns covered, an array of all variables in is_covered with value = 1
# Returns grid, an n x n grid where 0 means the corresponding tile is uncovered
#               and 1 means the corresponding tile is covered
def extract_solution(n, m, is_covered):
    uncovered = []
    covered = []
    grid = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            if type(is_covered[i][j]) == int or not m.getAttr('X', [is_covered[i][j]])[0]:
                uncovered.append(is_covered[i][j])
                grid[i, j] = 0
            else:
                covered.append(is_covered[i][j])
                grid[i, j] = 1

    return uncovered, covered, grid