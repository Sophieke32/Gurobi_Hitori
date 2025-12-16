import gurobipy as gp
from gurobipy import GRB

from src.optimised_naive_solver.helper_methods.add_illegal_solution import add_illegal_solution
from src.optimised_naive_solver.helper_methods.extract_solution import extract_solution
from src.optimised_naive_solver.helper_methods.path_checker import path_checker
from src.optimised_naive_solver.minimise_black_squares_objective import minimise_black_squares_objective
from src.optimised_naive_solver.optimised_naive_constraints.optimised_naive_adjacent_constraint import optimised_naive_adjacent_constraint
from src.optimised_naive_solver.optimised_naive_constraints.optimised_naive_unique_constraint import optimised_naive_unique_constraint
from src.optimised_naive_solver.helper_methods.find_duplicates import find_duplicates


def optimised_naive_solver(n, board):
    # Create the duplicates array
    duplicates = find_duplicates(n, board)

    # Create a new model
    m = gp.Model("Hitori optimised naive")

    # Silence model, set memory limit to 8 GB and threads to 1
    m.params.OutputFlag = 0
    m.params.MemLimit = 8
    m.params.Threads = 1

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

    # Add optimisations
    # corner_close(board, is_black, duplicates, n, m)

    # Adjacency constraint
    optimised_naive_adjacent_constraint(n, is_black, m, duplicates)

    # Unique constraint
    optimised_naive_unique_constraint(n, is_black, m, duplicates)

    # Heuristic: Minimise the number of black squares
    minimise_black_squares_objective(n, is_black, m)

    # Optimise the model
    try:
        m.optimize()
    except GRB.ERROR_OUT_OF_MEMORY:
        print("Out of Memory")

    # Extract values
    white, black, grid = extract_solution(n, m, is_black)
    iteration = 0

    while not path_checker(n, grid):
        add_illegal_solution(white, black, m, iteration)
        m.optimize()

        white, black, grid = extract_solution(n, m, is_black)
        iteration += 1

    return m, is_black
