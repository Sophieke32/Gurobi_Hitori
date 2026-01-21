def scipopt_naive_adjacent_constraint(n, is_covered, m):
    for i in range(n-1):
        for j in range(n):
            m.addCons(is_covered[i][j] + is_covered[i + 1][j] <= 1)

    for i in range(n):
        for j in range(n-1):
            m.addCons(is_covered[i][j] + is_covered[i][j + 1] <= 1)
