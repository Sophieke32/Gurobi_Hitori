import time
import numpy as np
from gurobipy import GRB

from src.duplicates_solver.duplicates_solver import duplicates_solver
from src.naive_solver.naive_solver import naive_solver
from src.pretty_print import pretty_print
from src.solution_checker import run_solution_checker
from src.write_results import get_results

def read_file(root, file):
    with open(root + "/" + file, "r") as f:
        line = f.readline()
        while type(int(line)) != int: continue
        n = int(line)

        board = np.zeros((n,n), dtype=int)

        f.readline()

        for i in range(n):
            board[i] = [int(number) for number in f.readline().split()]

        f.close()

        return n, board

def write_to_file(m, is_black, n, board, cpu_time, root, file):
    with open(root + "_solutions/" + file + "sol", "w") as f:
        f.write(get_results(m, is_black, n, board))
        f.write("\n")

        with open(root + "/" + file, "r") as source:
            for line in source:
                if len(line) > 0 and line[0] != "@" and line[0] != "#":
                    continue
                else:
                    f.write(line)

        f.write("\n# Computed in " + str(cpu_time) + " seconds")


def write_infeasible(cpu_time, root, file):
    with open(root + "_solutions/" + file + "sol", "w") as file:
        file.write("# Model Infeasible in " + str(cpu_time) + " seconds")

def main(root, file, model):
    n, board = read_file(root, file)

    m = None
    is_black = None

    start = time.process_time()
    if model == "duplicates":
        m, is_black = duplicates_solver(n, board)
    else:
        m, is_black = naive_solver(n, board)
    end = time.process_time()

    cpu_time = end - start

    if m.status == GRB.INFEASIBLE:
        print(root + "/" + file, "was found to be infeasible")
        write_infeasible(cpu_time, root, file)
        return n, time, "INVALID"

    if run_solution_checker(root, file):
        write_to_file(m, is_black, n, board, cpu_time, root, file)
    else:
        # If incorrect solution, print the solution for debugging
        print("###### Incorrect Solution! ######\n")
        print(root + "/" + file)
        pretty_print(m, is_black, n, board)
        print("\n#################################")

    return n, time, run_solution_checker(root, file)
