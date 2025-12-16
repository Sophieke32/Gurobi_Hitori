import numpy as np

# Returns an array where all values that are unique in their role and column have been set to 0
# e.g.:
#  [2 2 1 3 3]
#  [4 1 4 5 3]
#  [1 1 3 2 2]
#  [5 3 4 1 2]
#  [4 2 2 4 4]
#
# Turns into
#  [2 2 0 3 3]
#  [4 1 4 0 3]
#  [1 1 0 2 2]
#  [0 0 4 0 2]
#  [4 2 2 4 4]
def find_duplicates(n, board):
    duplicates = np.zeros((n,n), dtype=int)

    for i in range(n):
        values, counts = np.unique(board[i], return_counts=True)
        for j in range(n):
            if counts[np.where(values == board[i][j])] > 1:
                duplicates[i][j] = board[i][j]


    for i in range(n):
        values, counts = np.unique(board[:, i], return_counts=True)
        for j in range(n):
            if counts[np.where(values == board[j][i])] > 1:
                duplicates[j][i] = board[j][i]

    return duplicates
