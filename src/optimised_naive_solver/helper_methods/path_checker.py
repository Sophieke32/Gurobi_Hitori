# grid is a 2d array of zeroes and ones, where a 1 represents a covered tile
def path_checker(n, grid):
    # Simple BFS tile explorer to find size of connected white squares
    i, j = 0, 0
    if grid[i][j] == 1: i = 1

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
            if grid[cur[0] + 1][cur[1]] == 0: queue.append((cur[0] + 1, cur[1]))
            # if "B" not in grid[cur[0] + 1][cur[1]]: queue.append((cur[0] + 1, cur[1]))
        if cur[0] -1 >= 0 and (cur[0] - 1, cur[1]) not in visited and (cur[0] - 1, cur[1]) not in queue:
            if grid[cur[0] - 1][cur[1]] == 0: queue.append((cur[0] - 1, cur[1]))
            # if "B" not in grid[cur[0] - 1][cur[1]]: queue.append((cur[0] - 1, cur[1]))
        if cur[1] + 1 < n and (cur[0], cur[1] + 1) not in visited and (cur[0], cur[1] + 1) not in queue:
            if grid[cur[0]][cur[1] + 1] == 0: queue.append((cur[0], cur[1] + 1))
            # if "B" not in grid[cur[0]][cur[1] + 1]: queue.append((cur[0], cur[1] + 1))
        if cur[1] -1 >= 0 and (cur[0], cur[1] - 1) not in visited  and (cur[0], cur[1] - 1) not in queue:
            if grid[cur[0]][cur[1] - 1] == 0: queue.append((cur[0], cur[1] - 1))
            # if "B" not in grid[cur[0]][cur[1] - 1]: queue.append((cur[0], cur[1] - 1))

    # Get the number of black squares, so we know how long the path should be
    number_of_black_squares = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1: number_of_black_squares += 1

    return n*n == path_length + number_of_black_squares
