from pyscipopt import quicksum

# Takes the current solution and makes it illegal
#
# Does so by creating a binary decision variable v
# if v = 0, at least one of the current black squares must be made white
# if v = 1, at least one additional square must be made black
def scipopt_add_illegal_solution(uncovered, covered, m, iteration, is_covered, n):
    m.freeTransform()

    print("Covered tiles:", covered)

    covered_tiles_expression = 0
    for c in covered:
        covered_tiles_expression += c

    print(covered_tiles_expression)

    print()
    print()
    print()

    print("Uncovered tiles:", uncovered)
    uncovered_tiles_expression = 0
    print(uncovered_tiles_expression)
    for i in range(n):
        for j in range(n):
            if not m.getVal(is_covered[i][j]):
                uncovered_tiles_expression += is_covered[i][j]
                print(uncovered_tiles_expression)


    # uncovered_tiles_expression = 0
    # for u in uncovered:
    #     uncovered_tiles_expression += u
    #
    # print(uncovered_tiles_expression)



    #
    # covered_tiles_expression += covered[0]
    # print(covered_tiles_expression)


    #
    # covered_tiles_expression = 0
    # for c in covered: covered_tiles_expression += c

    v0 = m.addVar(vtype='BINARY', name=f'illegal solution {iteration} decision variable')



    # uncovered_tiles_expression = quicksum(u for u in uncovered)
    # print("Quicksum", uncovered_tiles_expression)

    covered_tiles_expression = quicksum(c for c in covered)
    # print(covered_tiles_expression)

    m.addCons(uncovered_tiles_expression >= 1, name="different_uncovered_tiles")
    # m.addCons(uncovered_tiles_expression >= 1 - (v0 * 10000), name="different_uncovered_tiles")
    # m.addCons(covered_tiles_expression <= len(covered) - 1 + ((1 - v0) * 10000), name="different_covered_tiles")
