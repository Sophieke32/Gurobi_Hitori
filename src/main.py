import numpy as np
import gurobipy as gp
from gurobipy import GRB

from src.duplicates_constraints.duplicates_adjacent_constraint import duplicates_adjacent_constraint
from src.duplicates_constraints.duplicates_unique_constraint import duplicates_unique_constraint
from src.duplicates_constraints.find_duplicates import find_duplicates
from src.duplicates_constraints.create_duplicates_graph import create_graph
from src.duplicates_constraints.duplicates_path_constraint import duplicates_path_constraint
from src.pretty_print import pretty_print
from src.write_results import get_results

folder = "/8_instances"
instance_key = "123.singles"

def read_file():
    file = open("problem_instances/8_instances/123.singles", "r")
    line = file.readline()
    while type(int(line)) != int: continue
    n = int(line)

    board = np.zeros((n,n), dtype=int)

    file.readline()

    for i in range(n):
        board[i] = [int(number) for number in file.readline().split()]

    line = file.readline()

    while line:
        print(line.strip())
        line = file.readline()
    file.close()

    return n, board

def write_to_file(m, is_black, n, board):
    with open("problem_instances" + folder + "_solutions/" + instance_key + "sol", "w") as file:
        file.write(get_results(m, is_black, n, board))
        file.write("\n")

        with open("problem_instances" + folder + "/" + instance_key, "r") as source:
            for line in source:
                if len(line) > 0 and line[0] != "@" and line[0] != "#": continue
                else: file.write(line)


def main():
    n, board = read_file()

    # Create the duplicates array
    duplicates = find_duplicates(n, board)


    # Create a new model
    m = gp.Model("Hitori")

    # Make the variables. Only add variables for duplicate values.
    # Values on the Hitori board that are unique in their row and column will never
    # have to be blacked out.
    is_black = list()

    for i in range(n):
        new_list = list()
        for j in range(n):
            if duplicates[i][j] == 0:
                new_list.append(0)
            else:
                new_list.append(m.addVar(vtype=GRB.BINARY, name=f'is_black {i}_{j}'))
        is_black.append(new_list)
    m.update()

    # Adjacency constraint
    duplicates_adjacent_constraint(n, is_black, m, duplicates)

    # Unique constraint
    duplicates_unique_constraint(n, is_black, m, duplicates)

    # Path constraint
    g = create_graph(n, duplicates)
    duplicates_path_constraint(is_black, m, g)

    # Optimise the model
    m.optimize()

    if m.status == GRB.INFEASIBLE:
        print("Infeasible")
        exit()

    pretty_print(m, is_black, n, board)
    write_to_file(m, is_black, n, board)

    # run_solution_checker()

