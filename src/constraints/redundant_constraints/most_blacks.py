import math
import gurobipy as gp

from src.constraints.redundant_constraints.redundant_constraint import RedundantConstraint

class MostBlacksConstraint(RedundantConstraint):

    # Uses the fact that each row and column can have at most ceil(n/2) covered tiles.
    # This and least_whites do the same. There is no reason to use both at the same time.
    def apply(self, board, is_covered, duplicates, n, m, has_duplicates=False):
        for i in range(n):
            expr = gp.LinExpr()
            for j in range(n):
                if not has_duplicates:
                    expr += is_covered[i][j]
                else:
                    if duplicates[i][j] != 0:
                        expr += is_covered[i][j]
            m.addConstr(expr <= math.ceil(n / 2))

        for j in range(n):
            expr = gp.LinExpr()
            for i in range(n):
                if not has_duplicates:
                    expr += is_covered[i][j]
                else:
                    if duplicates[i][j] != 0:
                        expr += is_covered[i][j]
            m.addConstr(expr <= math.ceil(n / 2))
