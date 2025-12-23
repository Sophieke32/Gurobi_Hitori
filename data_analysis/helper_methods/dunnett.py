import scipy.stats as stats

# The first is assumed to be the control group
def dunnett_test(csv1, csv2, csv3):
    print(stats.dunnett(csv2['cpu time'], csv3['cpu time'], control=csv1['cpu time']))