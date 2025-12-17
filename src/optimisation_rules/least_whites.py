import math
import gurobipy as gp

# Uses the fact that each row and column must have at least floor(n/2) uncovered tiles.
# This and most_blacks do the same. There is no reason to use both at the same time.
def least_whites(is_covered, duplicates, n, m, has_duplicates=False):
    for i in range(n):
        missing_vars = 0
        expr = gp.LinExpr()
        for j in range(n):
            if not has_duplicates:
                expr += 1 - is_covered[i][j]
            else:
                if duplicates[i][j] != 0:
                    expr += 1 - is_covered[i][j]
                else: missing_vars += 1
        m.addConstr(expr + missing_vars >= math.floor(n / 2))

    for j in range(n):
        missing_vars = 0
        expr = gp.LinExpr()
        for i in range(n):
            if not has_duplicates:
                expr += 1 - is_covered[i][j]
            else:
                if duplicates[i][j] != 0:
                    expr += 1 - is_covered[i][j]
                else: missing_vars += 1
        m.addConstr(expr + missing_vars >= math.floor(n / 2))
