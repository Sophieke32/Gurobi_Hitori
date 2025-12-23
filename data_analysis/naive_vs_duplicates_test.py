from data_analysis.helper_methods.descriptive_statistics import print_descriptive_statistics
from data_analysis.helper_methods.process_data import get_csv
from data_analysis.helper_methods.wilcoxon_test import print_wilcoxon_test

duplicates_n10_file = "data_files/duplicates_n10.csv"  # duplicates model, n = 10, experiment_10_instances
optimised_naive_n10_file = "data_files/optimised_naive_n10.csv"  # duplicates model, n = 10, experiment_10_instances

duplicates_n10_csv = get_csv(duplicates_n10_file)
optimised_naive_n10_csv = get_csv(optimised_naive_n10_file)

def naive_vs_duplicates_test():
    print("\n########################### Describe Naive Heuristics: ###########################")
    print("Optimised naive:", print_descriptive_statistics(optimised_naive_n10_csv))
    print("Duplicates:", print_descriptive_statistics(duplicates_n10_csv))

    print("\n########################### Pair-wise Wilcoxon: ###########################")
    print("Naive vs Duplicates:", print_wilcoxon_test(optimised_naive_n10_csv, duplicates_n10_csv, alternative='less'))
