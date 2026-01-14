import numpy as np
import scipy.stats as stats

def print_permutation_test(csv1, csv2):
    mean_difference = statistic(csv1, csv2)

    if mean_difference < 0:
        stat = stats.permutation_test((csv1, csv2), statistic, n_resamples=9999, permutation_type='samples',
                                      alternative='less')
        return 'less', stat.pvalue
    else:
        stat = stats.permutation_test((csv1, csv2), statistic, n_resamples=9999, permutation_type='samples',
                                      alternative='greater')
        return 'greater', stat.pvalue


def statistic(x, y):
    return np.mean(x) - np.mean(y)
