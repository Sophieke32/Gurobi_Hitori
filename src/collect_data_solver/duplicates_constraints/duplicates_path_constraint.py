import networkx as nx
import gurobipy as gp

# Finds every cycle in the duplicates graph
# Constrains the model to break every cycle in at least one spot
# This ensures there is always a path between all white squares
def duplicates_path_constraint(is_black, m, g):
    # number_of_cycles = 0
    for value in nx.simple_cycles(g):
        # number_of_cycles += 1

        expr = gp.LinExpr()
        length = -1

        for c in value:
            if c != 'BORDER':
                expr.add(is_black[c[0]][c[1]])
                length += 1

        m.addConstr(expr <= length)

    m.update()

    # return number_of_cycles
