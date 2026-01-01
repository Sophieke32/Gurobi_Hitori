# Method that prevents adjacent covered tiles
# Loops through the duplicates array. If two values next to one another are duplicates,
# we forbid them to both be covered
def duplicates_connected_constraint(n, is_covered, m, duplicates):
    m.addConstrs(is_covered[i][j] + is_covered[i + 1][j] <= 1
                 for i in range(n-1)
                 for j in range(n)
                 if duplicates[i][j] > 0 and duplicates[i + 1][j] > 0)

    m.addConstrs(is_covered[i][j] + is_covered[i][j + 1] <= 1
                 for i in range(n)
                 for j in range(n-1)
                 if duplicates[i][j] > 0 and duplicates[i][j + 1] > 0)

    m.update()
