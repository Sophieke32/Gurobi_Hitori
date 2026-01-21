import time

import ilpy

from src.connected_checkers.connected_checker import ConnectedChecker
from src.constraints.redundant_constraints.redundant_constraint import RedundantConstraint
from src.heuristics.heuristic import Heuristic
from src.other_solvers.ilpy.naive_solver.helper_methods.ilpy_add_illegal_solution import ilpy_add_illegal_solution
from src.other_solvers.ilpy.naive_solver.helper_methods.ilpy_extract_solution import ilpy_extract_solution
from src.other_solvers.ilpy.naive_solver.helper_methods.ilpy_pretty_print import ilpy_pretty_print
from src.other_solvers.ilpy.naive_solver.ilpy_naive_adjacent_constraint import ilpy_naive_adjacent_constraint
from src.other_solvers.ilpy.naive_solver.ilpy_naive_unique_constraint import ilpy_naive_unique_constraint
from src.other_solvers.scipopt.naive_solver.helper_methods.scipopt_extract_solution import scipopt_extract_solution
from src.other_solvers.scipopt.naive_solver.helper_methods.scipopt_pretty_print import scipopt_pretty_print
from src.solvers.solver import Solver


class IlpyNaiveSolver(Solver):
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
        m = ilpy

        # set_model_parameters(m)

        is_covered = list()

        for i in range(n):
            new_list = list()
            for j in range(n):
                new_list.append(m.Variable(0, 1))
            is_covered.append(new_list)


        #Add optimisations
        t1 = time.process_time_ns()
        for redundant_constraint in self.redundant_constraints:
            redundant_constraint.apply(board, is_covered, [], n, m)

        time_spent_on_optimisations = (time.process_time_ns() - t1) / 1000000000

        # Adjacency constraint
        ilpy_naive_adjacent_constraint(n, is_covered, m)

        # Unique constraint
        ilpy_naive_unique_constraint(n, is_covered, board, m)

        # Apply Heuristic
        self.heuristic.apply(n, is_covered, m)


        m.solve()

        print("Var 0_0", is_covered[0][0].value())

        # Extract values
        uncovered, covered, grid = ilpy_extract_solution(n, m, is_covered)
        ilpy_pretty_print(m, is_covered, n, board)
        iteration = 0

        while not self.connected_checker.check(n, grid):
            # print("Infeasible iteration")
            ilpy_add_illegal_solution(uncovered, covered, m, iteration, is_covered, n)
            m.run()
            print(m.getModelStatus())

            uncovered, covered, grid = scipopt_extract_solution(n, m, is_covered)
            print("\n")
            scipopt_pretty_print(m, is_covered, n, board)
            iteration += 1


        # scipopt_pretty_print(m, is_covered, n, board)
        print("SOLVED")
        return m, is_covered, time_spent_on_optimisations
