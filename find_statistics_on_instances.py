import time
import argparse
import os
import numpy as np
from gurobipy import GRB

from src.collect_data_solver.duplicates_solver import duplicates_solver

def read_file(root, file):
    with open(os.path.join(root, file), "r") as f:
        line = f.readline()
        while type(int(line)) != int: continue
        n = int(line)

        board = np.zeros((n,n), dtype=int)

        f.readline()

        for i in range(n):
            board[i] = [int(number) for number in f.readline().split()]

        f.close()

        return n, board

def write_to_file(cpu_time, number_of_covered_squares, number_of_cycles, root, file):
    with open(os.path.join(root, file), "a") as f:
        f.write("\n# Computed in " + str(cpu_time) + " nanoseconds")
        f.write("\n# Number of covered squares: " + str(number_of_covered_squares))
        f.write("\n# Number of cycles: " + str(number_of_cycles))


def find_statistics_on_instance(root, file):
    n, board = read_file(root, file)

    start = time.process_time_ns()
    m, is_black, number_of_cycles = duplicates_solver(n, board)
    end = time.process_time_ns()

    cpu_time = end - start

    if m.status == GRB.INFEASIBLE:
        print(root + "/" + file, "was found to be infeasible")
        m.dispose()
        return

    number_of_covered_squares = 0

    for i in range(n):
        for j in range(n):
            if type(is_black[i][j]) != int and m.getAttr('X', [is_black[i][j]])[0]:
                number_of_covered_squares += 1

    write_to_file(cpu_time, number_of_covered_squares, number_of_cycles, root, file)

    m.dispose()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find the number of black squares and cycles in Hitori puzzles")

    parser.add_argument(
        "-d", "--dirname",
        type=str,
        required=True,
        help="Directory in which all .singles files will be read. Will also read sub-directories."
    )

    args = parser.parse_args()
    directory_name = args.dirname

    print(directory_name)

    for root, dirs, files in os.walk(directory_name):
        for file in files:
            if file.endswith(".singles"):
                find_statistics_on_instance(root, file)
            print("Preprocessed file:", file)
