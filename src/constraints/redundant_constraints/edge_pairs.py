from src.constraints.redundant_constraints.redundant_constraint import RedundantConstraint


class EdgePairsConstraint(RedundantConstraint):
    # This does n-edge pairs.
    # It looks for a set of tiles in the form of
    #
    #       __________
    #        a x x b
    #        c y y d
    #
    # for n rows, where n > 1.
    # When it finds such a set of tiles it sets the outer values (e.g. a and b in row 1)
    # of each row except the last to 0.
    def apply(self, board, is_covered, duplicates, n, m, has_duplicates=False):
        occurrences = 0

        # Top row of the board
        for j in range(n - 2, 1):
            if board[0][j - 1] != board[0][j] and board[0][j] == board[0][j + 1] and board[0][j + 1] != board[0][j + 2]:
                i = 1
                while board[i][j - 1] != board[i][j] and board[i][j] == board[i][j + 1] and board[i][j + 1] != board[i][
                    j + 2]:
                    # print("edge_pairs top side: i =", i)
                    if has_duplicates and type(duplicates[i - 1][j - 1]) != int or not has_duplicates:
                        # print("Went into effect left")
                        m.addConstr(is_covered[i - 1][j - 1] == 0)

                    if has_duplicates and type(duplicates[i - 1][j + 2]) != int or not has_duplicates:
                        # print("Went to in effect right")
                        m.addConstr(is_covered[i - 1][j + 2] == 0)

                    i = i + 1
                    occurrences += 1

        # Bottom row of the board
        for j in range(n - 2, 1):
            if board[-1][j - 1] != board[-1][j] and board[-1][j] == board[-1][j + 1] and board[-1][j + 1] != board[-1][
                j + 2]:
                i = -2
                while board[i][j - 1] != board[i][j] and board[i][j] == board[i][j + 1] and board[i][j + 1] != board[i][
                    j + 2]:
                    # print("edge_pairs bottom side: i =", i)
                    if has_duplicates and type(duplicates[i + 1][j - 1]) != int or not has_duplicates:
                        # print("Went into effect left")
                        m.addConstr(is_covered[i + 1][j - 1] == 0)

                    if has_duplicates and type(duplicates[i + 1][j + 2]) != int or not has_duplicates:
                        # print("Went to in effect right")
                        m.addConstr(is_covered[i + 1][j + 2] == 0)

                    i = i - 1
                    occurrences += 1

        # Left side of the board
        for i in range(n - 2, 1):
            if board[i - 1][0] != board[i][0] and board[i][0] == board[i + 1][0] and board[i + 1][0] == board[i + 2][0]:
                j = 1
                while board[i - 1][j] != board[i][j] and board[i][j] == board[i + 1][j] and board[i + 1][j] != \
                        board[i + 2][j]:
                    # print("edge_pairs left side: j =", j)
                    if has_duplicates and type(duplicates[i - 1][j - 1]) != int or not has_duplicates:
                        # print("Went into effect left")
                        m.addConstr(is_covered[i - 1][j - 1] == 0)

                    if has_duplicates and type(duplicates[i + 2][j - 1]) != int or not has_duplicates:
                        # print("Went to in effect right")
                        m.addConstr(is_covered[i + 2][j - 1] == 0)

                    j = j + 1
                    occurrences += 1

        # Right side of the board
        for i in range(n - 2, 1):
            if board[i - 1][-1] != board[i][-1] and board[i][-1] == board[i + 1][-1] and board[i + 1][-1] == \
                    board[i + 2][-1]:
                j = -2
                while board[i - 1][j] != board[i][j] and board[i][j] == board[i + 1][j] and board[i + 1][j] != \
                        board[i + 2][j]:
                    # print("edge_pairs left side: j =", j)
                    if has_duplicates and type(duplicates[i - 1][j + 1]) != int or not has_duplicates:
                        # print("Went into effect left")
                        m.addConstr(is_covered[i - 1][j + 1] == 0)

                    if has_duplicates and type(duplicates[i + 2][j + 1]) != int or not has_duplicates:
                        # print("Went to in effect right")
                        m.addConstr(is_covered[i + 2][j + 1] == 0)

                    j = j - 1
                    occurrences += 1

        return occurrences
