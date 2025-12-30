import argparse
import os
import datetime
import csv

import numpy as np

from src.connected_checkers.bfs_connected_checker import BFSConnectedChecker
from src.connected_checkers.connected_components_connected_checker import ConnectedComponentsConnectedChecker
from src.connected_checkers.cycles_connected_checker import CyclesConnectedChecker
from src.constraints.redundant_constraints.corner_check_constraint import CornerCheckConstraint
from src.constraints.redundant_constraints.corner_close_constraint import CornerCloseConstraint
from src.constraints.redundant_constraints.edge_pairs import EdgePairsConstraint
from src.constraints.redundant_constraints.least_whites import LeastWhitesConstraint
from src.constraints.redundant_constraints.most_blacks import MostBlacksConstraint
from src.constraints.redundant_constraints.pair_isolation import PairIsolationConstraint
from src.constraints.redundant_constraints.sandwiches import SandwichesConstraint
from src.heuristics.max_heuristic import MaxHeuristic
from src.heuristics.min_heuristic import MinHeuristic
from src.heuristics.no_heuristic import NoHeuristic
from src.main import main
from src.solvers.duplicates_solver.duplicates_solver import DuplicatesSolver
from src.solvers.naive_solver.naive_solver import NaiveSolver


def test():
    heuristics = {"min": MinHeuristic(), "max": MaxHeuristic(), "no": NoHeuristic()}
    connected_checkers = {"bfs": BFSConnectedChecker(), "cycles": CyclesConnectedChecker(), "cc": ConnectedComponentsConnectedChecker()}
    redundant_constraints = {"cc": CornerCloseConstraint(), "cch": CornerCheckConstraint, "edge pairs": EdgePairsConstraint(),
                             "least whites": LeastWhitesConstraint(), "most blacks": MostBlacksConstraint(),
                             "pair isolation": PairIsolationConstraint(), "sandwiches": SandwichesConstraint()}
    naive_solver = NaiveSolver("naive solver", [], connected_checkers["bfs"], heuristics["min"])
    duplicates_solver = DuplicatesSolver("duplicates solver", [redundant_constraints["most blacks"]])

    naive_solver.solve(5, np.array([
        [1, 5, 5, 3, 1],
        [3, 2, 4, 3, 1],
        [5, 3, 1, 5, 2],
        [4, 5, 2, 5, 3],
        [1, 1, 4, 2, 4]]))

    duplicates_solver.solve(5, np.array([
        [1, 5, 5, 3, 1],
        [3, 2, 4, 3, 1],
        [5, 3, 1, 5, 2],
        [4, 5, 2, 5, 3],
        [1, 1, 4, 2, 4]]))


if __name__ == "__main__":
    test()

    # parser = argparse.ArgumentParser(description="solve n x n singles puzzle(s)")
    #
    # parser.add_argument(
    #     "-d", "--dirname",
    #     type=str,
    #     required=True,
    #     help="Directory in which all .singles files will be read. Will also read sub-directories."
    # )
    #
    # parser.add_argument(
    #     "-m", "--model",
    #     type=str,
    #     default="duplicates",
    #     help="Model that will be used. Can be 'duplicates' or 'naive'. If given none, will use 'duplicates'."
    # )
    #
    # parser.add_argument(
    #     "-t", "--time",
    #     type=bool,
    #     default=False,
    #     help="Determines whether a csv will be made with the time it took to solve each instance"
    # )
    #
    # args = parser.parse_args()
    #
    # directory_name = args.dirname
    # model = args.model
    # time = args.time
    #
    # print("Solving all puzzles in file:", directory_name)
    # print("Using model:", model)
    # if time: print("Storing time!")
    #
    # i = 0
    #
    # if time:
    #     with open(os.path.join("experiments", model, datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + "_" + model + ".csv"), "w", newline='') as csvfile:
    #         writer = csv.DictWriter(csvfile, fieldnames=["instance", "n", "number of cycles", "covered squares", "cpu_time (s)", "solution found"])
    #         writer.writeheader()
    #
    #         for root, dirs, files in os.walk(directory_name):
    #             for file in files:
    #                 if file.endswith(".singles"):
    #                     n, number_of_cycles, number_of_covered_squares, time, solution = main(root, file, model, time)
    #                     writer.writerow({"instance": file, "n": n, "number of cycles": number_of_cycles, "covered squares": number_of_covered_squares,"cpu_time (s)": time, "solution found": solution})
    #                     print(i, n, time)
    #                     i = i + 1
    #             print(root)
    #
    # else:
    #     for root, dirs, files in os.walk(directory_name):
    #         for file in files:
    #             if file.endswith(".singles"):
    #                 n, time, solution = main(root, file, model, False)
    #                 print(i, n, time)
    #                 i = i + 1
    #         print(root)
