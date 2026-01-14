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
        # f.readline()

        # print(f.readline().replace("# Computed in ", "").replace(" nanoseconds", ""))
        number_of_covered_tiles = f.readline().replace("# Number of covered tiles: ", "").replace("\n", "")
        number_of_duplicates = f.readline().replace("# Number of duplicates: ", "").replace("\n", "")
        number_of_cycles = f.readline().replace("# Number of cycles: ", "").replace("\n", "")
        corner_checks = f.readline().replace("# Corner-checks hits: ", "").replace("\n", "")
        edge_pairs = f.readline().replace("# Edge-pairs hits: ", "").replace("\n", "")
        pair_isolations = f.readline().replace("# Pair-isolation hits: ", "").replace("\n", "")
        pairs = f.readline().replace("# Sandwich-pair hits: ", "").replace("\n", "")
        triples = f.readline().replace("# Sandwich-triple hits: ", "").replace("\n", "")
        duplicates_time = f.readline().replace("# Time spent making duplicates array (s): ", "").replace("\n", "")
        graph_time = f.readline().replace("# Time spent making graph (s): ", "").replace("\n", "")
        runs = f.readline().replace("# Number of runs to collect time data: ", "").replace("\n", "")
        iterations = f.readline().replace("# Number of iterations: ", "").replace("\n", "")
        time_illegal_solutions = f.readline().replace("# Time spent on illegal solutions (s): ", "").replace("\n", "")

        data = {
            "number_of_covered_tiles": number_of_covered_tiles,
            "number_of_duplicates": number_of_duplicates,
            "number_of_cycles": number_of_cycles,
            "corner_check_hits": corner_checks,
            "edge_pairs_hits": edge_pairs,
            "pair_isolation_hits": pair_isolations,
            "sandwich_pairs_hits": pairs,
            "sandwich_triple_hits": triples,
            "duplicates_time": duplicates_time,
            "graph_time": graph_time,
            "runs": runs,
            "iterations": iterations,
            "time_illegal_solutions": time_illegal_solutions,
        }

        return n, board, data
