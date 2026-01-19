import os

from src.experiment_runners.run_environment import RunEnvironment
from src.write_results import get_results


class BenchmarkRunEnvironment(RunEnvironment):
    solver = None
    time_out = 10
    path = None

    def __init__(self, solver, directory_name, time_out=10):
        self.solver = solver
        self.time_out = time_out
        self.path = directory_name


    def run_puzzle(self, n, board, file, **kwargs):

        try:
            m, is_covered, time_spent_on_optimisations = self.solver.solve(n, board)
            write_to_file_success(m, is_covered, n, board, self.path, file)

        except TimeoutError:
            print("Experiment timed out")
            write_to_file_failure(self.path, file)


def write_to_file_success(m, is_covered, n, board, root, file):
    print("Writing to file:", root + "/" + file + "sol")
    with open(os.path.join(root, file + "sol"), "w") as f:
        f.write(get_results(m, is_covered, n, board))
        f.write("\n")

        with open(os.path.join(root, file), "r") as source:
            for line in source:
                if len(line) > 0 and line[0] != "@" and line[0] != "#":
                    continue
                else:
                    f.write(line)


def write_to_file_failure(root, file):
    with open(os.path.join(root + "_solutions", file + "sol"), "w") as f:
        f.write("Timed out")
