import scipy.stats as stats

def bartlett_test_3(csv1, csv2, csv3):
    print(stats.bartlett(csv1['cpu time'], csv2['cpu time'], csv3['cpu time']))

def bartlett_test_2(csv1, csv2):
    print(stats.bartlett(csv1['cpu time'], csv2['cpu time']))