from scipy import stats
import math


def wilcoxon_test(csv1, csv2, alternative='two-sided'):
    # data1, data2 = remove_outliers_two_arrays(csv1['cpu time'], csv2['cpu time'])
    data1, data2 = csv1['cpu time'], csv2['cpu time']
    return stats.wilcoxon(data1, data2, alternative=alternative, method='asymptotic')

# Method for pretty printing t-test data
def print_wilcoxon_test(csv1, csv2, alternative='two-sided'):
    stat = wilcoxon_test(csv1, csv2, alternative=alternative)
    return ("\nZ-value: {}\nr: {}\np-value: {}\n"
            .format(stat.zstatistic, stat.zstatistic/math.sqrt(1000), stat.pvalue))
