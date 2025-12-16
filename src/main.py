import time
import os
import signal
import numpy as np
from gurobipy import GRB

from src.duplicates_solver.duplicates_solver import duplicates_solver
from src.naive_solver.naive_solver import naive_solver
from src.optimised_naive_solver.optimised_naive_solver import optimised_naive_solver
from src.path_solver.path_solver import path_solver
from src.pretty_print import pretty_print
from src.solution_checker import run_solution_checker
from src.write_results import get_results

def read_file(root, file):
    with open(os.path.join(root, file), "r") as f:
        line = f.readline()
        while type(int(line)) != int: continue
        n = int(line)

        board = np.zeros((n,n), dtype=int)

        f.readline()

        for i in range(n):
            board[i] = [int(number) for number in f.readline().split()]

        # Skip to the relevant lines
        f.readline()
        f.readline()
        f.readline()

        # print(f.readline().replace("# Computed in ", "").replace(" nanoseconds", ""))
        number_of_covered_tiles = f.readline().replace("# Number of covered squares: ", "").replace("\n", "")
        number_of_cycles = f.readline().replace("# Number of cycles: ", "").replace("\n", "")

        return n, board, number_of_covered_tiles, number_of_cycles

def write_to_file(m, is_black, n, board, cpu_time, root, file):
    with open(os.path.join(root + "_solutions", file + "sol"), "w") as f:
        f.write(get_results(m, is_black, n, board))
        f.write("\n")

        with open(os.path.join(root, file), "r") as source:
            for line in source:
                if len(line) > 0 and line[0] != "@" and line[0] != "#":
                    continue
                else:
                    f.write(line)

        f.write("\n# Computed in " + str(cpu_time) + " seconds")


def write_infeasible(cpu_time, root, file):
    with open(os.path.join(root + "_solutions", file + "sol"), "w") as file:
        file.write("# Model Infeasible in " + str(cpu_time) + " seconds")

def main(root, file, model, experiment):
    n, board, number_of_covered_tiles, number_of_cycles = read_file(root, file)

    time_out = 10 # Number of seconds before it times out

    # Handle timeouts
    signal.signal(signal.SIGALRM, handle_timeout)

    try:
        if model == "duplicates":
            signal.alarm(time_out)
            start = time.process_time_ns()
            m, is_black = duplicates_solver(n, board)
            end = time.process_time_ns()
            signal.alarm(0)
        elif model == "path":
            signal.alarm(time_out)
            start = time.process_time_ns()
            m, is_black = path_solver(n, board)
            end = time.process_time_ns()
            signal.alarm(0)
        elif model == "optimised_naive":
            signal.alarm(time_out)
            start = time.process_time_ns()
            m, is_black = optimised_naive_solver(n, board)
            end = time.process_time_ns()
            signal.alarm(0)
        else:
            signal.alarm(time_out)
            start = time.process_time_ns()
            m, is_black = naive_solver(n, board)
            end = time.process_time_ns()
            signal.alarm(0)

    except TimeoutError as exc:
        print("Oopsie")
        cpu_time = 2 * time_out * 1000000000
        if experiment:
            return n, -1, -1, cpu_time, False
        else:
            return n, cpu_time, False


    cpu_time = (end - start) /1000000000

    if experiment:
        m.dispose()
        return n, number_of_cycles, number_of_covered_tiles, cpu_time, True

    # If we are not running an experiment, perform more checks write solutions
    else:
        if m.status == GRB.INFEASIBLE:
            print(root + "/" + file, "was found to be infeasible")
            write_infeasible(cpu_time, root, file)
            return n, time, "INVALID"

        write_to_file(m, is_black, n, board, cpu_time, root, file)

        valid = run_solution_checker(root, file)
        if not valid:
            # If incorrect solution, print the solution for debugging
            print("\n###### Incorrect Solution! ######\n")
            print(root + "/" + file + "\n")
            pretty_print(m, is_black, n, board)
            print("\n#################################\n")

            os.remove(root + "_solutions/" + file + "sol")

        m.dispose()

        return n, cpu_time, valid


def handle_timeout(sig, frame):
    raise TimeoutError('took too long')
