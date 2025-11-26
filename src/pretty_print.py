from colorama import Fore, Back, Style

def pretty_print(m, is_black, n, board):
    for i in range(n):
        for j in range(n):
            if type(is_black[i][j]) == int:
                print(Style.RESET_ALL + Back.WHITE + Fore.BLACK + " " + get_cube(str(board[i][j]), n), end=" ")
            elif m.getAttr('X', [is_black[i][j]])[0]:
                print(Back.BLACK + Fore.WHITE + "", get_cube(str(board[i][j]), n), end=" ")
            else: print(Style.RESET_ALL + Back.WHITE + Fore.BLACK + " " + get_cube(str(board[i][j]), n), end=" ")
        print(Style.RESET_ALL)

def get_cube(s, n):
    return s + (len(str(n)) - len(s)) * " "