def duplicates_set_unique_values(n, is_black, m, duplicates):
    for i in range(n):
        for j in range(n):
            if duplicates[i][j] == 0:
                m.addConstr(is_black[i][j] == 0)
                print(i, j)