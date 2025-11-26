import sys
import pandas as pd

def check(file):
    stream = open(file, "r")

    lines = stream.read().splitlines()

    n = int(lines[0])

    if len(lines) < n + 2:
        print("file format wrong, expected more")
        exit(1)

    stream.close()

    # Make the grid
    grid = []
    for i in range(2, n + 2):
        line = lines[i]
        row = [x for x in line.split(" ", )]
        assert (len(row) == n)
        grid.append(row)

    # No two black squares next to one another
    for i in range(n -1):
        if "B" in grid[i][n-1]:
            if "B" in grid[i+1][n-1]: return False

        for j in range(n-1):
            if "B" in grid[n-1][j]:
                if "B" in grid[n-1][j+1]: return False

            if "B" in grid[i][j]:
                if "B" in grid[i+1][j]: return False
                if "B" in grid[i][j+1]: return False

    # Check all unique
    for i in range(n):
        if (len(list(filter(lambda s: "B" not in s, grid[i]))) !=
                len(pd.unique(list(filter(lambda s: "B" not in s, grid[i]))))):
            return False

        if (len(list(filter(lambda s: "B" not in s, list(row[i] for row in grid)))) !=
                len(pd.unique(list(filter(lambda s: "B" not in s, list(row[i] for row in grid)))))):
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
        if cur[0] -1 >= 0 and (cur[0] - 1, cur[1]) not in visited and (cur[0] - 1, cur[1]) not in queue:
            if "B" not in grid[cur[0] - 1][cur[1]]: queue.append((cur[0] - 1, cur[1]))
        if cur[1] + 1 < n and (cur[0], cur[1] + 1) not in visited and (cur[0], cur[1] + 1) not in queue:
            if "B" not in grid[cur[0]][cur[1] + 1]: queue.append((cur[0], cur[1] + 1))
        if cur[1] -1 >= 0 and (cur[0], cur[1] - 1) not in visited  and (cur[0], cur[1] - 1) not in queue:
            if "B" not in grid[cur[0]][cur[1] - 1]: queue.append((cur[0], cur[1] - 1))

    # Get the number of black squares, so we know how long the path should be
    number_of_black_squares = 0
    for i in range(n):
        for j in range(n):
            if "B" in grid[i][j]: number_of_black_squares += 1

    if path_length != n*n - number_of_black_squares: return False

    return True


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("usage ./main.py input.singlessol")
        exit(1)

    filename = sys.argv[1]
    print(check(filename))