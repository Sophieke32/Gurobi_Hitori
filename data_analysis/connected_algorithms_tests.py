import csv
import pylab

from data_analysis.helper_methods.bartlett_test import bartlett_test_3
from data_analysis.helper_methods.descriptive_statistics import print_descriptive_statistics
from data_analysis.helper_methods.permutation_test import print_permutation_test
from data_analysis.helper_methods.qq_plot import create_qq_plot
from data_analysis.helper_methods.shapiro_wilk_test import shapiro_test
from data_analysis.retrieve_data import naive_files


def connected_algorithms_tests(verbose=False):
    print("Performing connected algorithms tests...")
    if verbose:
        print("\n########################### Describe Naive Heuristics: ###########################")
        print("Optimised naive BFS:", print_descriptive_statistics(naive_files['bfs']))
        print("Optimised naive cycles:", print_descriptive_statistics(naive_files['cycles']))
        print("Optimised naive connected components:", print_descriptive_statistics(naive_files['connected component']))


        print("\n########################### Shapiro Wilk test optimised naive: ###########################")
        shapiro_test(naive_files['bfs'])
        shapiro_test(naive_files['cycles'])
        shapiro_test(naive_files['connected component'])


        print("\n########################### Compare Variances: ###########################")
        bartlett_test_3(naive_files['bfs'], naive_files['cycles'], naive_files['connected component'])
        print("So variances the same. Still move to Kruskal-Wallis-H test")

    ########################### QQ plots: ###########################
    create_qq_plot(naive_files['bfs'])
    pylab.savefig("figures/qq-plot3.svg")
    create_qq_plot(naive_files['cycles'])
    create_qq_plot(naive_files['connected component'])
    # pylab.show()

    ########################### Permutation Test: ###########################
    res = []
    res.append(["bfs", "cycles", print_permutation_test(naive_files['bfs']['cpu time'], naive_files['cycles']['cpu time'])])
    res.append(["bfs", "connected component", print_permutation_test(naive_files['bfs']['cpu time'], naive_files['connected component']['cpu time'])])
    res.append(["cycles", "connected component", print_permutation_test(naive_files['cycles']['cpu time'], naive_files['connected component']['cpu time'])])


    with open("results/connected_algorithms_tests.csv", "w", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["model 1", "model 2", "direction", "p-value"])
        writer.writeheader()

        for i in res:
            if i[2][0] == 'greater':
                writer.writerow({"model 1": i[1], "model 2": i[0], "direction": 'less', "p-value": i[2][1]})
            else:
                writer.writerow({"model 1": i[0], "model 2": i[1], "direction": i[2][0], "p-value": i[2][1]})
