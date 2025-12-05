import numpy as np
import scipy.stats as stats

# Removes the outliers of an array of data
# Outliers are defined as values whose absolute z-score is larger than 3
def remove_outliers(data):
    z = np.abs(stats.zscore(data))

    return data[(z < 3)]


# Function to remove the outliers of 2 arrays of data.
# Outliers are defined as values whose absolute z-score is larger than 3
# This function assumes that the two arrays of data are based on the same problem instances and
# as a result are the exact same shape
def remove_outliers_two_arrays(data1, data2):
    z1 = np.abs(stats.zscore(data1))
    z2 = np.abs(stats.zscore(data2))

    z_combined = np.logical_and(z1 < 3, z2 < 3)

    return data1[z_combined], data2[z_combined]