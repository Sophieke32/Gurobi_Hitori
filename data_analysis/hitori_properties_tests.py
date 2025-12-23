from data_analysis.helper_methods.process_data import get_csv
from data_analysis.helper_methods.spearman_test import print_spearman

duplicates_n10_file = "data_files/duplicates_n10.csv"  # duplicates model, n = 10, experiment_10_instances
optimised_naive_n10_file = "data_files/optimised_naive_n10.csv"  # duplicates model, n = 10, experiment_10_instances
naive_n10_file = "data_files/naive_n10.csv"  # duplicates model, n = 10, experiment_10_instances

naive_n10_csv = get_csv(naive_n10_file)
duplicates_n10_csv = get_csv(duplicates_n10_file)
optimised_naive_n10_csv = get_csv(optimised_naive_n10_file)

def hitori_properties_tests():
    print("Spearman: Effect of number of covered tiles on non-optimised naive (n=10)",
          print_spearman(naive_n10_csv, 'covered squares'))
    print("Spearman: Effect of number of covered tiles on optimised naive (n=10)",
          print_spearman(optimised_naive_n10_csv, 'covered squares'))
    print("Spearman: Effect of number of covered tiles on duplicates (n=10)",
          print_spearman(duplicates_n10_csv, 'covered squares'))
    print("Spearman: Effect of number of cycles on duplicates (n=10)",
          print_spearman(duplicates_n10_csv, 'number of cycles'))
