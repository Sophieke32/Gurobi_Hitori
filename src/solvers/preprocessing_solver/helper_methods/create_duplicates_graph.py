import networkx as nx
import matplotlib.pyplot as plt

# Creates a graph used in ensuring the path constraint
#
# Each duplicate value is a node, and a general BORDER node is made as well
# Duplicate values on the edge of the board are connected to BORDER
# Two duplicate values that are diagonally adjacent are connected with an edge
def create_graph(n, duplicates):
    g = nx.Graph()
    g.add_node("BORDER")
    for i in range(n):
        for j in range(n):
            g.add_node((i, j))

    for i in range(n):
        if duplicates[i][0] > 0:
            g.add_edge("BORDER", (i, 0))
        if duplicates[i][n-1] > 0:
            g.add_edge("BORDER", (i, n-1))

    for i in range(1, n-1):
        if duplicates[0][i] > 0:
            g.add_edge("BORDER", (0, i))
        if duplicates[n-1][i] > 0:
            g.add_edge("BORDER", (n-1, i))

    for i in range(1, n-1):
        for j in range(1, n-1):
            if duplicates[i][j] > 0:
                if duplicates[i-1][j-1] > 0:
                    g.add_edge((i, j), (i-1, j-1))
                if duplicates[i+1][j-1] > 0:
                    g.add_edge((i, j), (i + 1, j - 1))
                if duplicates[i-1][j+1] > 0:
                    g.add_edge((i, j), (i - 1, j + 1))
                if duplicates[i+1][j+1] > 0:
                    g.add_edge((i, j), (i + 1, j + 1))

    # if the two squares next to a corner-square are duplicates, connect them
    if duplicates[0][1] > 0 and duplicates[1][0] > 0:
        g.add_edge((0, 1), (1, 0))

    if duplicates[0][n-2] > 0 and duplicates[1][n-1] > 0:
        g.add_edge((0, n-2), (1, n-1))

    if duplicates[n-2][0] > 0 and duplicates[n-1][1] > 0:
        g.add_edge((n-2, 0), (n-1, 1))

    if duplicates[n-2][n-1] > 0 and duplicates[n-1][n-2] > 0:
        g.add_edge((n-2, n-1), (n-1, n-2))

    return g

# Prints the graph using matplotlib
def print_graph(g):
    # write edgelist to grid.edgelist
    nx.write_edgelist(g, path="grid.edgelist", delimiter=":")
    # read edgelist from grid.edgelist
    h = nx.read_edgelist(path="grid.edgelist", delimiter=":")

    pos = nx.spring_layout(h, seed=200)
    nx.draw(h, pos)
    plt.show()
