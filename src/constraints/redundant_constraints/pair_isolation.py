from src.constraints.redundant_constraints.redundant_constraint import RedundantConstraint


class PairIsolationConstraint(RedundantConstraint):
    # Looks for a pattern like:
    #
    #   x x .+ x
    #
    # And then requires the single x to be covered (also works on columns)
    def apply(self, board, is_covered, duplicates, n, m, has_duplicates=False):
        for i in range(n):
            pairs = list()
            for j in range(n - 1):
                if board[i][j] == board[i][j + 1]:
                    pairs.append(board[i][j])
            for j in range(1, n - 1):
                if board[i][j - 1] != board[i][j] and board[i][j] != board[i][j + 1] and board[i][j] in pairs:
                    # print('got a pair isolation')
                    m.addConstr(is_covered[i][j] == 1)

        for j in range(n):
            pairs = list()
            for i in range(n - 1):
                if board[i][j] == board[i + 1][j]:
                    pairs.append(board[i][j])
            for i in range(1, n - 1):
                if board[i - 1][j] != board[i][j] and board[i][j] != board[i + 1][j] and board[i][j] in pairs:
                    # print('got a pair isolation')
                    m.addConstr(is_covered[i][j] == 1)
