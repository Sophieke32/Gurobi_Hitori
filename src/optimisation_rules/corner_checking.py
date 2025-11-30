
def corner_checking(board, is_black, duplicates, n, m):
    if n < 2: return
    if board[0][0] == board[1][0] and board[1][0] == board[1][1]:
        m.addConstrs(is_black[i][i] == 1 for i in range(2))
        m.addConstr(is_black[0][1] == 0)
        m.addConstr(is_black[1][0] == 0)

        # Update duplicates