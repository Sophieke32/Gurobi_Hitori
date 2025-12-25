import gurobipy as gp
from gurobipy import GRB

from src.heuristics.abstract_heuristic import Heuristic


class NoHeuristic(Heuristic):

    def apply(self, n, is_covered, m):
        pass