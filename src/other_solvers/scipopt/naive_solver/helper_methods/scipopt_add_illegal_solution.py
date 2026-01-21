from pyscipopt import quicksum

# Takes the current solution and makes it illegal
#
# Does so by creating a binary decision variable v
# if v = 0, at least one of the current black squares must be made white
# if v = 1, at least one additional square must be made black
def scipopt_add_illegal_solution(uncovered, covered, m, iteration, that_one_var):
    m.freeTransform()

    # print("##################################### Uncovered tiles: #####################################\n\n", uncovered, "\n\n")
    uncovered_tiles_expression = 0
    # uncovered_tiles_expression += that_one_var
    # print(uncovered_tiles_expression)

    for i in range(len(uncovered)):
        uncovered_tiles_expression += uncovered[i]


    # print("##################################### Uncovered expr: #####################################\n\n", uncovered_tiles_expression, "\n\n")


    # print("Covered tiles:", covered)
    covered_tiles_expression = 0
    for c in covered:
        covered_tiles_expression += c
        # print(c)

    # print("##################################### Covered expr: #####################################\n\n", covered_tiles_expression, "\n\n")

    v0 = m.addVar(vtype='BINARY', name=f'illegal solution {iteration} decision variable')

    m.addCons(uncovered_tiles_expression >= 1 - (v0 * 10000), name="different_uncovered_tiles")
    m.addCons(covered_tiles_expression <= len(covered) - 1 + ((1 - v0) * 10000), name="different_covered_tiles")
