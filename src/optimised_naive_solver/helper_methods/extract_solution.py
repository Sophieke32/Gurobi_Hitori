import numpy as np

# Method to extract the solution of an optimisation
#
# Returns white, an array of all variables in is_black with value = 0
# Returns black, an array of all variables in is_black with value = 1
# Returns grid, an n x n grid where 0 means the corresponding value is white
#               and 1 means the corresponding value is black
def extract_solution(n, m, is_black):
    white = []
    black = []
    grid = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            if type(is_black[i][j]) == int or not m.getAttr('X', [is_black[i][j]])[0]:
                white.append(is_black[i][j])
                grid[i, j] = 0
            # if m.getAttr('X', [is_black[i][j]])[0]:
            else:
                black.append(is_black[i][j])
                grid[i, j] = 1

            # else:
            #     white.append(is_black[i][j])
            #     grid[i, j] = 0

    return white, black, grid