from scipy import stats


def shapiro_test(csv):
    stat = stats.shapiro(csv['cpu time'])
    print("w = {}, p = {}".format(stat.statistic, stat.pvalue))

    if stat.statistic > 0.9: print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")