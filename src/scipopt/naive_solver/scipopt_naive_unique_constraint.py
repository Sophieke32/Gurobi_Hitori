def scipopt_naive_unique_constraint(n, is_covered, board, m):
    # For each row we make a map, from a value (the value on the board) to all the variables
    # on a square with that value. We sum all these variables, and that should not exceed 1
    for i in range(n):
        horizontal_map = {}
        for j in range(n):
            if board[i][j] in horizontal_map:
                horizontal_map[board[i][j]] += (1 - is_covered[i][j])
            else:
                horizontal_map[board[i][j]] = 1 - is_covered[i][j]

        for i in range(1, n + 1):
            if i in horizontal_map:
                m.addCons(horizontal_map[i] <= 1)

    # For each column we make a map, from a value (the value on the board) to all the variables
    # on a square with that value. We sum all these variables, and that should not exceed 1
    for j in range(n):
        vertical_map = {}
        for i in range(n):
            if board[i][j] in vertical_map:
                vertical_map[board[i][j]] += (1 - is_covered[i][j])
            else:
                vertical_map[board[i][j]] = 1 - is_covered[i][j]

        for i in range(1, n+1):
            if i in vertical_map:
                m.addCons(vertical_map[i] <= 1)
        # m.addConstrs(vertical_map[i] <= 1 for i in range(1, n + 1) if i in vertical_map)
