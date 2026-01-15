import statsmodels.api as sm
import pylab

def create_qq_plot(csv1):
    sm.qqplot(csv1['cpu time'], line='45')
    # pylab.show()
