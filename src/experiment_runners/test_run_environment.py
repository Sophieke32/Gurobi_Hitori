from src.check_solution import check_solution
from src.experiment_runners.run_environment import RunEnvironment
from src.other_solvers.scipopt.naive_solver.vars.var_scipopt_extract_solution import var_scipopt_extract_solution
from src.other_solvers.scipopt.naive_solver.vars.var_scipopt_pretty_print import var_scipopt_pretty_print
from src.pretty_print import path_pretty_print, pretty_print
from src.solvers.naive_solver.helper_methods.extract_solution import extract_solution


class TestRunEnvironment(RunEnvironment):
    solver = None
    time_out = 10

    def __init__(self, solver, time_out=10):
        self.solver = solver
        self.time_out = time_out

    def run_puzzle(self, n, board, file, **kwargs):
        # m, is_covered, time_spent_on_optimisations, path = self.solver.solve(n, board)
        m, is_covered, time_spent_on_optimisations = self.solver.solve(n, board)


        uncovered, covered, grid = extract_solution(n, m, is_covered)
        # uncovered, covered, grid = var_scipopt_extract_solution(n, m, is_covered, self.solver.that_one_var)
        validity = check_solution(board, grid, n)
        print("Solution validity:", check_solution(board, grid, n))

        if not validity:
            # path_pretty_print(m, is_covered, path, n, board)
            # var_scipopt_pretty_print(m, is_covered, n, board, self.solver.that_one_var)
            raise Exception("file:", file)
