import csv

from data_analysis.helper_methods.descriptive_statistics import print_descriptive_statistics
from data_analysis.helper_methods.permutation_test import print_permutation_test
from data_analysis.retrieve_data import benchmark_files


def benchmark_tests(verbose=False):
    print("Comparing the benchmarked models...")
    if verbose:
        print("\n########################### Describe Naive Heuristics: ###########################")
        print("asp:", print_descriptive_statistics(benchmark_files["asp"]))
        print("gurobi:", print_descriptive_statistics(benchmark_files["gurobi"]))
        print("prolog:", print_descriptive_statistics(benchmark_files["prolog"]))
        print("pumpkin:", print_descriptive_statistics(benchmark_files["pumpkin"]))
        print("z3:", print_descriptive_statistics(benchmark_files["z3"]))

    ########################### Permutation Test: ###########################
    res = []
    res.append(["gurobi", "asp", print_permutation_test(benchmark_files['gurobi']['cpu time'], benchmark_files['asp']['cpu time'])])
    res.append(["gurobi", "prolog", print_permutation_test(benchmark_files['gurobi']['cpu time'], benchmark_files['prolog']['cpu time'])])
    res.append(["gurobi", "pumpkin", print_permutation_test(benchmark_files['gurobi']['cpu time'], benchmark_files['pumpkin']['cpu time'])])
    res.append(["gurobi", "z3", print_permutation_test(benchmark_files['gurobi']['cpu time'], benchmark_files['z3']['cpu time'])])

    with open("results/benchmark_comparison.csv", "w", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["model 1", "model 2", "mean difference", "p-value"])
        writer.writeheader()

        for i in res:
            if i[2][2] == 1:
                writer.writerow({"model 1": i[1], "model 2": i[0], "mean difference": i[2][0], "p-value": i[2][1]})
            else:
                writer.writerow({"model 1": i[0], "model 2": i[1], "mean difference": i[2][0], "p-value": i[2][1]})
