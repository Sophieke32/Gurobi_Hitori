from src.check_solution import check_solution
from src.experiment_runners.run_environment import RunEnvironment
from src.pretty_print import path_pretty_print, pretty_print
from src.solvers.naive_solver.helper_methods.extract_solution import extract_solution


class TestRunEnvironment(RunEnvironment):
    solver = None
    time_out = 10

    def __init__(self, solver, time_out=10):
        self.solver = solver
        self.time_out = time_out

    def run_puzzle(self, n, board, file, **kwargs):
        m, is_covered, path = self.solver.solve(n, board)

        path_pretty_print(m, is_covered, path, n, board)

        uncovered, covered, grid = extract_solution(n, m, is_covered)
        print("Solution validity:", check_solution(board, grid, n))
