from math import sqrt
from statistics import stdev, mean
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

from data_analysis.save_plot_naive_vs_duplicates import save_plot_naive_vs_duplicates
from data_analysis.save_boxplots_covered_vs_time import save_boxplots_covered_vs_time
from data_analysis.save_scatter_cycles_vs_time import save_scatter_cycles_vs_time
from data_analysis.save_boxplot_two_models import save_boxplot_two_models


# Generates a boxplot of the given data. Does not show the boxplot, this has to be done with plt.show()
def show_boxplot(data):
    plt.boxplot(data)
    plt.title('CPU_time (s)')


# Generates a histogram of the given data. Does not show the histogram, this has to be done with plt.show()
def show_histogram(data):
    plt.hist(data, 100, range=(data.min(), data.max()))
    plt.title('CPU_time (s)')


# Performs a t-test on the given data
# Expects the csv data of two experiments. They need to be run on the same problem instances
# and the csv data needs to contain a 'cpu time' column which holds the solving time for each instance
def t_test(csv1, csv2):
    # data1, data2 = remove_outliers_two_arrays(csv1['cpu time'], csv2['cpu time'])
    data1, data2 = csv1['cpu time'], csv2['cpu time']
    return stats.ttest_ind(data1, data2, equal_var=False)

# Strength of the t-test effect
def cohens_d(csv1, csv2):
    # data1, data2 = remove_outliers_two_arrays(csv1['cpu time'], csv2['cpu time'])
    data1, data2 = csv1['cpu time'], csv2['cpu time']
    return (mean(data1) - mean(data2)) / (sqrt((stdev(data1) ** 2 + stdev(data2) ** 2) / 2))

# Method for pretty printing t-test data
def print_t_test(csv1, csv2):
    stat = t_test(csv1, csv2)
    return "\nT-score: {}\np-value: {}\ndf: {}\nCohen's d: {}\n".format(stat.statistic, stat.pvalue, stat.df, cohens_d(csv1, csv2))

# Performs a spearman test on the given data
# Expects the csv data of an experiment which needs to contain a 'cpu time' column which holds all the
# solving time for each instance, and another column with the name sent here as attribute, which is what
# the spearman tries to relate to solving time.
def spearman(csv, attribute):
    # csv = remove_outliers_csv(csv)
    attribute_array = csv[attribute]
    cpu_time = csv['cpu time']

    return stats.spearmanr(attribute_array, cpu_time)

# Gets data from a csv file
def get_csv(file):
    return np.loadtxt(file, delimiter=',', skiprows=1,
        dtype={'names': ('instance', 'n', 'number of cycles', 'covered squares', 'cpu time', 'solution found'),
            'formats': ('S30', 'i4', 'i4', 'i4', 'f4', 'S1')})

# Pretty prints descriptive statistics
def print_descriptive_statistics(csv):
    # desc_stat = stats.describe(remove_outliers(csv['cpu time']))
    desc_stat = stats.describe(csv['cpu time'])

    return "\nMean: {}\nVariance: {}\n".format(desc_stat[2], desc_stat[3])

# Printing all descriptive statistics
def print_all_descriptive_statistics(csvs):
    print("Descriptive statistics duplicates n = 5:", print_descriptive_statistics(csvs[0]))
    print("Descriptive statistics duplicates n = 10:", print_descriptive_statistics(csvs[1]))

    print("Descriptive statistics naive no heuristic n = 5:", print_descriptive_statistics(csvs[2]))
    print("Descriptive statistics naive max heuristic n = 5:", print_descriptive_statistics(csvs[3]))
    print("Descriptive statistics naive min heuristic n = 5:", print_descriptive_statistics(csvs[4]))
    print("Descriptive statistics naive min heuristic n = 10:", print_descriptive_statistics(csvs[5]))


def main():
    #################################
    #           Load Files          #
    #################################

    ### Base Cases
    duplicates_n5_file = "data_files/duplicates_n5.csv"  # duplicates model, n = 5, experiment_5_instances
    duplicates_n10_file = "data_files/duplicates_n10.csv"  # duplicates model, n = 10, experiment_10_instances
    naive_n5_file = "data_files/naive_n5.csv"  # duplicates model, n = 10, experiment_10_instances
    naive_n10_file = "data_files/naive_n10.csv"  # duplicates model, n = 10, experiment_10_instances
    optimised_naive_n5_file = "data_files/optimised_naive_n5.csv"  # duplicates model, n = 10, experiment_10_instances
    optimised_naive_n10_file = "data_files/optimised_naive_n10.csv"  # duplicates model, n = 10, experiment_10_instances

    duplicates_n5_csv = get_csv(duplicates_n5_file)
    duplicates_n10_csv = get_csv(duplicates_n10_file)
    naive_n5_csv = get_csv(naive_n5_file)
    naive_n10_csv = get_csv(naive_n10_file)
    optimised_naive_n5_csv = get_csv(optimised_naive_n5_file)
    optimised_naive_n10_csv = get_csv(optimised_naive_n10_file)


    ### Naive Heuristics
    naive_no_heuristic_n5_file = "data_files/naive_heuristics/naive_n5_no_heuristic.csv"  # naive model, n = 5, experiment_5_instances, no minimum-black-squares heuristic
    naive_max_heuristic_n5_file = "data_files/naive_heuristics/naive_n5_max_heuristic.csv"  # naive model,      n = 5, experiment_5_instances
    naive_min_heuristic_n5_file = "data_files/naive_heuristics/naive_n5_min_heuristic.csv"  # naive model,      n = 5, experiment_5_instances

    naive_no_heuristic_n5_csv = get_csv(naive_no_heuristic_n5_file)
    naive_max_heuristic_n5_csv = get_csv(naive_max_heuristic_n5_file)
    naive_min_heuristic_n5_csv = get_csv(naive_min_heuristic_n5_file)


    ### Path Checkers
    optimised_naive_path_checker_bfs_file = "data_files/path_checkers/optimised_naive_path_checker_bfs.csv"
    optimised_naive_path_checker_cycles_file = "data_files/path_checkers/optimised_naive_path_checker_cycles.csv"
    optimised_naive_path_checker_cc_file = "data_files/path_checkers/optimised_naive_path_checker_cc.csv"

    optimised_naive_path_checker_bfs_csv = get_csv(optimised_naive_path_checker_bfs_file)
    optimised_naive_path_checker_cycles_csv = get_csv(optimised_naive_path_checker_cycles_file)
    optimised_naive_path_checker_cc_csv = get_csv(optimised_naive_path_checker_cc_file)


    # Redundant Constraints (all are n = 10, BFS, min heuristic)
    optimised_naive_corner_close_file = "data_files/redundant_constraints/optimised_naive_corner_close.csv"
    optimised_naive_corner_checking_file = "data_files/redundant_constraints/optimised_naive_corner_check.csv"
    optimised_naive_sandwiches_file = "data_files/redundant_constraints/optimised_naive_sandwiches.csv"
    optimised_naive_all_file = "data_files/redundant_constraints/optimised_naive_all.csv"

    duplicates_corner_close_file = "data_files/redundant_constraints/duplicates_corner_close.csv"
    duplicates_corner_checking_file = "data_files/redundant_constraints/duplicates_corner_check.csv"
    duplicates_sandwiches_file = "data_files/redundant_constraints/duplicates_sandwiches.csv"
    duplicates_all_file = "data_files/redundant_constraints/duplicates_all.csv"

    optimised_naive_corner_close_csv = get_csv(optimised_naive_corner_close_file)
    optimised_naive_corner_checking_csv = get_csv(optimised_naive_corner_checking_file)
    optimised_naive_sandwiches_csv = get_csv(optimised_naive_sandwiches_file)
    optimised_naive_all_csv = get_csv(optimised_naive_all_file)

    duplicates_corner_close_csv = get_csv(duplicates_corner_close_file)
    duplicates_corner_checking_csv = get_csv(duplicates_corner_checking_file)
    duplicates_sandwiches_csv = get_csv(duplicates_sandwiches_file)
    duplicates_all_csv = get_csv(duplicates_all_file)


    #################################
    #         Generate graphs       #
    #################################

    # generate_for_poster = False

    # save_plot_naive_vs_duplicates(duplicates_n5_csv, naive_min_heuristic_n5_csv, generate_for_poster)
    # save_scatter_cycles_vs_time(duplicates_n10_csv, generate_for_poster)

    # save_boxplots_covered_vs_time(naive_min_heuristic_n5_csv, generate_for_poster, "naive", "Influence of number of covered tiles on naive runtime")
    # save_boxplots_covered_vs_time(duplicates_n10_csv, generate_for_poster, "duplicates", "Influence of number of covered tiles on duplicates runtime")

    # save_boxplot_two_models(naive_min_heuristic_n5_csv, duplicates_n5_csv, generate_for_poster)


    #################################
    #       Print Descriptive       #
    #################################

    print_descriptive = False

    if print_descriptive:
        ### Base Cases
        print("\n############################## Describe base cases: ##############################")
        print("Duplicates n = 5", print_descriptive_statistics(duplicates_n5_csv))
        print("Naive n = 5", print_descriptive_statistics(naive_n5_csv))
        print("Optimised naive n = 5", print_descriptive_statistics(optimised_naive_n5_csv))
        print("Duplicates n = 10", print_descriptive_statistics(duplicates_n10_csv))
        print("Naive n = 10", print_descriptive_statistics(naive_n10_csv))
        print("Optimised naive n = 10", print_descriptive_statistics(optimised_naive_n10_csv))


        ### Naive Heuristics
        print("\n########################### Describe Naive Heuristics: ###########################")
        print("No heuristics:", print_descriptive_statistics(naive_no_heuristic_n5_csv))
        print("Min heuristics:", print_descriptive_statistics(naive_min_heuristic_n5_csv))
        print("Max heuristics:", print_descriptive_statistics(naive_max_heuristic_n5_csv))


        ### Path Checkers
        print("\n################################# Path Checkers: #################################")
        print("Optimised naive BFS:", print_descriptive_statistics(optimised_naive_path_checker_bfs_csv))
        print("Optimised naive cycles:", print_descriptive_statistics(optimised_naive_path_checker_cycles_csv))
        print("Optimised naive connected components:", print_descriptive_statistics(optimised_naive_path_checker_cc_csv))


        # Redundant Constraints (all are n = 10, BFS, min heuristic)
        print("\n############################# Redundant Constraints: #############################")
        print("Optimised naive corner close:", print_descriptive_statistics(optimised_naive_corner_close_csv))
        print("Optimised naive corner checking:", print_descriptive_statistics(optimised_naive_corner_checking_csv))
        print("Optimised naive sandwiches:", print_descriptive_statistics(optimised_naive_sandwiches_csv))
        print("Optimised naive all:", print_descriptive_statistics(optimised_naive_all_csv))
        print()
        print("Duplicates corner close:", print_descriptive_statistics(duplicates_corner_close_csv))
        print("Duplicates corner checking:", print_descriptive_statistics(duplicates_corner_checking_csv))
        print("Duplicates sandwiches:", print_descriptive_statistics(duplicates_sandwiches_csv))
        print("Duplicates all:", print_descriptive_statistics(duplicates_all_csv))

    #################################
    #         Print t-tests         #
    #################################

    print_t_test_data = True

    if print_t_test_data:
        ### Base Cases
        print("\n############################### t-test base cases: ###############################")
        print()

    # print("### t-test: Compare BFS and cycles ###",
    #       print_t_test(optimised_naive_path_checker_bfs_csv, optimised_naive_path_checker_cycles_csv))
    # print("### t-test: Compare BFS and cc ###",
    #       print_t_test(optimised_naive_path_checker_bfs_csv, optimised_naive_path_checker_cc_csv))
    # print("### t-test: Compare optimised naive with/without corner close ###",
    #       print_t_test(optimised_naive_n10_csv, optimised_naive_n10_corner_close_csv))
    # print("### t-test: Compare duplicates with duplicates + corner checking ###",
    #       print_t_test(naive_min_heuristic_n10_csv, naive_n10_with_corner_close_csv))
    # print("### t-test: Compare duplicates with duplicates + corner checking ###",
    #       print_t_test(duplicates_n10_csv, duplicates_n10_with_corner_close_csv))
    # print("### t-test: Compare naive no heuristic and naive with min heuristic ###", print_t_test(naive_no_heuristic_n5_csv, naive_min_heuristic_n5_csv))
    # print("### t-test: Compare naive no heuristic and naive with max heuristic ###", print_t_test(naive_no_heuristic_n5_csv, naive_max_heuristic_n5_csv))
    # print("### t-test: Compare duplicates and naive with min heuristic ###", print_t_test(naive_min_heuristic_n10_csv, duplicates_n10_csv))

    # print()
    # print("Spearman: Effect of number of cycles on duplicates (n=5)", spearman(duplicates_n5_csv, 'number of cycles'))
    # print("Spearman: Effect of number of cycles on duplicates (n=10)", spearman(duplicates_n10_csv, 'number of cycles'))
    # print("Spearman: Effect of number of covered tiles on duplicates (n=5)", spearman(duplicates_n5_csv, 'covered squares'))
    # print("Spearman: Effect of number of covered tiles on duplicates (n=10)", spearman(duplicates_n10_csv, 'covered squares'))
    # print("Spearman: Effect of number of covered tiles on naive (n=5)", spearman(naive_no_heuristic_n5_csv, 'covered squares'))
    # print("Spearman: Effect of number of covered tiles on naive minimise (n=10)", spearman(naive_min_heuristic_n10_csv, 'covered squares'))
    # print("Spearman: Effect of number of covered tiles on naive with heuristic", spearman(naive_min_heuristic_csv, 'covered squares'))


if __name__ == "__main__":
    main()
