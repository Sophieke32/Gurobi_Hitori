import gurobipy as gp
from gurobipy import GRB

from src.duplicates_solver.duplicates_constraints.duplicates_adjacent_constraint import duplicates_adjacent_constraint
from src.duplicates_solver.duplicates_constraints.duplicates_unique_constraint import duplicates_unique_constraint
from src.duplicates_solver.helper_methods.find_duplicates import find_duplicates
from src.duplicates_solver.helper_methods.create_duplicates_graph import create_graph
from src.duplicates_solver.duplicates_constraints.duplicates_path_constraint import duplicates_path_constraint
from src.optimisation_rules.corner_check import corner_check
from src.optimisation_rules.corner_close import corner_close
from src.optimisation_rules.edge_pairs import edge_pairs
from src.optimisation_rules.least_whites import least_whites
from src.optimisation_rules.most_blacks import most_blacks
from src.optimisation_rules.pair_isolation import pair_isolation
from src.optimisation_rules.sandwiches import sandwiches


def duplicates_solver(n, board):
    # Create the duplicates array
    duplicates = find_duplicates(n, board)

    # Create a new model
    m = gp.Model("Hitori_Solver_Duplicates")

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
    # corner_close(is_black, m)
    # corner_check(board, is_black, duplicates, n, m)
    # sandwiches(board, is_black, duplicates, n, m)
    # edge_pairs(board, is_black, duplicates, n, m, has_duplicates=True)
    # most_blacks(is_black, duplicates, n, m, has_duplicates=True)
    # least_whites(is_black, duplicates, n, m, has_duplicates=True)
    # pair_isolation(board, is_black, n, m)

    # Adjacency constraint
    duplicates_adjacent_constraint(n, is_black, m, duplicates)

    # Unique constraint
    duplicates_unique_constraint(n, is_black, m, duplicates)

    # Path constraint
    g = create_graph(n, duplicates)
    # number_of_cycles = duplicates_path_constraint(is_black, m, g)
    duplicates_path_constraint(is_black, m, g)

    # Optimise the model
    try:
        m.optimize()
    except GRB.ERROR_OUT_OF_MEMORY: print("Out of Memory")

    return m, is_black