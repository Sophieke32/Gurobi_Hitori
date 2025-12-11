import gurobipy as gp
from gurobipy import GRB

from src.naive_solver.naive_constraints.naive_adjacent_constraint import naive_adjacent_constraint
from src.naive_solver.naive_constraints.naive_unique_constraint import naive_unique_constraint
from src.path_solver.path_constraints.path_constraint import path_path_constraint


# THIS SOLVER IS BROKEN AND SHOULD NOT BE USED
#
# It uses an experimental path_constraint algorithm that has not passed the testing phase
# Use of this solver may result in a correct solution, in which case you were lucky
# Don't actually use this to solve puzzles

def path_solver(n, board):
    # Create a new model
    m = gp.Model("Hitori")

    # Silence model, set memory limit to 8 GB and threads to 1
    m.params.OutputFlag = 0
    m.params.MemLimit = 8
    m.params.Thread = 1

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

    # Path constraint
    path_path_constraint(n, is_black, board, m)

    # Optimise the model
    try:
        m.optimize()
    except GRB.ERROR_OUT_OF_MEMORY:
        print("Out of Memory")

    return m, is_black
