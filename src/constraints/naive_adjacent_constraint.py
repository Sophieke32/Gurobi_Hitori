def naive_adjacent_constraint(n, is_black, m):
    m.addConstrs(is_black[i][j] + is_black[i + 1][j] <= 1
                 for i in range(n - 1)
                 for j in range(n)
                )

    m.addConstrs(is_black[i][j] + is_black[i][j + 1] <= 1
                 for i in range(n)
                 for j in range(n - 1)
                 )

    m.update()