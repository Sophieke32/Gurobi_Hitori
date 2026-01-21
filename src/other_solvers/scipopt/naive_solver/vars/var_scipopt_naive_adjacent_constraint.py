def var_scipopt_naive_adjacent_constraint(n, is_covered, m, that_one_var):
    for i in range(n-1):
        for j in range(n):
            if i == 0 and j == 0: m.addCons(that_one_var + is_covered[i + 1][j] <= 1)
            else: m.addCons(is_covered[i][j] + is_covered[i + 1][j] <= 1)

    for i in range(n):
        for j in range(n-1):
            if i == 0 and j == 0: m.addCons(that_one_var + is_covered[i][j + 1] <= 1)
            else: m.addCons(is_covered[i][j] + is_covered[i][j + 1] <= 1)
