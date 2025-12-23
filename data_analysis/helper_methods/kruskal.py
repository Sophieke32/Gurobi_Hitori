import scipy.stats as stats

def kruskal_wallis(csv1, csv2, csv3):
    return stats.kruskal(csv1['cpu time'], csv2['cpu time'], csv3['cpu time'])

def print_kruskal_wallis(csv1, csv2, csv3):
    stat = kruskal_wallis(csv1, csv2, csv3)
    return "\nH (or Chi^2)-score: {}\np-value: {}\n".format(stat[0], stat[1])