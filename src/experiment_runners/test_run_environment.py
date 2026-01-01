# import csv
# import os
# from datetime import datetime
#
# from src.experiment_runners.run_environment import RunEnvironment
#
#
# class TestRunEnvironment(RunEnvironment):
#     solver = None
#     writer = None
#
#     def __init__(self, solver):
#         self.solver = solver
#
#         with open(os.path.join("experiments", self.solver.name,
#                      datetime.now().strftime("%Y-%m-%d_%H-%M-%S"), ".csv"), "w",
#         newline = '') as csvfile:
#             self.writer = csv.DictWriter(csvfile,
#                                     fieldnames=["instance", "n", "cpu_time (s)",
#                                                 "solution found"])
#             self.writer.writeheader()
#
#     def run_puzzle(self, file):
#         n, number_of_cycles, number_of_covered_squares, time, solution = self.solver.solve(self.solver.)
#
#         # pretty_print(m, is_covered, n, board)
#         self.writer.writerow({"instance": file, "n": n, "cpu_time (s)": time,
#             "solution found": solution})
#
