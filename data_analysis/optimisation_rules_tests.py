import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import pylab

from data_analysis.helper_methods.descriptive_statistics import print_descriptive_statistics
from data_analysis.helper_methods.process_data import get_csv
from data_analysis.helper_methods.qq_plot import create_qq_plot
from data_analysis.helper_methods.shapiro_wilk_test import shapiro_test
from data_analysis.helper_methods.wilcoxon_test import print_wilcoxon_test
from data_analysis.visualisation_methods.show_histogram import show_histogram

# Redundant Constraints (all are n = 10, BFS, min heuristic)
optimised_naive_corner_close_file = "data_files/redundant_constraints/optimised_naive_corner_close.csv"
optimised_naive_corner_checking_file = "data_files/redundant_constraints/optimised_naive_corner_check.csv"
optimised_naive_sandwiches_file = "data_files/redundant_constraints/optimised_naive_sandwiches.csv"
optimised_naive_edge_pairs_file = "data_files/redundant_constraints/optimised_naive_edge_pairs.csv"
optimised_naive_most_blacks_file = "data_files/redundant_constraints/optimised_naive_most_blacks.csv"
optimised_naive_least_whites_file = "data_files/redundant_constraints/optimised_naive_least_whites.csv"
optimised_naive_pair_isolation_file = "data_files/redundant_constraints/optimised_naive_pair_isolation.csv"
# optimised_naive_all_file = "data_files/redundant_constraints/optimised_naive_all.csv"

duplicates_corner_close_file = "data_files/redundant_constraints/duplicates_corner_close.csv"
duplicates_corner_checking_file = "data_files/redundant_constraints/duplicates_corner_check.csv"
duplicates_sandwiches_file = "data_files/redundant_constraints/duplicates_sandwiches.csv"
duplicates_edge_pairs_file = "data_files/redundant_constraints/duplicates_edge_pairs.csv"
duplicates_most_blacks_file = "data_files/redundant_constraints/duplicates_most_blacks.csv"
duplicates_least_whites_file = "data_files/redundant_constraints/duplicates_least_whites.csv"
duplicates_pair_isolation_file = "data_files/redundant_constraints/duplicates_pair_isolation.csv"
# duplicates_all_file = "data_files/redundant_constraints/duplicates_all.csv"

optimised_naive_corner_close_csv = get_csv(optimised_naive_corner_close_file)
optimised_naive_corner_checking_csv = get_csv(optimised_naive_corner_checking_file)
optimised_naive_sandwiches_csv = get_csv(optimised_naive_sandwiches_file)
optimised_naive_edge_pairs_csv = get_csv(optimised_naive_edge_pairs_file)
optimised_naive_max_black_csv = get_csv(optimised_naive_most_blacks_file)
optimised_naive_least_whites_csv = get_csv(optimised_naive_least_whites_file)
optimised_naive_pair_isolation_csv = get_csv(optimised_naive_pair_isolation_file)
# optimised_naive_all_csv = get_csv(optimised_naive_all_file)

duplicates_corner_close_csv = get_csv(duplicates_corner_close_file)
duplicates_corner_checking_csv = get_csv(duplicates_corner_checking_file)
duplicates_sandwiches_csv = get_csv(duplicates_sandwiches_file)
duplicates_edge_pairs_csv = get_csv(duplicates_edge_pairs_file)
duplicates_max_black_csv = get_csv(duplicates_most_blacks_file)
duplicates_least_whites_csv = get_csv(duplicates_least_whites_file)
duplicates_pair_isolation_csv = get_csv(duplicates_pair_isolation_file)
# duplicates_all_csv = get_csv(duplicates_all_file)


duplicates_n10_file = "data_files/duplicates_n10.csv"  # duplicates model, n = 10, experiment_10_instances
optimised_naive_n10_file = "data_files/optimised_naive_n10.csv"  # duplicates model, n = 10, experiment_10_instances

duplicates_n10_csv = get_csv(duplicates_n10_file)
optimised_naive_n10_csv = get_csv(optimised_naive_n10_file)

def optimisation_rules_tests():

    print("\n########################### Describe Naive Heuristics: ###########################")
    # print("Optimised naive base:", print_descriptive_statistics(optimised_naive_n10_csv))
    # print("Optimised naive corner close:", print_descriptive_statistics(optimised_naive_corner_close_csv))
    # print("Optimised naive corner checking:", print_descriptive_statistics(optimised_naive_corner_checking_csv))
    # print("Optimised naive sandwiches:", print_descriptive_statistics(optimised_naive_sandwiches_csv))
    # print("Optimised naive edge pairs:", print_descriptive_statistics(optimised_naive_edge_pairs_csv))
    # print("Optimised naive most blacks:", print_descriptive_statistics(optimised_naive_max_black_csv))
    # print("Optimised naive least whites:", print_descriptive_statistics(optimised_naive_least_whites_csv))
    # print("Optimised naive pair isolation:", print_descriptive_statistics(optimised_naive_pair_isolation_csv))


    print("duplicates base:", print_descriptive_statistics(duplicates_n10_csv))
    print("duplicates edge pairs:", print_descriptive_statistics(duplicates_edge_pairs_csv))

    print("compare", np.count_nonzero(duplicates_edge_pairs_csv['cpu time'] - duplicates_n10_csv['cpu time'] > 0))
    print(len(duplicates_edge_pairs_csv['cpu time']))

    arr2 = duplicates_edge_pairs_csv['cpu time'][duplicates_edge_pairs_csv['cpu time'] < 1]
    arr1 = duplicates_n10_csv['cpu time'][duplicates_n10_csv['cpu time'] < 1]

    plt.hist(arr1, 50, range=(0, 1), alpha=0.3)
    plt.hist(arr2, 50, range=(0, 1), alpha=0.3)
    plt.title('CPU_time (s)')
    plt.show()


    # print("duplicates max black:", print_descriptive_statistics(duplicates_max_black_csv))
    # print("duplicates least white:", print_descriptive_statistics(duplicates_least_whites_csv))
    # print("duplicates pair isolation:", print_descriptive_statistics(duplicates_pair_isolation_csv))

    print("\n########################### Shapiro Wilk test optimised naive: ###########################")
    # shapiro_test(optimised_naive_corner_close_csv)
    # shapiro_test(optimised_naive_corner_checking_csv)
    # shapiro_test(optimised_naive_sandwiches_csv)
    # shapiro_test(optimised_naive_edge_pairs_csv)
    # shapiro_test(optimised_naive_max_black_csv)
    # shapiro_test(optimised_naive_least_whites_csv)
    # shapiro_test(optimised_naive_pair_isolation_csv)
    # shapiro_test(optimised_naive_all_csv)

    # print("\n########################### Shapiro Wilk test duplicates: ###########################")
    # shapiro_test(duplicates_corner_close_csv)
    # shapiro_test(duplicates_corner_checking_csv)
    # shapiro_test(duplicates_sandwiches_csv)
    # shapiro_test(duplicates_edge_pairs_csv)
    # shapiro_test(duplicates_max_black_csv)
    # shapiro_test(duplicates_least_whites_csv)
    # shapiro_test(duplicates_pair_isolation_csv)
    # shapiro_test(duplicates_all_csv)


    # print("\n########################### QQ plots: ###########################")
    # create_qq_plot(duplicates_all_csv)
    # pylab.savefig("figures/qq-plot4.svg")
    # pylab.show()
    # print("Non-parametric")


    print("\n############################## Optimisation Rules: ##############################")
    print("Friedman Chi Square test optimised naive:")
    print(stats.friedmanchisquare(optimised_naive_n10_csv['cpu time'], optimised_naive_corner_close_csv['cpu time'], optimised_naive_corner_checking_csv['cpu time'],
                            optimised_naive_sandwiches_csv['cpu time'], optimised_naive_edge_pairs_csv['cpu time'], optimised_naive_max_black_csv['cpu time'],
                            optimised_naive_least_whites_csv['cpu time'], optimised_naive_pair_isolation_csv['cpu time']))


    # print("Friedman Chi Square test duplicates:")
    # print(stats.friedmanchisquare(duplicates_n10_csv['cpu time'], duplicates_corner_close_csv['cpu time'], duplicates_corner_checking_csv['cpu time'],
    #                         duplicates_sandwiches_csv['cpu time'], duplicates_edge_pairs_csv['cpu time'], duplicates_max_black_csv['cpu time'],
    #                         duplicates_least_whites_csv['cpu time'], duplicates_pair_isolation_csv['cpu time']))

    # print("\nWilcoxon for optimised naive:")
    # print("Base vs corner-close:", print_wilcoxon_test(optimised_naive_n10_csv, optimised_naive_corner_close_csv, alternative='less'))
    # print("Base vs corner-checking:", print_wilcoxon_test(optimised_naive_n10_csv, optimised_naive_corner_checking_csv, alternative='less'))
    # print("Base vs sandwiches:", print_wilcoxon_test(optimised_naive_n10_csv, optimised_naive_sandwiches_csv, alternative='less'))
    # print("Base vs edge pairs:", print_wilcoxon_test(optimised_naive_n10_csv, optimised_naive_edge_pairs_csv, alternative='less'))
    # print("Base vs max black:", print_wilcoxon_test(optimised_naive_n10_csv, optimised_naive_max_black_csv, alternative='less'))
    # print("Base vs least whites:", print_wilcoxon_test(optimised_naive_n10_csv, optimised_naive_least_whites_csv, alternative='less'))
    # print("Base vs pair isolation:", print_wilcoxon_test(optimised_naive_n10_csv, optimised_naive_pair_isolation_csv, alternative='less'))
    # print("Base vs all:", print_wilcoxon_test(optimised_naive_n10_csv, optimised_naive_all_csv, alternative='greater'))

    print("\nWilcoxon for duplicates:")
    # print("Base vs corner-close:", print_wilcoxon_test(duplicates_n10_csv, duplicates_corner_close_csv, alternative='less'))
    # print("Base vs corner-checking:", print_wilcoxon_test(duplicates_n10_csv, duplicates_corner_checking_csv, alternative='less'))
    # print("Base vs sandwiches:", print_wilcoxon_test(duplicates_n10_csv, duplicates_sandwiches_csv, alternative='less'))
    print("Base vs edge pairs:", print_wilcoxon_test(duplicates_n10_csv, duplicates_edge_pairs_csv, alternative='greater'))
    # print("Base vs max black:", print_wilcoxon_test(duplicates_n10_csv, duplicates_max_black_csv, alternative='greater'))
    # print("Base vs least whites:", print_wilcoxon_test(duplicates_n10_csv, duplicates_least_whites_csv, alternative='less'))
    # print("Base vs pair isolation:", print_wilcoxon_test(duplicates_n10_csv, duplicates_pair_isolation_csv))
    # print("Base vs all:", print_wilcoxon_test(duplicates_n10_csv, optimised_naive_all_csv, alternative='greater'))
