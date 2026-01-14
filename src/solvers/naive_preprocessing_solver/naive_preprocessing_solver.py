import time
import gurobipy as gp
from gurobipy import GRB

from src.connected_checkers.connected_checker import ConnectedChecker
from src.constraints.naive_adjacent_constraint import naive_adjacent_constraint
from src.constraints.naive_unique_constraint import naive_unique_constraint
from src.constraints.redundant_constraints.redundant_constraint import RedundantConstraint
from src.heuristics.heuristic import Heuristic
from src.solvers.naive_solver.helper_methods.add_illegal_solution import add_illegal_solution
from src.solvers.naive_solver.helper_methods.extract_solution import extract_solution
from src.solvers.set_model_parameters import set_model_parameters
from src.solvers.solver import Solver


class NaivePreprocessingSolver(Solver):
    name = ""
    redundant_constraints: list[RedundantConstraint] = []
    connected_checker: ConnectedChecker = None
    heuristic: Heuristic = None

    def __init__(self, name, redundant_constraints, connected_checker, heuristic):
        self.name = name
        self.redundant_constraints = redundant_constraints
        self.connected_checker = connected_checker
        self.heuristic = heuristic

    def solve(self, n, board):
        # Create a new model
        m = gp.Model(self.name)

        # Don't set the seed, we want to take an average over many seeds
        m.params.OutputFlag = 0
        m.params.MemLimit = 8
        m.params.Threads = 1

        is_covered = list()

        for i in range(n):
            new_list = list()
            for j in range(n):
                new_list.append(m.addVar(vtype=GRB.BINARY, name=f'is_covered {i}_{j}'))
            is_covered.append(new_list)
        m.update()

        #Add optimisations
        for redundant_constraint in self.redundant_constraints:
            redundant_constraint.apply(board, is_covered, [], n, m)

        # Adjacency constraint
        naive_adjacent_constraint(n, is_covered, m)

        # Unique constraint
        naive_unique_constraint(n, is_covered, board, m)

        self.heuristic.apply(n, is_covered, m)

        # Optimise the model
        try:
            m.optimize()
        except GRB.ERROR_OUT_OF_MEMORY:
            print("Out of Memory")

        # Extract values
        white, black, grid = extract_solution(n, m, is_covered)
        t1 = time.process_time_ns()
        iteration = 1

        while not self.connected_checker.check(n, grid):
            add_illegal_solution(white, black, m, iteration)
            m.optimize()

            white, black, grid = extract_solution(n, m, is_covered)
            iteration += 1

        iteration_time = (time.process_time_ns() - t1) / 1000000000

        data = {
            "iterations": iteration,
            "time spent on iterations": iteration_time
        }

        return data
