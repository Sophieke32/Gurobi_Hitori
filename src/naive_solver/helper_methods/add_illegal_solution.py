import gurobipy as gp
from gurobipy import GRB

# Takes the current solution and makes it illegal
#
# Does so by creating a binary decision variable v
# if v = 0, at least one of the current black squares must be made white
# if v = 1, at least one additional square must be made black
def add_illegal_solution(white, black, m, iteration):
    v = m.addVar(vtype=GRB.BINARY, name=f'illegal solution {iteration} decision variable')

    expr_white = gp.LinExpr()
    for w in white:
        expr_white += w
    m.addConstr(v * expr_white != len(white))

    expr_black = gp.LinExpr()
    for b in black:
        expr_black += b
    m.addConstr((1-v) * expr_black != len(black))

    m.update()