import scipy.stats as stats

# Performs a spearman test on the given data
# Expects the csv data of an experiment which needs to contain a 'cpu time' column which holds all the
# solving time for each instance, and another column with the name sent here as attribute, which is what
# the spearman tries to relate to solving time.
def spearman(csv, attribute):
    # csv = remove_outliers_csv(csv)
    attribute_array = csv[attribute]
    cpu_time = csv['cpu time']

    return stats.spearmanr(attribute_array, cpu_time)

def print_spearman(csv, attribute):
    res = spearman(csv, attribute)

    return "\nRho: {}\np-value: {}\n".format(res.statistic, res.pvalue)