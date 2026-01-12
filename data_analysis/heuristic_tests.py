import pylab
import scipy.stats as stats

from data_analysis.helper_methods.bartlett_test import bartlett_test_3
from data_analysis.helper_methods.descriptive_statistics import print_descriptive_statistics
from data_analysis.helper_methods.qq_plot import create_qq_plot
from data_analysis.helper_methods.shapiro_wilk_test import shapiro_test
from data_analysis.helper_methods.wilcoxon_test import print_wilcoxon_test
from data_analysis.retrieve_data import naive_files


def heuristic_tests():
    print("\n########################### Describe Naive Heuristics: ###########################")

    print("No heuristics:", print_descriptive_statistics(naive_files["no heuristic"]))
    print("Min heuristics:", print_descriptive_statistics(naive_files["min heuristic"]))
    print("Max heuristics:", print_descriptive_statistics(naive_files["max heuristic"]))


    print("\n########################### Shapiro Wilk test optimised naive: ###########################")
    shapiro_test(naive_files["no heuristic"])
    shapiro_test(naive_files["min heuristic"])
    shapiro_test(naive_files["max heuristic"])


    print("\n########################### QQ plots: ###########################")
    create_qq_plot(naive_files["no heuristic"])
    pylab.savefig("figures/qq-plot1.svg")
    create_qq_plot(naive_files["min heuristic"])
    pylab.savefig("figures/qq-plot2.svg")
    create_qq_plot(naive_files["max heuristic"])
    # pylab.savefig("figures/qq-plot3.png")
    print("Non-parametric")

    print("\n########################### Compare Variances: ###########################")
    bartlett_test_3(naive_files["no heuristic"], naive_files["min heuristic"], naive_files["max heuristic"])
    print("So variances differ")

    print("\n########################### Friedman Chi-squared test n = 10: ###########################")
    print(stats.friedmanchisquare(naive_files["no heuristic"]['cpu time'], naive_files["min heuristic"]['cpu time'],
                                  naive_files["max heuristic"]['cpu time']))
    print("So there is a difference between the algorithms")


    print("\n########################### Pair-wise Wilcoxon n = 10: ###########################")
    print("None vs min:", print_wilcoxon_test(naive_files["no heuristic"], naive_files["min heuristic"], alternative='greater'))
    print("None vs max:", print_wilcoxon_test(naive_files["no heuristic"], naive_files["max heuristic"], alternative='less'))
    print("Min vs max:", print_wilcoxon_test(naive_files["min heuristic"], naive_files["max heuristic"], alternative='less'))
