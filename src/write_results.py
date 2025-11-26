# Given a solved board, creates a string-representation of the solution
def get_results(m, is_black, n, board):
    string = str(n) + "\n\n"

    for i in range(n):
        for j in range(n):
            if type(is_black[i][j]) == int or not m.getAttr('X', [is_black[i][j]])[0]:
                string += (str(board[i][j]) + " ")
            else:
                string += (str(board[i][j]) + "B" + " ")
        string += "\n"

    return string
