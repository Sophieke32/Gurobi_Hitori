from colorama import Fore, Back, Style

def pretty_print(m, is_covered, n, board):
    for i in range(n):
        for j in range(n):
            if type(is_covered[i][j]) == int:
                print(Style.RESET_ALL + Back.WHITE + Fore.BLACK + " " + get_cube(str(board[i][j]), n), end=" ")
            elif m.getAttr('X', [is_covered[i][j]])[0]:
                print(Back.BLACK + Fore.WHITE + "", get_cube(str(board[i][j]), n), end=" ")
            else: print(Style.RESET_ALL + Back.WHITE + Fore.BLACK + " " + get_cube(str(board[i][j]), n), end=" ")
        print(Style.RESET_ALL)

def get_cube(s, n):
    return s + (len(str(n)) - len(s)) * " "

def path_pretty_print(m, is_covered, path, n, board):
    for i in range(n):
        for j in range(n):

            print_board_square(is_covered[i][j], n, m, board[i][j])

        print(Style.RESET_ALL, end="")

        print(5 * " ", end="")

        for j in range(n):
            print_path_square(path[i][j], is_covered[i][j], n, m, board[i][j])

        print(Style.RESET_ALL)

def print_board_square(board_tile, n, m, value):
    if m.getAttr('X', [board_tile])[0]:
        print(Back.BLACK + Fore.WHITE + "", get_cube(str(value), n), end=" ")
    else:
        print(Style.RESET_ALL + Back.WHITE + Fore.BLACK + " " + get_cube(str(value), n), end=" ")


def print_path_square(path_tile, board_tile, n, m, value):
    if m.getAttr('X', [path_tile])[0]:
        print(Back.LIGHTBLUE_EX + Fore.BLACK + "", get_cube(str(value), n), end=" ")
    else:
        print_board_square(board_tile, n, m, value)
