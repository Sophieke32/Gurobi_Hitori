import gurobipy as gp
from gurobipy import GRB

def minimise_black_squares_objective(n, is_black, m):
    expr = gp.LinExpr()

    for i in range(n):
        for j in range(n):
            expr += is_black[i][j]

    m.setObjective(expr, GRB.MAXIMIZE)