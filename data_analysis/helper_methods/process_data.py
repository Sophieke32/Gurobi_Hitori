import numpy as np
import scipy.stats as stats

# Removes the outliers of an array of data
# Outliers are defined as values whose absolute z-score is larger than 3
def remove_outliers(data):
    z = np.abs(stats.zscore(data))

    return data[(z < 3)]

def remove_outliers_csv(csv):
    z = np.abs(stats.zscore(csv['cpu time']))

    return csv[(z < 3)]

# Function to remove the outliers of 2 arrays of data.
# Outliers are defined as values whose absolute z-score is larger than 3
# This function assumes that the two arrays of data are based on the same problem instances and
# as a result are the exact same shape
def remove_outliers_two_arrays(data1, data2):
    z1 = np.abs(stats.zscore(data1))
    z2 = np.abs(stats.zscore(data2))

    z_combined = np.logical_and(z1 < 3, z2 < 3)

    return data1[z_combined], data2[z_combined]

# Gets data from a csv file
def get_csv(file):
    return np.loadtxt(file, delimiter=',', skiprows=1,
        dtype={'names': ("instance", "n", "cpu time", "duplicates time (s)",
                         "graph time (s)", "time spent on optimisations (s)",
                         "number_of_cycles",
                         "number_of_duplicates", "number_of_covered_tiles",
                         "corner_check_hits", "edge_pairs_hits",
                         "pairs_isolation_hits", "sandwich_pairs_hits",
                         "sandwich_triple_hits",
                         ),
            'formats': ('S30', 'i4', 'f4', 'f4', 'f4', 'f4', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4', 'i4')})

def get_csv_small(file):
    return np.loadtxt(file, delimiter=',', skiprows=1,
                      dtype={'names': ("instance", "n", "cpu time"),
                             'formats': ('S30', 'i4', 'f4')})
