from data_analysis.helper_methods.descriptive_statistics import print_descriptive_statistics
from data_analysis.helper_methods.wilcoxon_test import print_wilcoxon_test
from data_analysis.retrieve_data import naive_files, duplicates_files

def naive_vs_duplicates_test():
    print("\n########################### Describe Naive Heuristics: ###########################")
    print("Optimised naive:", print_descriptive_statistics(naive_files["base"]))
    print("Duplicates:", print_descriptive_statistics(duplicates_files["base"]))

    print("\n########################### Pair-wise Wilcoxon: ###########################")
    print("Naive vs Duplicates:", print_wilcoxon_test(naive_files["base"], duplicates_files["base"], alternative='less'))
