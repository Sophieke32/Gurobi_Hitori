# These methods check for a board-corner of the form
#
#             x y       or      x x
#             x y               y y
#
# and if there is, automatically assigns (0,0) and (1,1) to covered and the
# other two to uncovered
def corner_check(board, is_black, duplicates, n, m, has_duplicates=False):
    if not has_duplicates or has_duplicates and duplicates[0][0] != 0 and duplicates[-1][0] != 0 and duplicates[0][-1] != 0 and duplicates[-1][-1] != 0:
        top_left_corner(board, is_black, duplicates, m, has_duplicates=has_duplicates)
        top_right_corner(board, is_black, duplicates, m, has_duplicates=has_duplicates)
        bottom_left_corner(board, is_black, duplicates, m, has_duplicates=has_duplicates)
        bottom_right_corner(board, is_black, duplicates, m, has_duplicates=has_duplicates)


def top_left_corner(board, is_black, duplicates, m, has_duplicates=False):
    if (board[0][0] == board[1][0] and board[0][1] == board[1][1]
            or board[0][0] == board[0][1] and board[1][0] == board[1][1]):
        m.addConstrs(is_black[k][k] == 1 for k in range(2))
        m.addConstr(is_black[0][1] == 0)
        m.addConstr(is_black[1][0] == 0)

        m.addConstr(is_black[0][2] == 0)
        m.addConstr(is_black[2][0] == 0)

        m.addConstr(is_black[2][1] == 0)
        m.addConstr(is_black[1][2] == 0)

        if has_duplicates:
            # Update duplicates - Tiles that are covered do not have to be considered
            # in other constraints
            duplicates[0][0] = 0
            duplicates[1][1] = 0

def top_right_corner(board, is_black, duplicates, m, has_duplicates=False):
    if (board[-2][0] == board[-1][0] and board[-1][1] == board[-2][1]
            or board[-1][0] == board[-1][1] and board[-2][0] == board[-2][1]):
        m.addConstr(is_black[-1][0] == 1)
        m.addConstr(is_black[-2][1] == 1)
        m.addConstr(is_black[-2][0] == 0)
        m.addConstr(is_black[-1][1] == 0)

        m.addConstr(is_black[-3][0] == 0)
        m.addConstr(is_black[-1][2] == 0)

        m.addConstr(is_black[-2][2] == 0)
        m.addConstr(is_black[-3][1] == 0)

        if has_duplicates:
            # Update duplicates - Tiles that are covered do not have to be considered
            # in other constraints
            duplicates[-1][0] = 0
            duplicates[-2][1] = 0

def bottom_left_corner(board, is_black, duplicates, m, has_duplicates=False):
    if (board[0][-1] == board[1][-1] and board[0][-2] == board[1][-2]
            or board[0][-1] == board[0][-2] and board[1][-1] == board[1][-2]):
        m.addConstr(is_black[0][-1] == 1)
        m.addConstr(is_black[1][-2] == 1)
        m.addConstr(is_black[0][-2] == 0)
        m.addConstr(is_black[1][-1] == 0)

        m.addConstr(is_black[0][-3] == 0)
        m.addConstr(is_black[2][-1] == 0)

        m.addConstr(is_black[1][-3] == 0)
        m.addConstr(is_black[2][-2] == 0)


        if has_duplicates:
            # Update duplicates - Tiles that are covered do not have to be considered
            # in other constraints
            duplicates[0][-1] = 0
            duplicates[1][-2] = 0

def bottom_right_corner(board, is_black, duplicates, m, has_duplicates=False):
    if (board[-1][-1] == board[-2][-1] and board[-1][-2] == board[-2][-2]
            or board[-1][-1] == board[-1][-2] and board[-2][-1] == board[-2][-2]):
        m.addConstr(is_black[-1][-1] == 1)
        m.addConstr(is_black[-2][-2] == 1)
        m.addConstr(is_black[-1][-2] == 0)
        m.addConstr(is_black[-2][-1] == 0)

        m.addConstr(is_black[-1][-3] == 0)
        m.addConstr(is_black[-3][-1] == 0)

        m.addConstr(is_black[-3][-2] == 0)
        m.addConstr(is_black[-2][-3] == 0)

        if has_duplicates:
            # Update duplicates - Tiles that are covered do not have to be considered
            # in other constraints
            duplicates[0][0] = 0
            duplicates[1][1] = 0
