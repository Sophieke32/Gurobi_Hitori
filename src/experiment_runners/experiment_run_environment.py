import csv
from datetime import datetime
import time
import os
import signal

from src.experiment_runners.run_environment import RunEnvironment


class ExperimentRunEnvironment(RunEnvironment):
    solver = None
    time_out = 10
    path = None

    def __init__(self, solver, time_out=10):
        self.solver = solver
        self.time_out = time_out
        self.path = os.path.join("experiments", self.solver.name,
                     datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".csv")

        with open(self.path, "w", newline = '') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["instance", "n", "cpu_time (s)", "number_of_cycles",
                                                         "number_of_duplicates", "number_of_covered_tiles"])
            writer.writeheader()

    def run_puzzle(self, n, board, file, **kwargs):

        try:
            signal.alarm(self.time_out)
            start = time.process_time_ns()

            self.solver.solve(n, board)

            end = time.process_time_ns()
            signal.alarm(0)

            cpu_time = (end - start) / 1000000000

        except TimeoutError:
            print("Experiment timed out")
            cpu_time = 2 * self.time_out

        with open(self.path, "a", newline = '') as csvfile:
            self.writer = csv.DictWriter(csvfile,
                                    fieldnames=["instance", "n", "cpu_time (s)", "number_of_cycles",
                                                         "number_of_duplicates", "number_of_covered_tiles"])
            self.writer.writerow({"instance": file, "n": n, "cpu_time (s)": cpu_time,
                                  "number_of_cycles": kwargs["number_of_cycles"],
                                  "number_of_duplicates": kwargs["number_of_duplicates"],
                                  "number_of_covered_tiles": kwargs["number_of_covered_tiles"]})

        return cpu_time


def handle_timeout(sig, frame):
    raise TimeoutError("Took too long")
