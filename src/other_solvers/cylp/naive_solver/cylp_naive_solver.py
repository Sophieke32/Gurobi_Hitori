import time

import highspy

from src.connected_checkers.connected_checker import ConnectedChecker
from src.constraints.redundant_constraints.redundant_constraint import RedundantConstraint
from src.other_solvers.cylp.naive_solver.cylp_naive_unique_constraint import cylp_naive_unique_constraint
from src.other_solvers.cylp.naive_solver.helper_methods.cylp_add_illegal_solution import cylp_add_illegal_solution
from src.other_solvers.cylp.naive_solver.helper_methods.cylp_extract_solution import cylp_extract_solution
from src.other_solvers.cylp.naive_solver.helper_methods.cylp_pretty_print import cylp_pretty_print
from src.heuristics.heuristic import Heuristic
from src.other_solvers.scipopt.naive_solver.helper_methods.scipopt_extract_solution import scipopt_extract_solution
from src.other_solvers.scipopt.naive_solver.helper_methods.scipopt_pretty_print import scipopt_pretty_print
from src.other_solvers.cylp.naive_solver.cylp_naive_adjacent_constraint import cylp_naive_adjacent_constraint
from src.solvers.solver import Solver


class CylpNaiveSolver(Solver):
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

        m = highspy.Highs()

        # set_model_parameters(m)

        is_covered = list()

        for i in range(n):
            new_list = list()
            for j in range(n):
                new_list.append(m.addVariable(0, 1))
            is_covered.append(new_list)


        #Add optimisations
        t1 = time.process_time_ns()
        for redundant_constraint in self.redundant_constraints:
            redundant_constraint.apply(board, is_covered, [], n, m)

        time_spent_on_optimisations = (time.process_time_ns() - t1) / 1000000000

        # Adjacency constraint
        cylp_naive_adjacent_constraint(n, is_covered, m)

        # Unique constraint
        cylp_naive_unique_constraint(n, is_covered, board, m)

        # Apply Heuristic
        self.heuristic.apply(n, is_covered, m)


        m.run()

        print("Var 0_0", is_covered[0][0].value())

        # Extract values
        uncovered, covered, grid = cylp_extract_solution(n, m, is_covered)
        cylp_pretty_print(m, is_covered, n, board)
        iteration = 0

        while not self.connected_checker.check(n, grid):
            # print("Infeasible iteration")
            cylp_add_illegal_solution(uncovered, covered, m, iteration, is_covered, n)
            m.run()
            print(m.getModelStatus())

            uncovered, covered, grid = scipopt_extract_solution(n, m, is_covered)
            print("\n")
            scipopt_pretty_print(m, is_covered, n, board)
            iteration += 1


        # scipopt_pretty_print(m, is_covered, n, board)
        print("SOLVED")
        return m, is_covered, time_spent_on_optimisations
