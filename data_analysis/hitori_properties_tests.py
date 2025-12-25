import numpy as np

from data_analysis.helper_methods.process_data import get_csv
from data_analysis.helper_methods.spearman_test import print_spearman

duplicates_n10_file = "data_files/duplicates_n10.csv"  # duplicates model, n = 10, experiment_10_instances
optimised_naive_n10_file = "data_files/optimised_naive_n10.csv"  # duplicates model, n = 10, experiment_10_instances
naive_n10_file = "data_files/naive_n10.csv"  # duplicates model, n = 10, experiment_10_instances

naive_n10_csv = get_csv(naive_n10_file)
duplicates_n10_csv = get_csv(duplicates_n10_file)
optimised_naive_n10_csv = get_csv(optimised_naive_n10_file)

# Number of duplicates and graph time
graph_time_csv = np.loadtxt("data_files/graph_time_share/duplicates_n10_graph_time_share.csv", delimiter=',', skiprows=1,
        dtype={'names': ('instance', 'n', 'number of cycles', 'covered squares', 'cpu time', 'graph time (s)', 'graph time share (%)', 'solution found'),
            'formats': ('S30', 'i4', 'i4', 'i4', 'f4', 'f4', 'f4', 'S1')})

number_of_duplicates_csv = np.loadtxt("data_files/num_duplicates/duplicates_num_duplicates.csv", delimiter=',', skiprows=1,
        dtype={'names': ('instance', 'n', 'number of cycles', 'covered squares', 'cpu time', 'number of duplicates', 'solution found'),
            'formats': ('S30', 'i4', 'i4', 'i4', 'f4', 'i4', 'S1')})

def hitori_properties_tests():
    print("Spearman: Effect of number of covered tiles on non-optimised naive (n=10)",
          print_spearman(naive_n10_csv, 'covered squares'))
    print("Spearman: Effect of number of covered tiles on optimised naive (n=10)",
          print_spearman(optimised_naive_n10_csv, 'covered squares'))
    print("Spearman: Effect of number of covered tiles on duplicates (n=10)",
          print_spearman(duplicates_n10_csv, 'covered squares'))
    print("Spearman: Effect of number of cycles on duplicates (n=10)",
          print_spearman(duplicates_n10_csv, 'number of cycles'))

    print("Spearman: Effect of graph time on runtime",
          print_spearman(graph_time_csv, 'graph time (s)'))
    print("Spearman: Effect of graph time share on runtime",
          print_spearman(graph_time_csv, 'graph time share (%)'))
    print("Spearman: Effect of num duplicates on runtime",
          print_spearman(number_of_duplicates_csv, 'number of duplicates'))
