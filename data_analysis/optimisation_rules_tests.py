import csv

import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import pylab

from data_analysis.helper_methods.descriptive_statistics import print_descriptive_statistics
from data_analysis.helper_methods.permutation_test import print_permutation_test
from data_analysis.helper_methods.process_data import get_csv
from data_analysis.helper_methods.qq_plot import create_qq_plot
from data_analysis.helper_methods.shapiro_wilk_test import shapiro_test
from data_analysis.helper_methods.wilcoxon_test import print_wilcoxon_test
from data_analysis.retrieve_data import duplicates_files, naive_files
from data_analysis.visualisation_methods.show_histogram import show_histogram

def optimisation_rules_tests(verbose=False):
    print("Performing optimisation rules tests...")
    if verbose:
        print("\n########################### Describe Naive Heuristics: ###########################")
        print("Optimised naive base:", print_descriptive_statistics(naive_files["base"]))
        print("Optimised naive corner close:", print_descriptive_statistics(naive_files["cc"]))
        print("Optimised naive corner checking:", print_descriptive_statistics(naive_files["cch"]))
        print("Optimised naive sandwiches:", print_descriptive_statistics(naive_files["sandwiches"]))
        print("Optimised naive edge pairs:", print_descriptive_statistics(naive_files["edge pairs"]))
        print("Optimised naive most blacks:", print_descriptive_statistics(naive_files["most blacks"]))
        print("Optimised naive least whites:", print_descriptive_statistics(naive_files["least whites"]))
        print("Optimised naive pair isolation:", print_descriptive_statistics(naive_files["pair isolation"]))

        print("\n########################### Describe Duplicates Heuristics: ###########################")
        print("duplicates base:", print_descriptive_statistics(duplicates_files['base']))
        print("duplicates corner checking:", print_descriptive_statistics(duplicates_files['cch']))
        print("duplicates sandwiches:", print_descriptive_statistics(duplicates_files['sandwiches']))
        print("duplicates edge pairs:", print_descriptive_statistics(duplicates_files['edge pairs']))
        print("duplicates max black:", print_descriptive_statistics(duplicates_files['most blacks']))
        print("duplicates least white:", print_descriptive_statistics(duplicates_files['least whites']))
        print("duplicates pair isolation:", print_descriptive_statistics(duplicates_files['pair isolation']))

        print("\n########################### Shapiro Wilk test optimised naive: ###########################")
        shapiro_test(naive_files["base"])
        shapiro_test(naive_files["cc"])
        shapiro_test(naive_files["cch"])
        shapiro_test(naive_files["sandwiches"])
        shapiro_test(naive_files["edge pairs"])
        shapiro_test(naive_files["most blacks"])
        shapiro_test(naive_files["least whites"])
        shapiro_test(naive_files["pair isolation"])
        # shapiro_test(optimised_naive_all_csv)

        print("\n########################### Shapiro Wilk test duplicates: ###########################")
        shapiro_test(duplicates_files['base'])
        shapiro_test(duplicates_files['cch'])
        shapiro_test(duplicates_files['sandwiches'])
        shapiro_test(duplicates_files['edge pairs'])
        shapiro_test(duplicates_files['most blacks'])
        shapiro_test(duplicates_files['least whites'])
        shapiro_test(duplicates_files['pair isolation'])
        # shapiro_test(duplicates_files['all'])


    ########################### QQ plots: ###########################
    # create_qq_plot(duplicates_all_csv)
    # pylab.savefig("figures/qq-plot4.svg")

    ########################### Permutation Test: ###########################
    res_duplicates = []
    res_duplicates.append(["naive base", "naive cc", print_permutation_test(naive_files['base']['cpu time'], naive_files['cc']['cpu time'])])
    res_duplicates.append(["naive base", "naive cch", print_permutation_test(naive_files['base']['cpu time'], naive_files['cch']['cpu time'])])
    res_duplicates.append(["naive base", "naive sandwiches", print_permutation_test(naive_files['base']['cpu time'], naive_files['sandwiches']['cpu time'])])
    res_duplicates.append(["naive base", "naive edge pairs", print_permutation_test(naive_files['base']['cpu time'], naive_files['edge pairs']['cpu time'])])
    res_duplicates.append(["naive base", "naive most blacks", print_permutation_test(naive_files['base']['cpu time'], naive_files['most blacks']['cpu time'])])
    res_duplicates.append(["naive base", "naive least whites", print_permutation_test(naive_files['base']['cpu time'], naive_files['least whites']['cpu time'])])
    res_duplicates.append(["naive base", "naive pair isolation", print_permutation_test(naive_files['base']['cpu time'], naive_files['pair isolation']['cpu time'])])


    with open("results/naive_optimisation_rules_tests.csv", "w", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["model 1", "model 2", "direction", "p-value"])
        writer.writeheader()

        for i in res_duplicates:
            if i[2][0] == 'greater':
                writer.writerow({"model 1": i[1], "model 2": i[0], "direction": 'less', "p-value": i[2][1]})
            else:
                writer.writerow({"model 1": i[0], "model 2": i[1], "direction": i[2][0], "p-value": i[2][1]})

    res_duplicates = []
    res_duplicates.append(["duplicates base", "duplicates cch",
                      print_permutation_test(duplicates_files['base']['cpu time'], duplicates_files['cch']['cpu time'])])
    res_duplicates.append(["duplicates base", "duplicates sandwiches",
                      print_permutation_test(duplicates_files['base']['cpu time'], duplicates_files['sandwiches']['cpu time'])])
    res_duplicates.append(["duplicates base", "duplicates edge pairs",
                      print_permutation_test(duplicates_files['base']['cpu time'], duplicates_files['edge pairs']['cpu time'])])
    res_duplicates.append(["duplicates base", "duplicates most blacks",
                      print_permutation_test(duplicates_files['base']['cpu time'], duplicates_files['most blacks']['cpu time'])])
    res_duplicates.append(["duplicates base", "duplicates least whites",
                      print_permutation_test(duplicates_files['base']['cpu time'], duplicates_files['least whites']['cpu time'])])
    res_duplicates.append(["duplicates base", "duplicates pair isolation", print_permutation_test(duplicates_files['base']['cpu time'],
                                                                                   duplicates_files['pair isolation'][
                                                                                       'cpu time'])])

    with open("results/duplicates_optimisation_rules_tests.csv", "w", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["model 1", "model 2", "direction", "p-value"])
        writer.writeheader()

        for i in res_duplicates:
            if i[2][0] == 'greater':
                writer.writerow({"model 1": i[1], "model 2": i[0], "direction": 'less', "p-value": i[2][1]})
            else:
                writer.writerow({"model 1": i[0], "model 2": i[1], "direction": i[2][0], "p-value": i[2][1]})
