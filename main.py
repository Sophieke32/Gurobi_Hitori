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
from src.constraints.redundant_constraints.set_unique_values import SetUniqueValuesConstraint
from src.experiment_runners.experiment_run_environment import ExperimentRunEnvironment
from src.experiment_runners.preprocess_run_environment import PreprocessRunEnvironment
from src.experiment_runners.run_environment import RunEnvironment
from src.experiment_runners.test_run_environment import TestRunEnvironment
from src.heuristics.max_heuristic import MaxHeuristic
from src.heuristics.min_heuristic import MinHeuristic
from src.heuristics.no_heuristic import NoHeuristic
from src.main import main
from src.read_file import read_file
from src.solvers.duplicates_solver.duplicates_solver import DuplicatesSolver
from src.solvers.naive_solver.naive_solver import NaiveSolver
from src.solvers.path_solver.path_solver import PathSolver
from src.solvers.preprocessing_solver.preprocessing_solver import PreprocessingSolver

#############################
#        All options        #
#############################

heuristics = {"min": MinHeuristic(), "max": MaxHeuristic(), "no": NoHeuristic()}
connected_checkers = {"bfs": BFSConnectedChecker(), "cycles": CyclesConnectedChecker(), "cc": ConnectedComponentsConnectedChecker()}
redundant_constraints = {"cch": CornerCheckConstraint, "edge pairs": EdgePairsConstraint(),
    "least whites": LeastWhitesConstraint(), "most blacks": MostBlacksConstraint(),
    "pair isolation": PairIsolationConstraint(), "sandwiches": SandwichesConstraint()}
naive_only_redundant_constraints = {"cc": CornerCloseConstraint()}
duplicates_only_redundant_constraints = {"set unique values": SetUniqueValuesConstraint()}


def collect_all_data(directory_name):
    all_solvers = []

    # for key, value in heuristics.items():
    #     all_solvers.append(
    #         NaiveSolver("naive solver " + key + " heuristic", [], connected_checkers["bfs"], value))
    #
    # for key, value in connected_checkers.items():
    #     all_solvers.append(
    #         NaiveSolver("naive solver" + key + " checker", [], value, heuristics["min"]))

    all_solvers.append(
        NaiveSolver("naive_solver", [], connected_checkers["bfs"], heuristics["min"]))

    # for key, value in redundant_constraints.items():
    #     all_solvers.append(
    #         NaiveSolver("naive solver " + key + "constraint", value, connected_checkers["bfs"], heuristics["min"]))
    #
    # for key, value in naive_only_redundant_constraints.items():
    #     all_solvers.append(
    #         NaiveSolver("naive solver " + key + "constraint", value, connected_checkers["bfs"], heuristics["min"]))

    all_solvers.append(
        DuplicatesSolver("duplicates_solver", []))

    # for key, value in redundant_constraints.items():
    #     all_solvers.append(
    #         DuplicatesSolver("duplicates_solver_" + key + "constraint", value))
    #
    # for key, value in duplicates_only_redundant_constraints.items():
    #     all_solvers.append(
    #         DuplicatesSolver("duplicates solver " + key + "constraint", value))

    run_environments = []
    for solver in all_solvers:
        run_environments.append(ExperimentRunEnvironment(solver))


    i = 1
    for root, dirs, files in os.walk(directory_name):
        for file in files:
            if file.endswith(".singles"):

                n, board, number_of_covered_tiles, number_of_cycles = read_file(root, file)

                for environment in run_environments:
                    cpu_time = environment.run_puzzle(n, board, file)

                    print(i, n, cpu_time, environment.solver.name)
                    i += 1
        print(root)

def run_preprocess(directory_name):
    solver = PreprocessingSolver("preprocessing solver", [])
    i = 1
    for root, dirs, files in os.walk(directory_name):
        environment = PreprocessRunEnvironment(solver, root=root)
        for file in files:
            if file.endswith(".singles"):

                n, board, number_of_covered_tiles, number_of_cycles = read_file(root, file)

                cpu_time = environment.run_puzzle(n, board, file)

                print(i, n, cpu_time, environment.solver.name)
                i += 1
        print(root)


if __name__ == "__main__":
    # test()

    parser = argparse.ArgumentParser(description="Solve n x n Hitori puzzle(s)")

    parser.add_argument(
        "-d", "--dirname",
        type=str,
        required=True,
        help="Directory from which all .singles files will be read. Will also read sub-directories."
    )

    parser.add_argument(
        "-a", "--all",
        type=bool,
        default=False,
        help="If true, will time all variations of models, heuristics, redundant constraints, and path checkers. Collects"
             " all data required for our data analysis. Skips all other arguments except -d as a result"
    )

    parser.add_argument(
        "-p", "--preprocess",
        type=bool,
        default=False,
        help="Runs through the given puzzles and finds the number of covered tiles in the solution, duplicates values, "
             "and number of cycles"
    )

    parser.add_argument(
        "-m", "--model",
        type=str,
        default="duplicates",
        help="Model that will be used. Can be 'duplicates' or 'naive'. If given none, will use 'duplicates'."
    )

    parser.add_argument(
        "-t", "--time",
        type=bool,
        default=False,
        help="Determines whether a csv will be made with the time it took to solve each instance"
    )

    args = parser.parse_args()

    directory_name = args.dirname
    run_all = args.all
    preprocess = args.preprocess
    model = args.model
    time = args.time

    if run_all:
        collect_all_data(directory_name)
    elif preprocess:
        run_preprocess(directory_name)
    else:
        print("Solving all puzzles in file:", directory_name)
        print("Using model:", model)

        if model == "duplicates":
            print("Running the duplicates model")
            solver = DuplicatesSolver("duplicates_solver", [])
        elif model == "path":
            print("Running the path model")
            solver = PathSolver("path_solver", [])
        else:
            print("Running the naive model")
            solver = NaiveSolver("naive_solver", [])

        if time:
            print("Running in the Experiment Run Environment")
            environment = ExperimentRunEnvironment(solver)
        else:
            print("Running in the Testing Run Environment")
            environment = TestRunEnvironment(solver)

        i = 0

        print("Directory name:", directory_name)

        for root, dirs, files in os.walk(directory_name):
            for file in files:
                if file.endswith(".singles"):

                    n, board, number_of_covered_tiles, number_of_cycles = read_file(root, file)

                    cpu_time = environment.run_puzzle(n, board, file)

                    print(i, n, cpu_time, environment.solver.name)
                    i += 1
            print(root)
