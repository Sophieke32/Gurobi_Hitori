import time

from pyscipopt import Model

from src.connected_checkers.connected_checker import ConnectedChecker
from src.constraints.redundant_constraints.redundant_constraint import RedundantConstraint
from src.heuristics.heuristic import Heuristic
from src.other_solvers.scipopt.naive_solver.helper_methods.scipopt_add_illegal_solution import scipopt_add_illegal_solution
from src.other_solvers.scipopt.naive_solver.helper_methods.scipopt_extract_solution import scipopt_extract_solution
from src.other_solvers.scipopt.naive_solver.helper_methods.scipopt_pretty_print import scipopt_pretty_print
from src.other_solvers.scipopt.naive_solver.scipopt_min_heuristic import ScipOptMinHeuristic
from src.other_solvers.scipopt.naive_solver.scipopt_naive_adjacent_constraint import scipopt_naive_adjacent_constraint
from src.other_solvers.scipopt.naive_solver.scipopt_naive_unique_constraint import scipopt_naive_unique_constraint
from src.other_solvers.scipopt.naive_solver.vars.var_scipopt_extract_solution import var_scipopt_extract_solution
from src.other_solvers.scipopt.naive_solver.vars.var_scipopt_min_heuristic import VarScipOptMinHeuristic
from src.other_solvers.scipopt.naive_solver.vars.var_scipopt_naive_adjacent_constraint import \
    var_scipopt_naive_adjacent_constraint
from src.other_solvers.scipopt.naive_solver.vars.var_scipopt_naive_unique_constraint import \
    var_scipopt_naive_unique_constraint
from src.other_solvers.scipopt.naive_solver.vars.var_scipopt_pretty_print import var_scipopt_pretty_print
from src.solvers.solver import Solver


class ScipOptNaiveSolver(Solver):
    name = ""
    redundant_constraints: list[RedundantConstraint] = []
    connected_checker: ConnectedChecker = None
    heuristic: Heuristic = None
    that_one_var = None

    def __init__(self, name, redundant_constraints, connected_checker, heuristic):
        self.name = name
        self.redundant_constraints = redundant_constraints
        self.connected_checker = connected_checker
        self.heuristic = heuristic

    def solve(self, n, board):
        # Create a new model
        m = Model("scipopt_naive")

        # This one requires some explanation I'm afraid:
        # Creating constraints with is_covered[0][0] created buggy behaviour where is_covered[0][0] instead referred to
        # all variables in the model. I wasn't sure how to fix this (and frankly I was in a hurry), so instead I created
        # that_one_var which for all intents and purposes is is_covered[0][0].
        self.that_one_var = m.addVar(vtype='BINARY', name=f'This var is 0_0. Do not ask why, there might be a bug in SCIPOPT.')

        # set_model_parameters(m)
        m.hideOutput()

        is_covered = list()

        for i in range(n):
            new_list = list()
            for j in range(n):
                new_list.append(m.addVar(vtype='BINARY', name=f'is_covered {i}_{j}'))
            is_covered.append(new_list)


        #Add optimisations
        t1 = time.process_time_ns()
        for redundant_constraint in self.redundant_constraints:
            redundant_constraint.apply(board, is_covered, [], n, m)

        time_spent_on_optimisations = (time.process_time_ns() - t1) / 1000000000

        var_scipopt_naive_adjacent_constraint(n, is_covered, m, self.that_one_var)
        var_scipopt_naive_unique_constraint(n, is_covered, board, m, self.that_one_var)
        VarScipOptMinHeuristic().apply(n, is_covered, m, self.that_one_var)

        m.optimize()

        uncovered, covered, grid = var_scipopt_extract_solution(n, m, is_covered, self.that_one_var)
        # var_scipopt_pretty_print(m, is_covered, n, board, self.that_one_var)
        iteration = 0

        while not self.connected_checker.check(n, grid):
            # print("Infeasible iteration")
            scipopt_add_illegal_solution(uncovered, covered, m, iteration, self.that_one_var)
            m.optimize()
            # print(m.getStatus())

            uncovered, covered, grid = var_scipopt_extract_solution(n, m, is_covered, self.that_one_var)
            # print("\n")
            # var_scipopt_pretty_print(m, is_covered, n, board, self.that_one_var)
            iteration += 1


        # scipopt_pretty_print(m, is_covered, n, board)
        print("SOLVED")
        return m, is_covered, time_spent_on_optimisations
