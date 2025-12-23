import gurobipy as gp
from gurobipy import GRB

from src.naive_solver.naive_constraints.naive_adjacent_constraint import naive_adjacent_constraint
from src.naive_solver.naive_constraints.naive_unique_constraint import naive_unique_constraint
from src.optimisation_rules.corner_check import corner_check
from src.optimisation_rules.corner_close import corner_close
from src.optimisation_rules.edge_pairs import edge_pairs
from src.optimisation_rules.least_whites import least_whites
from src.optimisation_rules.most_blacks import most_blacks
from src.optimisation_rules.pair_isolation import pair_isolation
from src.optimisation_rules.sandwiches import sandwiches
from src.optimised_naive_solver.helper_methods.add_illegal_solution import add_illegal_solution
from src.optimised_naive_solver.helper_methods.extract_solution import extract_solution
from src.optimised_naive_solver.helper_methods.path_checker import path_checker
from src.optimised_naive_solver.minimise_black_squares_objective import minimise_black_squares_objective
from src.optimised_naive_solver.maximise_black_squares_objective import maximise_black_squares_objective
from src.optimised_naive_solver.optimised_naive_constraints.optimised_naive_adjacent_constraint import optimised_naive_adjacent_constraint
from src.optimised_naive_solver.optimised_naive_constraints.optimised_naive_unique_constraint import optimised_naive_unique_constraint
from src.optimised_naive_solver.helper_methods.find_duplicates import find_duplicates


def optimised_naive_solver(n, board):

    # Create a new model
    m = gp.Model("Hitori optimised naive")

    # Silence model, set memory limit to 8 GB and threads to 1, set seed to 32
    m.params.OutputFlag = 0
    m.params.MemLimit = 8
    m.params.Threads = 1
    m.params.Seed = 32

    is_black = list()

    for i in range(n):
        new_list = list()
        for j in range(n):
            new_list.append(m.addVar(vtype=GRB.BINARY, name=f'is_black {i}_{j}'))
        is_black.append(new_list)
    m.update()

    # Add optimisations
    # corner_close(is_black, m)
    # corner_check(board, is_black, [], n, m)
    # sandwiches(board, is_black, [], n, m)
    # edge_pairs(board, is_black, [], n, m, has_duplicates=False)
    # most_blacks(is_black, [], n, m, has_duplicates=False)
    # least_whites(is_black, [], n, m, has_duplicates=False)
    # pair_isolation(board, is_black, n, m)

    # Adjacency constraint
    naive_adjacent_constraint(n, is_black, m)

    # Unique constraint
    naive_unique_constraint(n, is_black, board, m)

    # Heuristic: Minimise the number of black squares
    # minimise_black_squares_objective(n, is_black, m)
    maximise_black_squares_objective(n, is_black, m)

    # Optimise the model
    try:
        m.optimize()
    except GRB.ERROR_OUT_OF_MEMORY:
        print("Out of Memory")

    # Extract values
    white, black, grid = extract_solution(n, m, is_black)
    iteration = 0

    while not path_checker(n, grid):
    # while not graph_path_checker_cycles(n, grid):
    # while not graph_path_checker_connected_components(n, grid):
        add_illegal_solution(white, black, m, iteration)
        m.optimize()

        white, black, grid = extract_solution(n, m, is_black)
        iteration += 1

    return m, is_black
