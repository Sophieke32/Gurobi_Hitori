import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


# Generates a boxplot of the given data. Does not show the boxplot, this has to be done with plt.show()
def show_boxplot(data):
    plt.boxplot(data)
    plt.title('CPU_time (s)')


# Generates a histogram of the given data. Does not show the histogram, this has to be done with plt.show()
def show_histogram(data):
    plt.hist(data, 100, range=(data.min(), data.max()))
    plt.title('CPU_time (s)')


# Removes the outliers of an array of data
# Outliers are defined as values whose absolute z-score is larger than 3
def remove_outliers(data):
    z = np.abs(stats.zscore(data))

    return data[(z < 3)]


# Function to remove the outliers of 2 arrays of data.
# Outliers are defined as values whose absolute z-score is larger than 3
# This function assumes that the two arrays of data are based on the same problem instances and
# as a result are the exact same shape
def remove_outliers_two_arrays(data1, data2):
    z1 = np.abs(stats.zscore(data1))
    z2 = np.abs(stats.zscore(data2))

    z_combined = np.logical_and(z1 < 3, z2 < 3)

    return data1[z_combined], data2[z_combined]


# Performs a t-test on the given data
# Expects the csv data of two experiments. They need to be run on the same problem instances
# and the csv data needs to contain a 'cpu time' column which holds the solving time for each instance
def t_test(csv1, csv2):
    data1, data2 = remove_outliers_two_arrays(csv1['cpu time'], csv2['cpu time'])
    print(stats.ttest_rel(data1, data2))


# Performs a spearman test on the given data
# Expects the csv data of an experiment which needs to contain a 'cpu time' column which holds all the
# solving time for each instance, and another column with the name sent here as attribute, which is what
# the spearman tries to relate to solving time.
def spearman(csv, attribute):
    number_of_cycles = csv[attribute]
    cpu_time = csv['cpu time']

    print(stats.spearmanr(number_of_cycles, cpu_time))

def get_csv(file):
    return np.loadtxt(file, delimiter=',', skiprows=1,
        dtype={'names': ('instance', 'n', 'number of cycles', 'covered squares', 'cpu time', 'solution found'),
            'formats': ('S30', 'i4', 'i4', 'i4', 'f4', 'S1')})

def main():
    file1 = "data_files/duplicates_n5_experiment_5_instances.csv" # duplicates model, n = 5, experiment_5_instances
    file2 = "data_files/naive_n5_experiment_5_instances.csv"      # naive model,      n = 5, experiment_5_instances

    # file3 = "data_files/duplicates_n10_experiment_10_instances.csv" # duplicates model, n = 10, experiment_10_instances
    # file4 = "data_files/naive_n5_experiment_5_instances_no_heuristic.csv" # naive model, n = 5, experiment_5_instances, no minimum-black-squares heuristic

    csv1 = get_csv(file1)
    csv2 = get_csv(file2)
    # csv3 = get_csv(file3)
    # csv4 = get_csv(file4)


    # t_test(csv1, csv2) # Compare duplicates and naive model
    # t_test(csv1, csv4) # Compare duplicates and naive model without heuristic

    # spearman(csv1, 'number of cycles') # Check effect of number of cycles on duplicates
    # spearman(csv3, 'number of cycles') # Check effect of number of cycles on duplicates
    # spearman(csv1, 'covered squares') # Check effect of number of covered tiles on duplicates
    # spearman(csv3, 'covered squares') # Check effect of number of covered tiles on duplicates, n = 10
    # spearman(csv2, 'covered squares') # Check effect of number of covered tiles on duplicates
    # spearman(csv4, 'covered squares') # Check effect of number of covered tiles on duplicates, no heuristic


if __name__ == "__main__":
    main()