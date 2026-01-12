import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import pylab

from data_analysis.helper_methods.descriptive_statistics import print_descriptive_statistics
from data_analysis.helper_methods.process_data import get_csv
from data_analysis.helper_methods.qq_plot import create_qq_plot
from data_analysis.helper_methods.shapiro_wilk_test import shapiro_test
from data_analysis.helper_methods.wilcoxon_test import print_wilcoxon_test
from data_analysis.retrieve_data import duplicates_files, naive_files
from data_analysis.visualisation_methods.show_histogram import show_histogram

def optimisation_rules_tests():

    print("\n########################### Describe Naive Heuristics: ###########################")
    print("Optimised naive base:", print_descriptive_statistics(naive_files["base"]))
    print("Optimised naive corner close:", print_descriptive_statistics(naive_files["cc"]))
    print("Optimised naive corner checking:", print_descriptive_statistics(naive_files["cch"]))
    print("Optimised naive sandwiches:", print_descriptive_statistics(naive_files["sandwiches"]))
    print("Optimised naive edge pairs:", print_descriptive_statistics(naive_files["edge pairs"]))
    print("Optimised naive most blacks:", print_descriptive_statistics(naive_files["most blacks"]))
    print("Optimised naive least whites:", print_descriptive_statistics(naive_files["least whites"]))
    print("Optimised naive pair isolation:", print_descriptive_statistics(naive_files["pair isolation"]))


    print("duplicates base:", print_descriptive_statistics(duplicates_files["base"]))
    print("duplicates edge pairs:", print_descriptive_statistics(duplicates_files["edge pairs"]))

    print("compare", np.count_nonzero(duplicates_files["edge pairs"]['cpu time'] - duplicates_files["base"]['cpu time'] > 0))
    print(len(duplicates_files["edge pairs"]['cpu time']))

    arr2 = duplicates_files["edge pairs"]['cpu time'][duplicates_files["edge pairs"]['cpu time'] < 1]
    arr1 = duplicates_files["base"]['cpu time'][duplicates_files["base"]['cpu time'] < 1]

    plt.hist(arr1, 50, range=(0, 1), alpha=0.3)
    plt.hist(arr2, 50, range=(0, 1), alpha=0.3)
    plt.title('CPU_time (s)')
    plt.show()


    # print("duplicates max black:", print_descriptive_statistics(duplicates_max_black_csv))
    # print("duplicates least white:", print_descriptive_statistics(duplicates_least_whites_csv))
    # print("duplicates pair isolation:", print_descriptive_statistics(duplicates_pair_isolation_csv))

    print("\n########################### Shapiro Wilk test optimised naive: ###########################")
    shapiro_test(naive_files["cc"])
    shapiro_test(naive_files["cch"])
    shapiro_test(naive_files["sandwiches"])
    shapiro_test(naive_files["edge pairs"])
    shapiro_test(naive_files["most blacks"])
    shapiro_test(naive_files["least whites"])
    shapiro_test(naive_files["pair isolation"])
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
    print(stats.friedmanchisquare(naive_files["base"]['cpu time'], naive_files["cc"]['cpu time'], naive_files["cch"]['cpu time'],
                            naive_files["sandwiches"]['cpu time'], naive_files["edge pairs"]['cpu time'], naive_files["most blacks"]['cpu time'],
                            naive_files["least whites"]['cpu time'], naive_files["pair isolation"]['cpu time']))


    # print("Friedman Chi Square test duplicates:")
    # print(stats.friedmanchisquare(duplicates_files["base"]['cpu time'], duplicates_corner_close_csv['cpu time'], duplicates_corner_checking_csv['cpu time'],
    #                         duplicates_sandwiches_csv['cpu time'], duplicates_edge_pairs_csv['cpu time'], duplicates_max_black_csv['cpu time'],
    #                         duplicates_least_whites_csv['cpu time'], duplicates_pair_isolation_csv['cpu time']))

    # print("\nWilcoxon for optimised naive:")
    # print("Base vs corner-close:", print_wilcoxon_test(naive_files["base"], optimised_naive_corner_close_csv, alternative='less'))
    # print("Base vs corner-checking:", print_wilcoxon_test(naive_files["base"], optimised_naive_corner_checking_csv, alternative='less'))
    # print("Base vs sandwiches:", print_wilcoxon_test(naive_files["base"], optimised_naive_sandwiches_csv, alternative='less'))
    # print("Base vs edge pairs:", print_wilcoxon_test(naive_files["base"], optimised_naive_edge_pairs_csv, alternative='less'))
    # print("Base vs max black:", print_wilcoxon_test(naive_files["base"], optimised_naive_max_black_csv, alternative='less'))
    # print("Base vs least whites:", print_wilcoxon_test(naive_files["base"], optimised_naive_least_whites_csv, alternative='less'))
    # print("Base vs pair isolation:", print_wilcoxon_test(naive_files["base"], optimised_naive_pair_isolation_csv, alternative='less'))
    # print("Base vs all:", print_wilcoxon_test(naive_files["base"], optimised_naive_all_csv, alternative='greater'))

    print("\nWilcoxon for duplicates:")
    # print("Base vs corner-close:", print_wilcoxon_test(duplicates_files["base"], duplicates_corner_close_csv, alternative='less'))
    # print("Base vs corner-checking:", print_wilcoxon_test(duplicates_files["base"], duplicates_corner_checking_csv, alternative='less'))
    # print("Base vs sandwiches:", print_wilcoxon_test(duplicates_files["base"], duplicates_sandwiches_csv, alternative='less'))
    print("Base vs edge pairs:", print_wilcoxon_test(duplicates_files["base"], duplicates_files["edge pairs"], alternative='greater'))
    # print("Base vs max black:", print_wilcoxon_test(duplicates_files["base"], duplicates_max_black_csv, alternative='greater'))
    # print("Base vs least whites:", print_wilcoxon_test(duplicates_files["base"], duplicates_least_whites_csv, alternative='less'))
    # print("Base vs pair isolation:", print_wilcoxon_test(duplicates_files["base"], duplicates_pair_isolation_csv))
    # print("Base vs all:", print_wilcoxon_test(duplicates_files["base"], optimised_naive_all_csv, alternative='greater'))
