import gurobipy as gp
from gurobipy import GRB
from colorama import Fore, Back, Style

# THIS SOLVER IS BROKEN AND SHOULD NOT BE USED
#
# It uses an experimental path_constraint algorithm that has not passed the testing phase
# Use of this solver may result in a correct solution, in which case you were lucky
# Don't actually use this to solve puzzles




def read_file():
    file = open("problem_instances/c36f666a-7b7d-42cd-bbec-5b9d6f541235.singles", "r")
    line = file.readline()
    while type(int(line)) != int: continue
    n = int(line)

    board = [[0] * n] * n

    file.readline()

    for i in range(n):
        board[i] = [int(number) for number in file.readline().split()]

    print("board", board)

    line = file.readline()

    while line:
        print(line.strip())
        line = file.readline()
    file.close()

    return n, board


def no_adjacent(m, n, is_black):
    # each var added with its neighbour should not exceed 1
    for i in range(n - 1):
        for j in range(n):
            m.addConstr(is_black[i][j] + is_black[i + 1][j] <= 1)

    for i in range(n):
        for j in range(n - 1):
            m.addConstr(is_black[i][j] + is_black[i][j + 1] <= 1)

    m.update()


def all_unique(m, n, is_black, board):
    # sum (i=1 till n) x_i,k = 1 for k = 1, 2, 3, ..., n

    # For each row we make a map, from a value (the value on the board) to all the variables
    # on a square with that value. We sum all these variables, and that should not exceed 1
    for i in range(n):
        horizontal_map = {}
        print(i)
        for j in range(n):
            if board[i][j] in horizontal_map:
                horizontal_map[board[i][j]].add(1 - is_black[i][j])
                print("Adding to horizontalMap", horizontal_map[board[i][j]])
            else:
                horizontal_map[board[i][j]] = 1 - is_black[i][j]
                print("Adding to horizontalMap", horizontal_map[board[i][j]])

            print("horizontal map for value", board[i][j], horizontal_map[board[i][j]])

        m.addConstrs(horizontal_map[i] <= 1 for i in range(1, n + 1) if i in horizontal_map)

    # For each column we make a map, from a value (the value on the board) to all the variables
    # on a square with that value. We sum all these variables, and that should not exceed 1
    for j in range(n):
        vertical_map = {}
        print(j)
        for i in range(n):
            if board[i][j] in vertical_map:
                vertical_map[board[i][j]].add(1 - is_black[i][j])
                print("Adding to horizontalMap", vertical_map[board[i][j]])
            else:
                vertical_map[board[i][j]] = 1 - is_black[i][j]
                print("Adding to horizontalMap", vertical_map[board[i][j]])

            print("horizontal map for value", board[i][j], vertical_map[board[i][j]])

        m.addConstrs(vertical_map[i] <= 1 for i in range(1, n + 1) if i in vertical_map)

# Note: This method does not work, and should not be used!
def single_path(m, n, is_black):
    # Make another 2d array of variables in the size of the board
    make_path = list()

    for i in range(n):
        new_list = list()
        for j in range(n):
            new_list.append(m.addVar(vtype=GRB.BINARY, name=f'is_black {i}_{j}'))
        make_path.append(new_list)
    m.update()

    # Create an expression we will use for our objective. The objective expression counts
    # all the variables in make_path. Since we will maximise our objective, the model is
    # incentivised to add as many variables to the path as possible
    objective_expression = gp.LinExpr()

    for i in range(n):
        for j in range(n):
            objective_expression.add(make_path[i][j])

    # If a tile is black, it's value in make_path must be 0 (it is not part of the path)
    m.addConstrs(
        make_path[x][y] == 1 - is_black[x][y] for x in range(n) for y in range(n))

    # For each variable in make_path we now add a rule that it can only be set to 1 if a
    # neighbour is also set to 1
    for i in range(n - 1):
        for j in range(n):
            if i == 0 and j == 0: continue # Exempt the top left corner and a neighbour so that the model
            if i == 0 and j == 1: continue # has someplace to start

            s = m.addVar(vtype=GRB.BINARY)
            m.addConstr(make_path[i][j] + make_path[i + 1][j] <= 1 + s)  # s = 0: <= 1     s = 1: <= 2
            m.addConstr(make_path[i][j] + make_path[i + 1][j] >= 1 + s)  # s = 0: >= 1     s = 1: >= 2

    for i in range(n):
        for j in range(n - 1):
            if i == 0 and j == 0: continue # Exempt the top left corner and a neighbour so that the model
            if i == 0 and j == 1: continue # has someplace to start

            t = m.addVar(vtype=GRB.BINARY)
            m.addConstr(make_path[i][j] + make_path[i][j + 1] <= 1 + t)  # t = 0: <= 1       t = 1: <= 2
            m.addConstr(make_path[i][j] + make_path[i][j + 1] >= 1 + t)  # t = 0: >= 1       t = 1: >= 2

    m.setObjective(objective_expression, GRB.MAXIMIZE)


def main():
    n, board = read_file()

    # Create a new model
    m = gp.Model("Hitori")

    # Add all the variables
    is_black = list()

    for i in range(n):
        new_list = list()
        for j in range(n):
            new_list.append(m.addVar(vtype=GRB.BINARY, name=f'is_black {i}_{j}'))
        is_black.append(new_list)
    m.update()

    # No adjacent black squares
    no_adjacent(m, n, is_black)

    # All unique on each row and column
    all_unique(m, n, is_black, board)

    # Single path
    single_path(m, n, is_black)

    # Optimise the model
    m.optimize()

    if m.status == GRB.INFEASIBLE:
        print("Infeasible")
    else:
        # Get results
        pretty_print(m, is_black, n, board)
        get_results(m, is_black, n, board)

if __name__ == "__main__":
    main()
