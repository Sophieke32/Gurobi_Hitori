import gurobipy as gp
from gurobipy import GRB

from src.constraints.duplicates_connected_constraint import duplicates_connected_constraint
from src.constraints.duplicates_unique_constraint import duplicates_unique_constraint
from src.constraints.duplicates_path_constraint import duplicates_path_constraint

from src.constraints.redundant_constraints.redundant_constraint import RedundantConstraint
from src.solvers.naive_solver.helper_methods.extract_solution import extract_solution
from src.solvers.preprocessing_solver.helper_methods.create_duplicates_graph import create_graph
from src.solvers.preprocessing_solver.helper_methods.find_duplicates import find_duplicates
from src.solvers.solver import Solver


class PreprocessingSolver(Solver):
    name = ""
    redundant_constraints: list[RedundantConstraint] = []

    def __init__(self, name, redundant_constraints):
        self.name = name
        self.redundant_constraints = redundant_constraints

    def solve(self, n, board):
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
        is_covered = list()

        for i in range(n):
            new_list = list()
            for j in range(n):
                if duplicates[i][j] == 0:
                    new_list.append(0)
                else:
                    new_list.append(m.addVar(vtype=GRB.BINARY, name=f'is_covered {i}_{j}'))
            is_covered.append(new_list)
        m.update()

        # Adjacency constraint
        duplicates_connected_constraint(n, is_covered, m, duplicates)

        # Unique constraint
        duplicates_unique_constraint(n, is_covered, m, duplicates)

        # Path constraint
        g = create_graph(n, duplicates)
        number_of_cycles = duplicates_path_constraint(is_covered, m, g)

        # Optimise the model
        try:
            m.optimize()
        except GRB.ERROR_OUT_OF_MEMORY: print("Out of Memory")

        white, black, grid = extract_solution(n, m, is_covered)

        number_of_duplicates = 0
        for i in range(n):
            for j in range(n):
                if duplicates[i][j] != 0: number_of_duplicates += 1

        return number_of_cycles, len(black), number_of_duplicates
