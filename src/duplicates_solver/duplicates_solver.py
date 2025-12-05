import gurobipy as gp
from gurobipy import GRB

from src.duplicates_solver.duplicates_constraints.duplicates_adjacent_constraint import duplicates_adjacent_constraint
from src.duplicates_solver.duplicates_constraints.duplicates_unique_constraint import duplicates_unique_constraint
from src.duplicates_solver.helper_methods.find_duplicates import find_duplicates
from src.duplicates_solver.helper_methods.create_duplicates_graph import create_graph
from src.duplicates_solver.duplicates_constraints.duplicates_path_constraint import duplicates_path_constraint


def duplicates_solver(n, board):
    # Create the duplicates array
    duplicates = find_duplicates(n, board)

    # Create a new model
    m = gp.Model("Hitori_Solver_Duplicates")
    m.params.OutputFlag = 0
    m.params.MemLimit = 8

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
    number_of_cycles = duplicates_path_constraint(is_black, m, g)

    # Optimise the model
    try:
        m.optimize()
    except GRB.ERROR_OUT_OF_MEMORY: print("Out of Memory")
    finally: m.dispose()

    return m, is_black, number_of_cycles