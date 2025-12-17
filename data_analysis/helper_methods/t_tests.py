from math import sqrt
from statistics import stdev, mean
import scipy.stats as stats


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
