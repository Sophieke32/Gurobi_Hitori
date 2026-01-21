import numpy as np
from pyscipopt import Model

# Method to extract the solution of an optimisation
#
# Returns uncovered, an array of all variables in is_covered with value = 0
# Returns covered, an array of all variables in is_covered with value = 1
# Returns grid, an n x n grid where 0 means the corresponding tile is uncovered
#               and 1 means the corresponding tile is covered
def cylp_extract_solution(n, m, is_covered):
    uncovered = []
    covered = []
    grid = np.zeros((n, n))

    solution = m.getSolution()
    basis = m.getBasis()
    info = m.getInfo()
    model_status = m.getModelStatus()
    print("Solution = ", solution)
    print('basis = ', basis)
    print('Model status = ', m.modelStatusToString(model_status))
    print()
    print('Optimal objective = ', info.objective_function_value)
    print('Iteration count = ', info.simplex_iteration_count)
    print('Primal solution status = ', m.solutionStatusToString(info.primal_solution_status))
    print('Dual solution status = ', m.solutionStatusToString(info.dual_solution_status))
    print('Basis validity = ', m.basisValidityToString(info.basis_validity))

    for i in range(n):
        for j in range(n):
            if not m.getVal(is_covered[i][j]):
                # print("Adding var with value", m.getVal(is_covered[i][j]), "to uncovered")
                uncovered.append(is_covered[i][j])
                grid[i, j] = 0
            elif m.getVal(is_covered[i][j]):
                # print("Adding var with value", m.getVal(is_covered[i][j]), "to covered")
                covered.append(is_covered[i][j])
                grid[i, j] = 1

    return uncovered, covered, grid
