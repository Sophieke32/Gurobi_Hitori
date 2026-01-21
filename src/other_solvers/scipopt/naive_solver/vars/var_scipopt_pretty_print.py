from colorama import Fore, Back, Style

def var_scipopt_pretty_print(m, is_covered, n, board, that_one_var):
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                if not m.getVal(that_one_var):
                    print(Style.RESET_ALL + Back.WHITE + Fore.BLACK + " " + get_cube(str(board[i][j]), n), end=" ")
                else:
                    print(Back.BLACK + Fore.WHITE + "", get_cube(str(board[i][j]), n), end=" ")
            else:
                if not m.getVal(is_covered[i][j]):
                    print(Style.RESET_ALL + Back.WHITE + Fore.BLACK + " " + get_cube(str(board[i][j]), n), end=" ")
                else:
                    print(Back.BLACK + Fore.WHITE + "", get_cube(str(board[i][j]), n), end=" ")
        print(Style.RESET_ALL)

def get_cube(s, n):
    return s + (len(str(n)) - len(s)) * " "
