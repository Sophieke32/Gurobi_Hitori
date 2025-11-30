# Method that prevents adjacent black squares
# Loops through the duplicates array. If two values next to one another are duplicates,
# we forbid them to both be black
def duplicates_adjacent_constraint(n, is_black, m, duplicates):
    m.addConstrs(is_black[i][j] + is_black[i + 1][j] <= 1
                 for i in range(n-1)
                 for j in range(n)
                 if duplicates[i][j] > 0 and duplicates[i + 1][j] > 0)

    m.addConstrs(is_black[i][j] + is_black[i][j + 1] <= 1
                 for i in range(n)
                 for j in range(n-1)
                 if duplicates[i][j] > 0 and duplicates[i][j + 1] > 0)

    m.update()
