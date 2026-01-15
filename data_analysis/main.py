from data_analysis.connected_algorithms_tests import connected_algorithms_tests
from data_analysis.descriptive_statistics import descriptive_statistics
from data_analysis.generate_graphs import generate_graphs
from data_analysis.heuristic_tests import heuristic_tests
from data_analysis.hitori_properties_tests import hitori_properties_tests
from data_analysis.naive_vs_duplicates_test import compare_models_test
from data_analysis.optimisation_rules_tests import optimisation_rules_tests


def main():
    verbose = False
    descriptive_statistics()
    # heuristic_tests(verbose=verbose)
    # connected_algorithms_tests(verbose=verbose)
    compare_models_test(verbose=verbose)
    optimisation_rules_tests(verbose=verbose)
    hitori_properties_tests(verbose=verbose)

    generate_graphs(generate_for_poster=False)

if __name__ == "__main__":
    main()
