import gurobipy as gp
from gurobipy import GRB

from src.constraints.naive_adjacent_constraint import naive_adjacent_constraint
from src.constraints.naive_unique_constraint import naive_unique_constraint
from src.constraints.path_connected_constraint import path_connected_constraint
from src.constraints.redundant_constraints.redundant_constraint import RedundantConstraint
from src.solvers.set_model_parameters import set_model_parameters
from src.solvers.solver import Solver


class PathSolver(Solver):
    name = ""
    redundant_constraints: list[RedundantConstraint] = []

    def __init__(self, name, redundant_constraints):
        self.name = name
        self.redundant_constraints = redundant_constraints

    def solve(self, n, board):
        # Create a new model
        m = gp.Model(self.name)

        set_model_parameters(m)

        is_covered = list()

        for i in range(n):
            new_list = list()
            for j in range(n):
                new_list.append(m.addVar(vtype=GRB.BINARY, name=f'is_covered {i}_{j}'))
            is_covered.append(new_list)
        m.update()

        # Add optimisations
        for redundant_constraint in self.redundant_constraints:
            redundant_constraint.apply(board, is_covered, [], n, m)

        # Adjacency constraint
        naive_adjacent_constraint(n, is_covered, m)

        # Unique constraint
        naive_unique_constraint(n, is_covered, board, m)

        # Connected constraint
        path = path_connected_constraint(n, is_covered, m)

        # Optimise the model
        try:
            m.optimize()
        except GRB.ERROR_OUT_OF_MEMORY:
            print("Out of Memory")


        return m, is_covered, path