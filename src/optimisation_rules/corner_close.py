# These methods check for a board-corner of the form
#
#             x y       or      x x
#             x y               y y
#
# and if there is, automatically assigns (0,0) and (1,1) to covered and the
# other two to uncovered
def corner_close(board, is_black, duplicates, n, m, has_duplicates=False):
    if not has_duplicates or has_duplicates and duplicates[0][0] != 0 and duplicates[-1][0] != 0 and duplicates[0][-1] != 0 and duplicates[-1][-1] != 0:
    # if duplicates[0][0] != 0 and duplicates[-1][0] != 0 and duplicates[0][-1] != 0 and duplicates[-1][-1] != 0:
        check_corner(board, is_black, duplicates, m, 0, 0, has_duplicates=has_duplicates)
        check_corner(board, is_black, duplicates, m, n - 2, 0, off_angle=True, has_duplicates=has_duplicates)
        check_corner(board, is_black, duplicates, m, 0, n - 2, off_angle=True, has_duplicates=has_duplicates)
        check_corner(board, is_black, duplicates, m, n-2, n-2, has_duplicates=has_duplicates)

# Helper method that actually does all the work
def check_corner(board, is_black, duplicates, m, i, j, off_angle=False, has_duplicates=False):
    if (board[i][j] == board[i + 1][j] and board[i][j + 1] == board[i + 1][j + 1]
            or board[i][j] == board[i][j + 1] and board[i + 1][j] == board[i + 1][j + 1]):

        print("DEBUG CORNER AAAAAAAAAAAAAAAAAAAAAAAAAAA")
        # We are on the top right or bottom left corner
        if off_angle:
            m.addConstr(is_black[i][j + 1] == 1)
            m.addConstr(is_black[i + 1][j] == 1)
            m.addConstr(is_black[i][j] == 0)
            m.addConstr(is_black[i + 1][j + 1] == 0)

            if has_duplicates:
                # Update duplicates - Tiles that are covered do not have to be considered
                # in other constraints
                duplicates[i][j + 1] = 0
                duplicates[i + 1][j] = 0
        else:
            m.addConstrs(is_black[k][k] == 1 for k in range(2))
            m.addConstr(is_black[i][j + 1] == 0)
            m.addConstr(is_black[i + 1][j] == 0)

            if has_duplicates:
                # Update duplicates - Tiles that are covered do not have to be considered
                # in other constraints
                duplicates[i][j] = 0
                duplicates[i + 1][j + 1] = 0