import networkx as nx

# grid is a 2d array of zeroes and ones, where a 1 represents a covered tile

# Converts the grid to a graph, and checks if there are any cycles from covered tiles and
# possibly the edge of the board
def graph_path_checker_cycles(n, grid):
    g = nx.Graph()
    g.add_node("BORDER")

    # Add all 1's in grid to the graph
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1: g.add_node((i, j))

    for i in range(n):
        if grid[i][0] == 1:
            g.add_edge("BORDER", (i, 0))
        if grid[i][-1] == 1:
            g.add_edge("BORDER", (i, n-1))

    for i in range(1, n-1):
        if grid[0][i] == 1:
            g.add_edge("BORDER", (0, i))
        if grid[-1][i] == 1:
            g.add_edge("BORDER", (n-1, i))

    for i in range(1, n-1):
        for j in range(1, n-1):
            if grid[i][j] == 1:
                if grid[i-1][j-1] == 1:
                    g.add_edge((i, j), (i-1, j-1))
                if grid[i+1][j-1] == 1:
                    g.add_edge((i, j), (i + 1, j - 1))
                if grid[i-1][j+1] == 1:
                    g.add_edge((i, j), (i - 1, j + 1))
                if grid[i+1][j+1] == 1:
                    g.add_edge((i, j), (i + 1, j + 1))

    # if the two squares next to a corner-square are duplicates, connect them
    if grid[0][1] == 1 and grid[1][0] == 1:
        g.add_edge((0, 1), (1, 0))

    if grid[0][n-2] == 1 and grid[1][n-1] == 1:
        g.add_edge((0, n-2), (1, n-1))

    if grid[n-2][0] == 1 and grid[n-1][1] == 1:
        g.add_edge((n-2, 0), (n-1, 1))

    if grid[n-2][n-1] == 1 and grid[n-1][n-2] == 1:
        g.add_edge((n-2, n-1), (n-1, n-2))

    # If there is a cycle in this graph: connected constraint is not satisfied
    try:
        nx.find_cycle(g)
    except nx.NetworkXNoCycle:
        return True
    return False

def graph_path_checker_connected_components(n, grid):
    g = nx.Graph()

    # Add all uncovered tiles to the graph
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0: g.add_node((i, j))

    # Add all orthogonally connected uncovered tiles
    for i in range(n-1):
        for j in range(n):
            if grid[i][j] == 0 and grid[i + 1][j] == 0:
                g.add_edge((i, j), (i + 1, j))

    for i in range(n):
        for j in range(n-1):
            if grid[i][j] == 0 and grid[i][j + 1] == 0:
                g.add_edge((i, j), (i, j + 1))

    # If there is only one connected component, then we satisfy the connected constraint
    return nx.number_connected_components(g) == 1