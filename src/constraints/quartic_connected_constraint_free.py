import gurobipy as gp
import numpy as np
from gurobipy import GRB


def quadratic_path_connected_constraint_free(n, is_covered, m):
    # Make another 2d array of variables in the size of the board
    path = list()

    for i in range(n):
        path.append(list())
        for j in range(n):
            new_list = list()

            for k in range(n * n):
                new_list.append(m.addVar(vtype=GRB.BINARY, name=f'path_{i}_{j}_[{k}]'))
                # new_list.append(f'{i}_{j}_{k}')
            path[i].append(new_list)
    m.update()

    # Covered tiles cannot be on the path
    m.addConstrs(path[x][y][z] <= 1 - is_covered[x][y] for x in range(n) for y in range(n) for z in range(n*n))
    m.update()

    # Allow path-making. path[x][y][z] may be set to 1 if one of its neighbour has path[a][b][z-1] set to 1
    for i in range(1, n-1):
        if not i == 1 and not i == 2:
            m.addConstr(path[i][0][0] <= 0)
        m.addConstrs(path[i][0][z] <= path[i-1][0][z-1] + path[i][1][z-1] + path[i+1][0][z-1] for z in range(1, n*n))

    for i in range(1, n-1):
        m.addConstr(path[i][n-1][0] <= 0)
        m.addConstrs(path[i][n-1][z] <= path[i-1][n-1][z-1] + path[i][n-2][z-1] + path[i+1][n-1][z-1] for z in range(1, n*n))


    for j in range(1, n-1):
        m.addConstr(path[0][j][0] <= 0)
        m.addConstrs(path[0][j][z] <= path[0][j-1][z-1] + path[1][j][z-1] + path[0][j+1][z-1] for z in range(1, n*n))
        m.addConstr(path[-1][j][0] <= 0)
        m.addConstrs(path[n-1][j][z] <= path[n-1][j-1][z-1] + path[n-2][j][z-1] + path[n-1][j+1][z-1] for z in range(1, n*n))


    m.addConstr(path[0][0][0] <= 0)
    m.addConstrs(path[0][0][z] <= path[0][1][z - 1] + path[1][0][z - 1] for z in range(1, n * n))

    m.addConstr(path[-1][0][0] <= 0)
    m.addConstrs(path[-1][0][z] <= path[-1][1][z - 1] + path[-2][0][z - 1] for z in range(1, n * n))

    m.addConstr(path[0][-1][0] <= 0)
    m.addConstrs(path[0][-1][z] <= path[1][-1][z - 1] + path[0][-2][z - 1] for z in range(1, n * n))

    m.addConstr(path[-1][-1][0] <= 0)
    m.addConstrs(path[-1][-1][z] <= path[-2][-1][z - 1] + path[-1][-2][z - 1] for z in range(1, n * n))

    m.addConstrs(path[x][y][0] <= 0 for x in range(1, n-1) for y in range(1, n-1))
    m.addConstrs(path[x][y][z] <= path[x-1][y][z-1] + path[x+1][y][z-1] + path[x][y-1][z-1] + path[x][y+1][z-1]
                             for x in range(1, n-1) for y in range(1, n-1) for z in range(1, n*n))

    m.update()

    number_of_path_tiles = gp.LinExpr()

    for i in range(n):
        for j in range(n):
            sum_of_path = gp.LinExpr()
            for k in range(n * n):
                sum_of_path += path[i][j][k]

            s = m.addVar(vtype=GRB.BINARY, name=f'on_path_{i}_{j}')
            m.addConstr(s <= sum_of_path)
            number_of_path_tiles += s

            # number_of_uncovered_squares.add(1 - is_covered[i][j])
            # number_of_tiles_on_path.add(path[i][j])
            # number_of_covered_squares.add(path[i][j])

    number_of_covered_tiles = gp.LinExpr()

    for i in range(n):
        for j in range(n):
            number_of_covered_tiles += (is_covered[i][j])

    m.addConstr(number_of_path_tiles + number_of_covered_tiles == n * n)

    # m.setObjective(number_of_path_tiles, GRB.MAXIMIZE)
    m.update()

    return path
