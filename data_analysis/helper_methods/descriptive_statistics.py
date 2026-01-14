import scipy.stats as stats


# Pretty prints descriptive statistics
def print_descriptive_statistics(csv):
    # desc_stat = stats.describe(remove_outliers(csv['cpu time']))
    desc_stat = stats.describe(csv['cpu time'])

    return "\nMean: {}\nVariance: {}\n".format(desc_stat[2], desc_stat[3])

def get_descriptive_statistics(csv, attribute):
    return stats.describe(csv[attribute])