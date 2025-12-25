import pylab
import scipy.stats as stats

from data_analysis.helper_methods.bartlett_test import bartlett_test_3, bartlett_test_2
from data_analysis.helper_methods.descriptive_statistics import print_descriptive_statistics
from data_analysis.helper_methods.process_data import get_csv
from data_analysis.helper_methods.qq_plot import create_qq_plot
from data_analysis.helper_methods.shapiro_wilk_test import shapiro_test
from data_analysis.helper_methods.wilcoxon_test import print_wilcoxon_test

naive_no_heuristic_n5_file = "data_files/naive_heuristics/naive_n5_no_heuristic.csv"  # naive model, n = 5, experiment_5_instances, no minimum-black-squares heuristic
naive_max_heuristic_n5_file = "data_files/naive_heuristics/naive_n5_max_heuristic.csv"  # naive model,      n = 5, experiment_5_instances
naive_min_heuristic_n5_file = "data_files/naive_heuristics/naive_n5_min_heuristic.csv"  # naive model,      n = 5, experiment_5_instances

naive_no_heuristic_n10_file = "data_files/naive_heuristics/naive_n10_no_heuristic.csv"
naive_max_heuristic_n10_file = "data_files/naive_heuristics/naive_n10_max_heuristic.csv"
naive_min_heuristic_n10_file = "data_files/naive_heuristics/naive_n10_min_heuristic.csv"

naive_no_heuristic_n5_csv = get_csv(naive_no_heuristic_n5_file)
naive_max_heuristic_n5_csv = get_csv(naive_max_heuristic_n5_file)
naive_min_heuristic_n5_csv = get_csv(naive_min_heuristic_n5_file)

naive_no_heuristic_n10_csv = get_csv(naive_no_heuristic_n10_file)
naive_max_heuristic_n10_csv = get_csv(naive_max_heuristic_n10_file)
naive_min_heuristic_n10_csv = get_csv(naive_min_heuristic_n10_file)


def heuristic_tests():
    print("\n########################### Describe Naive Heuristics: ###########################")
    # print("No heuristics n = 5:", print_descriptive_statistics(naive_no_heuristic_n5_csv))
    # print("Min heuristics n = 5:", print_descriptive_statistics(naive_min_heuristic_n5_csv))
    # print("Max heuristics n = 5:", print_descriptive_statistics(naive_max_heuristic_n5_csv))

    print("No heuristics n = 10:", print_descriptive_statistics(naive_no_heuristic_n10_csv))
    print("Min heuristics n = 10:", print_descriptive_statistics(naive_min_heuristic_n10_csv))
    print("Max heuristics n = 10:", print_descriptive_statistics(naive_max_heuristic_n10_csv))


    print("\n########################### Shapiro Wilk test optimised naive: ###########################")
    # shapiro_test(naive_no_heuristic_n5_csv)
    # shapiro_test(naive_min_heuristic_n5_csv)
    # shapiro_test(naive_max_heuristic_n5_csv)
    shapiro_test(naive_no_heuristic_n10_csv)
    shapiro_test(naive_min_heuristic_n10_csv)
    shapiro_test(naive_max_heuristic_n10_csv)


    print("\n########################### QQ plots: ###########################")
    create_qq_plot(naive_no_heuristic_n5_csv)
    pylab.savefig("figures/qq-plot1.svg")
    create_qq_plot(naive_min_heuristic_n5_csv)
    pylab.savefig("figures/qq-plot2.svg")
    create_qq_plot(naive_max_heuristic_n5_csv)
    # pylab.savefig("figures/qq-plot3.png")
    print("Non-parametric")

    print("\n########################### Compare Variances: ###########################")
    # bartlett_test_3(naive_no_heuristic_n5_csv, naive_max_heuristic_n5_csv, naive_min_heuristic_n5_csv)
    bartlett_test_3(naive_no_heuristic_n10_csv, naive_min_heuristic_n10_csv, naive_max_heuristic_n10_csv)
    print("So variances differ")

    print("\n########################### Friedman Chi-squared test n = 10: ###########################")
    print(stats.friedmanchisquare(naive_no_heuristic_n10_csv['cpu time'], naive_min_heuristic_n10_csv['cpu time'],
                                  naive_max_heuristic_n10_csv['cpu time']))
    print("So there is a difference between the algorithms")


    # print("\n########################### Pair-wise Wilcoxon n = 5: ###########################")
    # print("None vs min:", print_wilcoxon_test(naive_no_heuristic_n5_csv, naive_min_heuristic_n5_csv))
    # print("None vs max:", print_wilcoxon_test(naive_no_heuristic_n5_csv, naive_max_heuristic_n5_csv, alternative='less'))
    # print("Min vs max:", print_wilcoxon_test(naive_min_heuristic_n5_csv, naive_max_heuristic_n5_csv, alternative='less'))


    print("\n########################### Pair-wise Wilcoxon n = 10: ###########################")
    print("None vs min:", print_wilcoxon_test(naive_no_heuristic_n10_csv, naive_min_heuristic_n10_csv, alternative='greater'))
    print("None vs max:", print_wilcoxon_test(naive_no_heuristic_n10_csv, naive_max_heuristic_n10_csv, alternative='less'))
    print("Min vs max:", print_wilcoxon_test(naive_min_heuristic_n10_csv, naive_max_heuristic_n10_csv, alternative='less'))