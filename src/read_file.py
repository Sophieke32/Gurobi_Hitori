import os
import numpy as np


def read_file(root, file):
    with open(os.path.join(root, file), "r") as f:
        line = f.readline()
        while type(int(line)) != int: continue
        n = int(line)

        board = np.zeros((n,n), dtype=int)

        f.readline()

        for i in range(n):
            board[i] = [int(number) for number in f.readline().split()]

        # Skip to the relevant lines
        f.readline()
        f.readline()
        f.readline()

        # print(f.readline().replace("# Computed in ", "").replace(" nanoseconds", ""))
        number_of_covered_tiles = f.readline().replace("# Number of covered squares: ", "").replace("\n", "")
        number_of_cycles = f.readline().replace("# Number of cycles: ", "").replace("\n", "")

        return n, board, number_of_covered_tiles, number_of_cycles