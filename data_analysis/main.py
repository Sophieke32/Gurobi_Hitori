import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

from data_analysis.helper_methods.remove_outliers import remove_outliers_two_arrays
from data_analysis.save_plot_naive_vs_duplicates import save_plot_naive_vs_duplicates
from data_analysis.save_scatter_cycles_vs_time import save_scatter_cycles_vs_time


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
    data1, data2 = remove_outliers_two_arrays(csv1['cpu time'], csv2['cpu time'])
    return stats.ttest_rel(data1, data2)


# Performs a spearman test on the given data
# Expects the csv data of an experiment which needs to contain a 'cpu time' column which holds all the
# solving time for each instance, and another column with the name sent here as attribute, which is what
# the spearman tries to relate to solving time.
def spearman(csv, attribute):
    number_of_cycles = csv[attribute]
    cpu_time = csv['cpu time']

    return stats.spearmanr(number_of_cycles, cpu_time)

def get_csv(file):
    return np.loadtxt(file, delimiter=',', skiprows=1,
        dtype={'names': ('instance', 'n', 'number of cycles', 'covered squares', 'cpu time', 'solution found'),
            'formats': ('S30', 'i4', 'i4', 'i4', 'f4', 'S1')})


def main():
    file1 = "data_files/duplicates_n5_experiment_5_instances.csv" # duplicates model, n = 5, experiment_5_instances
    file2 = "data_files/naive_n5_experiment_5_instances.csv" # naive model, n = 5, experiment_5_instances, no minimum-black-squares heuristic
    file3 = "data_files/naive_n5_experiment_5_instances_with_heuristic.csv"      # naive model,      n = 5, experiment_5_instances

    file4 = "data_files/duplicates_n10_experiment_10_instances.csv" # duplicates model, n = 10, experiment_10_instances

    csv1 = get_csv(file1)
    csv2 = get_csv(file2)
    csv3 = get_csv(file3)
    csv4 = get_csv(file4)

    # save_plot_naive_vs_duplicates(csv1, csv2)
    # save_scatter_cycles_vs_time(csv4)




    print("t-test: Compare duplicates and naive", t_test(csv1, csv2))
    print("t-test: Compare duplicates and naive with heuristic", t_test(csv1, csv3))

    print("Spearman: Effect of number of cycles on duplicates (n=5)", spearman(csv1, 'number of cycles'))
    print("Spearman: Effect of number of cycles on duplicates (n=10)", spearman(csv4, 'number of cycles'))
    print("Spearman: Effect of number of covered tiles on duplicates (n=5)", spearman(csv1, 'covered squares'))
    print("Spearman: Effect of number of covered tiles on duplicates (n=10)", spearman(csv4, 'covered squares'))
    print("Spearman: Effect of number of covered tiles on naive", spearman(csv2, 'covered squares'))
    print("Spearman: Effect of number of covered tiles on naive with heuristic", spearman(csv3, 'covered squares'))


if __name__ == "__main__":
    main()