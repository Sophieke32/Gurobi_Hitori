from colorama import Fore, Back, Style

def scipopt_pretty_print(m, is_covered, n, board):
    for i in range(n):
        for j in range(n):
            if not m.getVal(is_covered[i][j]):
                print(Style.RESET_ALL + Back.WHITE + Fore.BLACK + " " + get_cube(str(board[i][j]), n), end=" ")
            else:
                print(Back.BLACK + Fore.WHITE + "", get_cube(str(board[i][j]), n), end=" ")
        print(Style.RESET_ALL)

def get_cube(s, n):
    return s + (len(str(n)) - len(s)) * " "