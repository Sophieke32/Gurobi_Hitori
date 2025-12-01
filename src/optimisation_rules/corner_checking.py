# These methods check for a corner of the form
#
#               x y       or      x x
#               x y               y y
#
# and if there is, automatically assigns (0,0) and (1,1) to black and the
# other two to white
def corner_checking(board, is_black, duplicates, n, m):
    if n < 2: return
    check_corner(board, is_black, duplicates, m, 0, 0)
    if n > 2:
        check_corner(board, is_black, duplicates, m, n-2, 0)
        check_corner(board, is_black, duplicates, m, 0, n-2)
        check_corner(board, is_black, duplicates, m, n-2, n-2)


def check_corner(board, is_black, duplicates, m, i, j):
    if (board[i][j] == board[i + 1][j] and board[i][j + 1] == board[i + 1][j + 1]
            or board[i][j] == board[i][j + 1] and board[i + 1][j] == board[i + 1][j + 1]):
        m.addConstrs(is_black[k][k] == 1 for k in range(2))
        m.addConstr(is_black[i][j + 1] == 0)
        m.addConstr(is_black[i + 1][j] == 0)

        # Update duplicates
        duplicates[i][j] = 0
        duplicates[i + 1][j + 1] = 0