import argparse
import os
import datetime

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
from src.other_solvers.cylp.naive_solver.cylp_min_heuristic import CylpMinHeuristic
from src.other_solvers.cylp.naive_solver.cylp_naive_solver import CylpNaiveSolver
from src.experiment_runners.benchmark_run_environment import BenchmarkRunEnvironment
from src.experiment_runners.experiment_run_environment import ExperimentRunEnvironment
from src.experiment_runners.preprocess_run_environment import PreprocessRunEnvironment
from src.experiment_runners.test_run_environment import TestRunEnvironment
from src.heuristics.max_heuristic import MaxHeuristic
from src.heuristics.min_heuristic import MinHeuristic
from src.heuristics.no_heuristic import NoHeuristic
from src.other_solvers.ilpy.naive_solver.ilpy_min_heuristic import IlpyMinHeuristic
from src.other_solvers.ilpy.naive_solver.ilpy_naive_solver import IlpyNaiveSolver
from src.other_solvers.scipopt.naive_solver.scipopt_min_heuristic import ScipOptMinHeuristic
from src.other_solvers.scipopt.naive_solver.scipopt_naive_solver import ScipOptNaiveSolver
from src.read_file import read_file
from src.solvers.duplicates_solver.duplicates_solver import DuplicatesSolver
from src.solvers.naive_preprocessing_solver.naive_preprocessing_solver import NaivePreprocessingSolver
from src.solvers.naive_solver.naive_solver import NaiveSolver
from src.solvers.path_solver.path_solver import PathSolver
from src.solvers.duplicates_preprocessing_solver.duplicates_preprocessing_solver import DuplicatesPreprocessingSolver
from src.solvers.path_solver.quartic_path_solver import QuarticPathSolver

#############################
#        All options        #
#############################

heuristics = {"min": MinHeuristic(), "max": MaxHeuristic(), "no": NoHeuristic()}
connected_checkers = {"bfs": BFSConnectedChecker(), "cycles": CyclesConnectedChecker(), "cc": ConnectedComponentsConnectedChecker()}
redundant_constraints = {"cch": CornerCheckConstraint(), "edge_pairs": EdgePairsConstraint(),
    "least_whites": LeastWhitesConstraint(), "most_blacks": MostBlacksConstraint(),
    "pair_isolation": PairIsolationConstraint(), "sandwiches": SandwichesConstraint()}
naive_only_redundant_constraints = {"cc": CornerCloseConstraint()}
# duplicates_only_redundant_constraints = {"set unique values": SetUniqueValuesConstraint()}

# Runs all combinations of solvers, heuristics, redundant constraints, and connected checkers on the directory
# in the ExperimentRunEnvironment
def collect_all_data(directory_name):
    all_solvers = []

    # Naive solvers
    for key, value in heuristics.items():
        all_solvers.append(
            NaiveSolver("naive_" + key + "_heuristic", [], connected_checkers["bfs"], value))

    for key, value in connected_checkers.items():
        all_solvers.append(
            NaiveSolver("naive_" + key + "_checker", [], value, heuristics["min"]))

    all_solvers.append(
        NaiveSolver("naive", [], connected_checkers["bfs"], heuristics["min"]))

    for key, value in redundant_constraints.items():
        all_solvers.append(
            NaiveSolver("naive_" + key + "_constraint", [value], connected_checkers["bfs"], heuristics["min"]))

    for key, value in naive_only_redundant_constraints.items():
        all_solvers.append(
            NaiveSolver("naive_" + key + "_constraint", [value], connected_checkers["bfs"], heuristics["min"]))

    # Duplicates Solvers
    all_solvers.append(
        DuplicatesSolver("duplicates", []))

    for key, value in redundant_constraints.items():
        all_solvers.append(
            DuplicatesSolver("duplicates_" + key + "_constraint", [value]))

    # QuarticPath solvers
    all_solvers.append(
        QuarticPathSolver("path", []))
    all_solvers.append(
        QuarticPathSolver("path_cc", [CornerCloseConstraint()])
    )

    for key, value in redundant_constraints.items():
        all_solvers.append(
            QuarticPathSolver("path_" + key + "_constraint", [value]))


    run_environments = []
    for solver in all_solvers:
        run_environments.append(ExperimentRunEnvironment(solver))

    run_instances(run_environments, directory_name)


# Preprocesses the files in the directory name. Runs
def run_preprocess(directory_name):
    s1 = DuplicatesPreprocessingSolver("duplicates preprocessing solver", [])
    s2 = NaivePreprocessingSolver("naive preprocessing solver", [], BFSConnectedChecker(), MinHeuristic())
    s3 = QuarticPathSolver("quartic preprocessing solver", [])

    i = 1
    for root, dirs, files in os.walk(directory_name):
        environment = PreprocessRunEnvironment(s1, root=root, second_solver=s2)
        for file in files:
            if file.endswith(".singles"):

                n, board, data = read_file(root, file)

                cpu_time = environment.run_puzzle(n, board, file)

                print(i, n, environment.solver.name)
                i += 1
        print(root)


# Runs a model on all .singles files in directory_name.
# Runs the model in the TestRunEnvironment, which actually checks solutions
# Manually change the code to change what model is run
def verify_instance(directory_name):
    # solver = QuarticPathSolver("quartic", [])
    solver = ScipOptNaiveSolver("cylp", [], BFSConnectedChecker(), ScipOptMinHeuristic())
    environment = TestRunEnvironment(solver)

    i = 1
    for root, dirs, files in os.walk(directory_name):
        for file in files:
            if file.endswith(".singles"):

                n, board, data = read_file(root, file)

                cpu_time = environment.run_puzzle(n, board, file, data=data)

                print(i, n, cpu_time, environment.solver.name)
                i += 1
        print(root)


# Currently there is no custom run setup
def run_custom(directory_name):
    # solver = ScipOptNaiveSolver("scipopt", [], BFSConnectedChecker(), ScipOptMinHeuristic())
    print("Not here right now")



# Runs all models in experiment mode on all files in custom_instances/ntest
def run_ntest(directory_name):
    all_solvers = []

    # all_solvers.append(
    #     QuarticPathSolver("path_ntest", []))
    # all_solvers.append(
    #     DuplicatesSolver("duplicates_ntest", []))
    # all_solvers.append(
    #     NaiveSolver("naive_ntest", [], BFSConnectedChecker(), MinHeuristic()))
    all_solvers.append(
        ScipOptNaiveSolver("scipopt_naive_ntest", [], BFSConnectedChecker(), ScipOptMinHeuristic()))

    run_environments = []
    for solver in all_solvers:
        run_environments.append(ExperimentRunEnvironment(solver))

    run_instances(run_environments, directory_name)


# Given an array of run_environments and a directory name, runs all
# run environments on all .singles files in the directory
def run_instances(run_environments, directory_name):
    i = 0
    start_time = datetime.datetime.now()

    for root, dirs, files in os.walk(directory_name):
        for file in files:
            if file.endswith(".singles"):

                n, board, data = read_file(root, file)


                for environment in run_environments:
                    cpu_time = environment.run_puzzle(n, board, file, data=data)

                    print(i, n, cpu_time, environment.solver.name)
                i += 1
        print(root)

    print("Job took:", datetime.datetime.now() - start_time)

if __name__ == "__main__":
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
        "-c", "--custom",
        type=bool,
        default=False,
        help="Runs a custom setup"
    )

    parser.add_argument(
        "-v", "--verify",
        type=bool,
        default=False,
        help="Runs in test mode"
    )

    parser.add_argument(
        "-n", "--ntest",
        type=bool,
        default=False,
        help="Run the ntest on all models"
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
    custom = args.custom
    verify = args.verify
    ntest = args.ntest
    model = args.model
    time = args.time

    if run_all:
        collect_all_data(directory_name)
    elif preprocess:
        run_preprocess(directory_name)
    elif custom:
        run_custom(directory_name)
    elif verify:
        verify_instance(directory_name)
    elif ntest:
        run_ntest(directory_name)
    else:
        print("Solving all puzzles in file:", directory_name)

        if model == "duplicates":
            print("Running the duplicates model")
            solver = DuplicatesSolver("duplicates_solver", [])
        elif model == "path":
            print("Running the path model")
            solver = PathSolver("path_solver", [SandwichesConstraint()])
        else:
            print("Running the naive model")
            solver = NaiveSolver("naive_solver", [], BFSConnectedChecker(), MinHeuristic())

        root = os.path.dirname(directory_name)
        file = directory_name.split("/")[-1]

        if time:
            print("Running in the Benchmarking Run Environment")
            environment = BenchmarkRunEnvironment(solver, root)
        else:
            print("Running in the Test Run Environment")
            environment = TestRunEnvironment(solver)

        print("## This is a single file run environment, change it if need be")
        n, board, data = read_file(root, file)

        environment.run_puzzle(n, board, file, data={})

        # i = 0
        #
        # print("Directory name:", directory_name)
        #
        # for root, dirs, files in os.walk(directory_name):
        #     for file in files:
        #         if file.endswith(".singles"):
        #
        #             n, board, data = read_file(root, file)
        #
        #             cpu_time = environment.run_puzzle(n, board, file, data=data)
        #
        #             print(i, n, cpu_time, environment.solver.name)
        #             i += 1
        #     print(root)
