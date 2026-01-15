import csv

import pylab

from data_analysis.helper_methods.bartlett_test import bartlett_test_3
from data_analysis.helper_methods.descriptive_statistics import print_descriptive_statistics
from data_analysis.helper_methods.permutation_test import print_permutation_test
from data_analysis.helper_methods.qq_plot import create_qq_plot
from data_analysis.helper_methods.shapiro_wilk_test import shapiro_test
from data_analysis.retrieve_data import naive_files


def heuristic_tests(verbose=False):
    print("Performing heuristic tests...")
    if verbose:
        print("\n\n########################### Describe Naive Heuristics: ###########################")
        print("No heuristics:", print_descriptive_statistics(naive_files["no heuristic"]))
        print("Min heuristics:", print_descriptive_statistics(naive_files["min heuristic"]))
        print("Max heuristics:", print_descriptive_statistics(naive_files["max heuristic"]))


        print("\n########################### Shapiro Wilk test optimised naive: ###########################")
        shapiro_test(naive_files["no heuristic"])
        shapiro_test(naive_files["min heuristic"])
        shapiro_test(naive_files["max heuristic"])


        print("\n########################### Compare Variances: ###########################")
        bartlett_test_3(naive_files["no heuristic"], naive_files["min heuristic"], naive_files["max heuristic"])
        print("So variances differ")


    ########################### Permutation Test: ###########################
    res = []
    res.append(["no heuristic", "min heuristic", print_permutation_test(naive_files['no heuristic']['cpu time'], naive_files['min heuristic']['cpu time'])])
    res.append(["no heuristic", "max heuristic", print_permutation_test(naive_files['no heuristic']['cpu time'], naive_files['max heuristic']['cpu time'])])
    res.append(["min heuristic", "max heuristic", print_permutation_test(naive_files['min heuristic']['cpu time'], naive_files['max heuristic']['cpu time'])])


    with open("results/heuristic_tests.csv", "w", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["model 1", "model 2", "mean difference", "p-value"])
        writer.writeheader()

        for i in res:
            if i[2][2] == 1:
                writer.writerow({"model 1": i[1], "model 2": i[0], "mean difference": i[2][0], "p-value": i[2][1]})
            else:
                writer.writerow({"model 1": i[0], "model 2": i[1], "mean difference": i[2][0], "p-value": i[2][1]})
