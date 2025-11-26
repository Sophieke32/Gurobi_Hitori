def get_results(m, is_black, n, board):
    print(n)
    print()

    for i in range(n):
        for j in range(n):
            if type(is_black[i][j]) == int or not m.getAttr('X', [is_black[i][j]])[0]:
                print(str(board[i][j]), end=" ")
            else:
                print(str(board[i][j]) + "B", end=" ")
        print()