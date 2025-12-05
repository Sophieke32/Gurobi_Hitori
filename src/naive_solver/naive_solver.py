import gurobipy as gp
from gurobipy import GRB

from src.naive_solver.helper_methods.add_illegal_solution import add_illegal_solution
from src.naive_solver.helper_methods.extract_solution import extract_solution
from src.naive_solver.helper_methods.path_checker import path_checker
from src.naive_solver.minimise_black_squares_objective import minimise_black_squares_objective
from src.naive_solver.naive_constraints.naive_adjacent_constraint import naive_adjacent_constraint
from src.naive_solver.naive_constraints.naive_unique_constraint import naive_unique_constraint


def naive_solver(n, board):
    # Create a new model
    m = gp.Model("Hitori")
    m.params.OutputFlag = 0
    m.params.MemLimit = 8

    is_black = list()

    for i in range(n):
        new_list = list()
        for j in range(n):
                new_list.append(m.addVar(vtype=GRB.BINARY, name=f'is_black {i}_{j}'))
        is_black.append(new_list)
    m.update()

    # Adjacency constraint
    naive_adjacent_constraint(n, is_black, m)

    # Unique constraint
    naive_unique_constraint(n, is_black, board, m)

    # Heuristic: Minimise the number of black squares
    minimise_black_squares_objective(n, is_black, m)

    # Optimise the model
    try:
        m.optimize()
    except GRB.ERROR_OUT_OF_MEMORY:
        print("Out of Memory")
    finally:
        m.dispose()

    # Extract values
    white, black, grid = extract_solution(n, m, is_black)
    iteration = 0

    while not path_checker(n, grid):
        add_illegal_solution(white, black, m, iteration)
        m.optimize()

        white, black, grid = extract_solution(n, m, is_black)
        iteration += 1

    return m, is_black
