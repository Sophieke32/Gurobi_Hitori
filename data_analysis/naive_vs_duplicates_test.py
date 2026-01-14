import csv

from data_analysis.helper_methods.descriptive_statistics import print_descriptive_statistics
from data_analysis.helper_methods.permutation_test import print_permutation_test
from data_analysis.helper_methods.wilcoxon_test import print_wilcoxon_test
from data_analysis.retrieve_data import naive_files, duplicates_files

def naive_vs_duplicates_test(verbose=False):
    print("Performing naive vs duplicates tests...")
    if verbose:
        print("\n########################### Describe Naive Heuristics: ###########################")
        print("Optimised naive:", print_descriptive_statistics(naive_files["base"]))
        print("Duplicates:", print_descriptive_statistics(duplicates_files["base"]))

    ########################### Permutation Test: ###########################
    res = []
    res.append(["naive", "duplicates", print_permutation_test(naive_files['base']['cpu time'], duplicates_files['base']['cpu time'])])

    with open("results/naive_vs_duplicates.csv", "w", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["model 1", "model 2", "direction", "p-value"])
        writer.writeheader()

        for i in res:
            if i[2][0] == 'greater':
                writer.writerow({"model 1": i[1], "model 2": i[0], "direction": 'less', "p-value": i[2][1]})
            else:
                writer.writerow({"model 1": i[0], "model 2": i[1], "direction": i[2][0], "p-value": i[2][1]})
