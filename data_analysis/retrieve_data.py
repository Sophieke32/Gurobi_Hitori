from data_analysis.helper_methods.process_data import get_csv

duplicates = get_csv("data_files/duplicates.csv")
duplicates_cch = get_csv("data_files/duplicates_cch_constraint.csv")
duplicates_edge_pairs = get_csv("data_files/duplicates_edge_pairs_constraint.csv")
duplicates_least_whites = get_csv("data_files/duplicates_least_whites_constraint.csv")
duplicates_most_blacks = get_csv("data_files/duplicates_most_blacks_constraint.csv")
duplicates_pair_isolation = get_csv("data_files/duplicates_pair_isolation_constraint.csv")
duplicates_sandwiches = get_csv("data_files/duplicates_sandwiches_constraint.csv")


naive = get_csv("data_files/naive_solver.csv")

naive_bfs = get_csv("data_files/naive_bfs_checker.csv")
naive_connected_component = get_csv("data_files/naive_cc_checker.csv")
naive_cycles = get_csv("data_files/naive_cycles_checker.csv")

naive_min = get_csv("data_files/naive_min_heuristic.csv")
naive_max = get_csv("data_files/naive_max_heuristic.csv")
naive_no = get_csv("data_files/naive_no_heuristic.csv")

naive_cc = get_csv("data_files/naive_cc_constraint.csv")
naive_cch = get_csv("data_files/naive_cch_constraint.csv")
naive_edge_pairs = get_csv("data_files/naive_edge_pairs_constraint.csv")
naive_least_whites = get_csv("data_files/naive_least_whites_constraint.csv")
naive_most_blacks = get_csv("data_files/naive_most_blacks_constraint.csv")
naive_pair_isolation = get_csv("data_files/naive_pair_isolation_constraint.csv")
naive_sandwiches = get_csv("data_files/naive_sandwiches_constraint.csv")

# Dict with all duplicates files for easier exporting to other files
duplicates_files = {"base": duplicates, "cch": duplicates_cch, "edge pairs": duplicates_edge_pairs,
                    "least whites": duplicates_least_whites, "most blacks": duplicates_most_blacks,
                    "pair isolation": duplicates_pair_isolation, "sandwiches": duplicates_sandwiches}

# Dict with all naive files for easier exporting
naive_files = {"base": naive, "bfs": naive_bfs, "connected component": naive_connected_component,
               "cycles": naive_cycles, "min heuristic": naive_min, "max heuristic": naive_max,
               "no heuristic": naive_no, "cc": naive_cc, "cch": naive_cch, "edge pairs:": naive_edge_pairs,
               "least whites": naive_least_whites, "most blacks": naive_most_blacks,
               "pair isolation": naive_pair_isolation, "sandwiches": naive_sandwiches}