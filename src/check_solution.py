import numpy as np
import pandas as pd


def check_solution(board, solution, n):
    grid = []

    for i in range(n):
        row = []
        for j in range(n):
            if solution[i][j] == 1:
                row.append(str(board[i][j]) + "B")
            else:
                row.append(str(board[i][j]))
        grid.append(row)

    grid = np.array(grid)

    # No two black squares next to one another
    for i in range(n - 1):
        if "B" in grid[i][n - 1]:
            if "B" in grid[i + 1][n - 1]: return False

        for j in range(n - 1):
            if "B" in grid[n - 1][j]:
                if "B" in grid[n - 1][j + 1]: return False

            if "B" in grid[i][j]:
                if "B" in grid[i + 1][j]: return False
                if "B" in grid[i][j + 1]: return False


    # Check all unique
    for i in range(n):
        if len(grid[i][~np.char.endswith(grid[i], "B")]) != len(pd.unique(grid[i][~np.char.endswith(grid[i], "B")])):
            return False

        if len(grid[:, i][~np.char.endswith(grid[:, i], "B")]) != len(
                pd.unique(grid[:, i][~np.char.endswith(grid[:, i], "B")])):
            return False


    # Simple BFS tile explorer to find size of connected white squares
    i, j = 0, 0
    if "B" in grid[i][j]: i = 1

    path_length = 0
    queue = []
    visited = set()
    queue.append((i, j))

    while len(queue) > 0:
        cur = queue.pop(0)
        visited.add(cur)
        path_length += 1

        # Add neighbours to the queue
        if cur[0] + 1 < n and (cur[0] + 1, cur[1]) not in visited and (cur[0] + 1, cur[1]) not in queue:
            if "B" not in grid[cur[0] + 1][cur[1]]: queue.append((cur[0] + 1, cur[1]))
        if cur[0] - 1 >= 0 and (cur[0] - 1, cur[1]) not in visited and (cur[0] - 1, cur[1]) not in queue:
            if "B" not in grid[cur[0] - 1][cur[1]]: queue.append((cur[0] - 1, cur[1]))
        if cur[1] + 1 < n and (cur[0], cur[1] + 1) not in visited and (cur[0], cur[1] + 1) not in queue:
            if "B" not in grid[cur[0]][cur[1] + 1]: queue.append((cur[0], cur[1] + 1))
        if cur[1] - 1 >= 0 and (cur[0], cur[1] - 1) not in visited and (cur[0], cur[1] - 1) not in queue:
            if "B" not in grid[cur[0]][cur[1] - 1]: queue.append((cur[0], cur[1] - 1))

    # Get the number of black squares, so we know how long the path should be
    number_of_black_squares = 0
    for i in range(n):
        for j in range(n):
            if "B" in grid[i][j]: number_of_black_squares += 1


    if path_length != n * n - number_of_black_squares: return False

    return True
