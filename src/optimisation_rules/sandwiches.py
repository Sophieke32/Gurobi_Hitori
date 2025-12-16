from itertools import islice

# This does both Sandwich Pair (SP) and Sandwich Triple (ST).
# It looks for a set of tiles in the form of
#
#                               x
#        x y x      OR          y
#                               x
#
# When it finds such a set of tiles it sets y to 0.
# if y == x then it also immediately sets the x-tiles to 1
def sandwiches(board, is_black, duplicates, n, m, has_duplicates=False):

    index_iter = iter(range(n-2))

    for j in range(n):
        for i in index_iter:
            if board[i][j] == board[i+2][j]:
                if board[i][j] == board[i+1][j]:

                    m.addConstr(is_black[i][j] == 1)
                    if type(is_black[i + 1][j]) != int: m.addConstr(is_black[i + 1][j] == 0)
                    m.addConstr(is_black[i + 2][j] == 1)

                    if has_duplicates:
                        # Update duplicates - Tiles that are covered do not have to be considered
                        # in other constraints
                        duplicates[i][j] = 0
                        duplicates[i + 2][j] = 0
                else:
                    if type(is_black[i + 1][j]) != int: m.addConstr(is_black[i + 1][j] == 0)

                # Skip the next two squares
                next(islice(index_iter, 1, 2), 0)

    index_iter = iter(range(n - 2))

    for j in index_iter:
        for i in range(n):
            if board[i][j] == board[i][j + 2]:
                if board[i][j] == board[i][j + 1]:

                    m.addConstr(is_black[i][j] == 1)
                    if type(is_black[i][j + 1]) != int: m.addConstr(is_black[i][j + 1] == 0)
                    m.addConstr(is_black[i][j + 2] == 1)

                    if has_duplicates:
                        # Update duplicates - Tiles that are covered do not have to be considered
                        # in other constraints
                        duplicates[i][j] = 0
                        duplicates[i][j + 2] = 0
                else:
                    if type(is_black[i][j + 1]) != int: m.addConstr(is_black[i][j + 1] == 0)

                # Skip the next two squares
                next(islice(index_iter, 1, 2), 0)


