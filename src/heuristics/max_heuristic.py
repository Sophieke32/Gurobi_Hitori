import gurobipy as gp
from gurobipy import GRB

from src.heuristics.abstract_heuristic import Heuristic


class MaxHeuristic(Heuristic):

    def apply(self, n, is_covered, m):
        expr = gp.LinExpr()

        for i in range(n):
            for j in range(n):
                expr += is_covered[i][j]

        m.setObjective(expr, GRB.MAXIMIZE)