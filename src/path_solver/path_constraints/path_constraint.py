import gurobipy as gp
from gurobipy import GRB

def path_path_constraint(n, is_covered, board, m):
    # Make another 2d array of variables in the size of the board
    path = list()

    for i in range(n):
        new_list = list()
        for j in range(n):
            new_list.append(m.addVar(vtype=GRB.BINARY, name=f'in_path {i}_{j}'))
        path.append(new_list)
    m.update()

    # m.addConstr(path[0][0] == 1)
    # m.addConstr(path[0][1] == 1)

    # For each square:
        # If its neighbour is white, and this square is white, and if its neighbour is on the path
            # This square is on the path
    for i in range(n-1):
        for j in range(n):
            if i == 0 and j == 0: continue
            if i == 0 and j == 1: continue
            m.addConstr(3* path[i][j] + is_covered[i][j] - (3* path[i+1][j] + is_covered[i+1][j]) <= 2)

    for i in range(1, n):
        for j in range(n):
            if i == 1 and j == 0: continue
            if i == 1 and j == 1: continue
            m.addConstr(3 * path[i][j] + is_covered[i][j] - (3 * path[i - 1][j] + is_covered[i - 1][j]) <= 2)

    for i in range(n):
        for j in range(n-1):
            if i == 0 and j == 0: continue
            if i == 0 and j == 1: continue
            m.addConstr(3 * path[i][j] + is_covered[i][j] - (3 * path[i][j + 1] + is_covered[i][j + 1]) <= 2)

    for i in range(n):
        for j in range(1, n):
            if i == 0 and j == 1: continue
            if i == 0 and j == 2: continue
            m.addConstr(3 * path[i][j] + is_covered[i][j] - (3 * path[i][j - 1] + is_covered[i][j - 1]) <= 2)

    # Either a tile is uncovered and on the path, or covered and off the path
    # m.addConstrs(
    #     path[x][y] == 1 - is_covered[x][y] for x in range(n) for y in range(n))




    # For each variable in path we now add a rule that it can only be set to 1 if a
    # neighbour is also set to 1
    # for i in range(n - 1):
    #     for j in range(n):
    #         if i == 0 and j == 0: continue  # Exempt the top left corner and a neighbour so that the model
    #         if i == 0 and j == 1: continue  # has someplace to start
    #
    #         s = m.addVar(vtype=GRB.BINARY)
    #         m.addConstr(path[i][j] + path[i + 1][j] <= 1 + s)  # s = 0: <= 1     s = 1: <= 2
    #         m.addConstr(path[i][j] + path[i + 1][j] >= 1 + s)  # s = 0: >= 1     s = 1: >= 2

    # for i in range(n):
    #     for j in range(n - 1):
    #         if i == 0 and j == 0: continue  # Exempt the top left corner and a neighbour so that the model
    #         if i == 0 and j == 1: continue  # has someplace to start
    #
    #         t = m.addVar(vtype=GRB.BINARY)
    #         m.addConstr(path[i][j] + path[i][j + 1] <= 1 + t)  # t = 0: <= 1       t = 1: <= 2
    #         m.addConstr(path[i][j] + path[i][j + 1] >= 1 + t)  # t = 0: >= 1       t = 1: >= 2

    # Number of covered squares + number of tiles in the path == n * n
    number_of_uncovered_squares = gp.LinExpr()
    number_of_tiles_on_path = gp.LinExpr()
    # number_of_covered_squares = gp.LinExpr()

    for i in range(n):
        for j in range(n):
            number_of_uncovered_squares.add(1 - is_covered[i][j])
            number_of_tiles_on_path.add(path[i][j])
            # number_of_covered_squares.add(path[i][j])

    m.addConstr(number_of_tiles_on_path + number_of_uncovered_squares == n*n)
