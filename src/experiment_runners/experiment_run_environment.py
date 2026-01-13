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
        self.path = os.path.join("experiments",
                     self.solver.name + ".csv")

        with open(self.path, "w", newline = '') as csvfile:
            # writer = csv.DictWriter(csvfile, fieldnames=["instance", "n", "cpu_time (s)", "duplicates time (s)",
            #                                              "graph time (s)", "time spent on optimisations (s)",
            #                                              "number_of_cycles",
            #                                              "number_of_duplicates", "number_of_covered_tiles",
            #                                              "corner_check_hits", "edge_pairs_hits",
            #                                              "pairs_isolation_hits", "sandwich_pairs_hits",
            #                                              "sandwich_triple_hits",
            #                                              ])
            writer = csv.DictWriter(csvfile, fieldnames=["instance", "n", "cpu_time (s)"])
            writer.writeheader()

    def run_puzzle(self, n, board, file, **kwargs):

        signal.signal(signal.SIGALRM, handle_timeout)

        try:
            signal.alarm(self.time_out)
            start = time.process_time_ns()

            m, is_covered, time_spent_on_optimisations = self.solver.solve(n, board)

            end = time.process_time_ns()
            signal.alarm(0)

            cpu_time = (end - start) / 1000000000

        except TimeoutError:
            print("Experiment timed out")
            cpu_time = 2 * self.time_out
            time_spent_on_optimisations = 0

        with open(self.path, "a", newline = '') as csvfile:
            # self.writer = csv.DictWriter(csvfile,
            #                         fieldnames=["instance", "n", "cpu_time (s)", "duplicates time (s)",
            #                                     "graph time (s)", "time spent on optimisations (s)",
            #                                     "number_of_cycles",
            #                                     "number_of_duplicates", "number_of_covered_tiles",
            #                                     "corner_check_hits", "edge_pairs_hits",
            #                                     "pairs_isolation_hits", "sandwich_pairs_hits",
            #                                     "sandwich_triple_hits",
            #                                     ])
            #
            #
            #
            # self.writer.writerow({"instance": file, "n": n, "cpu_time (s)": cpu_time,
            #                       "duplicates time (s)": kwargs["data"]["duplicates_time"],
            #                       "graph time (s)": kwargs["data"]["graph_time"],
            #                       "time spent on optimisations (s)": time_spent_on_optimisations,
            #                       "number_of_cycles": kwargs["data"]["number_of_cycles"],
            #                       "number_of_duplicates": kwargs["data"]["number_of_duplicates"],
            #                       "number_of_covered_tiles": kwargs["data"]["number_of_covered_tiles"],
            #                       "corner_check_hits": kwargs["data"]["corner_check_hits"],
            #                       "edge_pairs_hits": kwargs["data"]["edge_pairs_hits"],
            #                       "pairs_isolation_hits": kwargs["data"]["pair_isolation_hits"],
            #                       "sandwich_pairs_hits": kwargs["data"]["sandwich_pairs_hits"],
            #                       "sandwich_triple_hits": kwargs["data"]["sandwich_triple_hits"],
            #                       })

            self.writer = csv.DictWriter(csvfile,
                                         fieldnames=["instance", "n", "cpu_time (s)"])

            self.writer.writerow({"instance": file, "n": n, "cpu_time (s)": cpu_time})

        return cpu_time


def handle_timeout(sig, frame):
    raise TimeoutError("Took too long")
