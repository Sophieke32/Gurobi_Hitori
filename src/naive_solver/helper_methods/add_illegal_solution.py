import gurobipy as gp
from gurobipy import GRB

# Takes the current solution and makes it illegal
#
# Does so by creating a binary decision variable v
# if v = 0, at least one of the current black squares must be made white
# if v = 1, at least one additional square must be made black
#
# v_covered only matters if v = 1.
# Then, if v_covered = 0, there must be at least one less covered tile
# else, if v_covered = 1, there must be at least one more covered tile
def add_illegal_solution(white, black, m, iteration):
    v0 = m.addVar(vtype=GRB.BINARY, name=f'illegal solution {iteration} decision variable')
    # v_covered = m.addVar(vtype=GRB.BINARY, name=f'illegal solution {iteration} decision variable covered squares')

    expr_white = gp.LinExpr()

    for w in white:
        expr_white += w
    m.addConstr(expr_white >= 1 - (v0 * 10000))

    expr_black = gp.LinExpr()
    for b in black:
        expr_black += b
    m.addConstr(expr_black <= len(black) - 1 + ((1 - v0) * 10000))
    # m.addConstr(expr_black <= len(black) - 1 + (v_covered * 100000) + ((1 - v0) * 10000))
    # m.addConstr(expr_black >= len(black) + 1 - ((1 - v_covered) * 10000) - ((1 - v0) * 10000))

    m.update()
