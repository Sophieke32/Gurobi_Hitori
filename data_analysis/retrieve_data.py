from data_analysis.helper_methods.process_data import get_csv, get_csv_small, get_csv_better

benchmark_asp = get_csv_small("data_files/benchmark/asp.csv")
benchmark_gurobi = get_csv_small("data_files/benchmark/gurobi.csv")
benchmark_prolog = get_csv_small("data_files/benchmark/prolog.csv")
benchmark_pumpkin = get_csv_small("data_files/benchmark/pumpkin.csv")
benchmark_z3 = get_csv_small("data_files/benchmark/z3.csv")

duplicates = get_csv_better("data_files/duplicates.csv")
duplicates_ntest = get_csv_small("data_files/duplicates_ntest.csv")
duplicates_cch = get_csv_better("data_files/duplicates_cch_constraint.csv")
duplicates_edge_pairs = get_csv_better("data_files/duplicates_edge_pairs_constraint.csv")
duplicates_least_whites = get_csv_better("data_files/duplicates_least_whites_constraint.csv")
duplicates_most_blacks = get_csv_better("data_files/duplicates_most_blacks_constraint.csv")
duplicates_pair_isolation = get_csv_better("data_files/duplicates_pair_isolation_constraint.csv")
duplicates_sandwiches = get_csv_better("data_files/duplicates_sandwiches_constraint.csv")


path = get_csv_better("data_files/path.csv")
path_ntest = get_csv_small("data_files/path_ntest.csv")
path_cc = get_csv_better("data_files/path_cc.csv")
path_cch = get_csv_better("data_files/path_cch_constraint.csv")
path_edge_pairs = get_csv_better("data_files/path_edge_pairs_constraint.csv")
path_least_whites = get_csv_better("data_files/path_least_whites_constraint.csv")
path_most_blacks = get_csv_better("data_files/path_most_blacks_constraint.csv")
path_pair_isolation = get_csv_better("data_files/path_pair_isolation_constraint.csv")
path_sandwiches = get_csv_better("data_files/path_sandwiches_constraint.csv")


naive = get_csv_better("data_files/naive.csv")
naive_ntest = get_csv_small("data_files/naive_ntest.csv")

naive_bfs = get_csv_better("data_files/naive_bfs_checker.csv")
naive_connected_component = get_csv_better("data_files/naive_cc_checker.csv")
naive_cycles = get_csv_better("data_files/naive_cycles_checker.csv")

naive_min = get_csv_better("data_files/naive_min_heuristic.csv")
naive_max = get_csv_better("data_files/naive_max_heuristic.csv")
naive_no = get_csv_better("data_files/naive_no_heuristic.csv")

naive_cc = get_csv_better("data_files/naive_cc_constraint.csv")
naive_cch = get_csv_better("data_files/naive_cch_constraint.csv")
naive_edge_pairs = get_csv_better("data_files/naive_edge_pairs_constraint.csv")
naive_least_whites = get_csv_better("data_files/naive_least_whites_constraint.csv")
naive_most_blacks = get_csv_better("data_files/naive_most_blacks_constraint.csv")
naive_pair_isolation = get_csv_better("data_files/naive_pair_isolation_constraint.csv")
naive_sandwiches = get_csv_better("data_files/naive_sandwiches_constraint.csv")


# Dict with all duplicates files for easier exporting to other files
benchmark_files = {"asp": benchmark_asp, "gurobi": benchmark_gurobi, "prolog": benchmark_prolog,
                   "pumpkin": benchmark_pumpkin, "z3": benchmark_z3}

duplicates_files = {"base": duplicates, "ntest": duplicates_ntest, "cch": duplicates_cch, "edge pairs": duplicates_edge_pairs,
                    "least whites": duplicates_least_whites, "most blacks": duplicates_most_blacks,
                    "pair isolation": duplicates_pair_isolation, "sandwiches": duplicates_sandwiches}

path_files = {"base": path, "ntest": path_ntest, "cc": path_cc, "cch": path_cch, "edge pairs": path_edge_pairs,
                    "least whites": path_least_whites, "most blacks": path_most_blacks,
                    "pair isolation": path_pair_isolation, "sandwiches": path_sandwiches}

# Dict with all naive files for easier exporting
naive_files = {"base": naive, "ntest": naive_ntest, "bfs": naive_bfs, "connected component": naive_connected_component,
               "cycles": naive_cycles, "min heuristic": naive_min, "max heuristic": naive_max,
               "no heuristic": naive_no, "cc": naive_cc, "cch": naive_cch, "edge pairs": naive_edge_pairs,
               "least whites": naive_least_whites, "most blacks": naive_most_blacks,
               "pair isolation": naive_pair_isolation, "sandwiches": naive_sandwiches}
