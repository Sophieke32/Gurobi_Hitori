# from data_analysis.connected_algorithms_tests import connected_algorithms_tests
from numpy import mean, median

from data_analysis.helper_methods.descriptive_statistics import print_descriptive_statistics
from data_analysis.heuristic_tests import heuristic_tests
from data_analysis.helper_methods.process_data import get_csv
from data_analysis.helper_methods.spearman_test import print_spearman
from data_analysis.helper_methods.t_tests import print_t_test
from data_analysis.hitori_properties_tests import hitori_properties_tests
from data_analysis.naive_vs_duplicates_test import naive_vs_duplicates_test
from data_analysis.optimisation_rules_tests import optimisation_rules_tests
from data_analysis.retrieve_data import naive_files, duplicates_files
from data_analysis.visualisation_methods.save_boxplot_two_models import save_boxplot_two_models
from data_analysis.visualisation_methods.save_boxplots_covered_vs_time import save_boxplots_covered_vs_time
from data_analysis.visualisation_methods.save_plot_naive_vs_duplicates import save_plot_naive_vs_duplicates
from data_analysis.visualisation_methods.save_scatter_cycles_vs_time import save_scatter_cycles_vs_time
from data_analysis.visualisation_methods.save_survival_plot import save_survival_plot


def main():
    #################################
    #       Print Descriptive       #
    #################################
    # heuristic_tests()
    # connected_algorithms_tests()
    # naive_vs_duplicates_test()
    # optimisation_rules_tests()
    hitori_properties_tests()

    print("share of duplicates time", mean(duplicates_files["base"]['duplicates time (s)'] / duplicates_files["base"]['cpu time']))
    print("share of graph time", median(duplicates_files["base"]['graph time (s)'] / duplicates_files["base"]['cpu time']))


    # print(sum(naive_files["base"]['cpu time']))
    # print(sum(duplicates_files["base"]['cpu time']))

    # print("max naive", sum(sorted(naive_files["base"]['cpu time'])[990:]))
    # print("max duplicates", sorted(duplicates_files["base"]['cpu time']))

    #################################
    #         Generate graphs       #
    #################################

    generate_for_poster = False

    # save_survival_plot(naive_files["base"], duplicates_files["base"], generate_for_poster)
    #
    # save_plot_naive_vs_duplicates(duplicates_files["base"], naive_files["base"], generate_for_poster)
    # save_scatter_cycles_vs_time(duplicates_files["base"], generate_for_poster)
    #
    # save_boxplots_covered_vs_time(naive_files["base"], generate_for_poster, "naive", "Influence of number of covered tiles on naive runtime")
    # save_boxplots_covered_vs_time(duplicates_files["base"], generate_for_poster, "duplicates", "Influence of number of covered tiles on duplicates runtime")
    #
    # save_boxplot_two_models(naive_files["base"], duplicates_files["base"], generate_for_poster)

    #################################
    #       Print Descriptive       #
    #################################

    # descriptive_statistics()

    #################################
    #   Print comparative studies   #
    #################################

    # t_tests()

    #################################
    #     Print Spearman's tests    #
    #################################

    # spearman_tests()


def descriptive_statistics():
    ### Base Cases
    print("\n############################## Describe base cases: ##############################")
    # # print("Duplicates n = 5", print_descriptive_statistics(duplicates_n5_csv))
    # # print("Naive n = 5", print_descriptive_statistics(naive_n5_csv))
    # # print("Optimised naive n = 5", print_descriptive_statistics(optimised_naive_n5_csv))
    # print("Duplicates n = 10", print_descriptive_statistics(duplicates_n10_csv))
    # print("Naive n = 10", print_descriptive_statistics(naive_n10_csv))
    # print("Optimised naive n = 10", print_descriptive_statistics(optimised_naive_n10_csv))

    ### Naive Heuristics
    # print("\n########################### Describe Naive Heuristics: ###########################")
    # print("No heuristics n = 5:", print_descriptive_statistics(naive_no_heuristic_n5_csv))
    # print("Min heuristics n = 5:", print_descriptive_statistics(naive_min_heuristic_n5_csv))
    # print("Max heuristics n = 5:", print_descriptive_statistics(naive_max_heuristic_n5_csv))
    #
    # print("No heuristics n = 10:", print_descriptive_statistics(naive_no_heuristic_n10_csv))
    # print("Min heuristics n = 10:", print_descriptive_statistics(naive_min_heuristic_n10_csv))

    ### Path Checkers
    # print("\n################################# Path Checkers: #################################")
    # print("Optimised naive BFS:", print_descriptive_statistics(optimised_naive_path_checker_bfs_csv))
    # print("Optimised naive cycles:", print_descriptive_statistics(optimised_naive_path_checker_cycles_csv))
    # print("Optimised naive connected components:", print_descriptive_statistics(optimised_naive_path_checker_cc_csv))

    # Redundant Constraints (all are n = 10, BFS, min heuristic)
    # print("\n############################# Redundant Constraints: #############################")
    # print("Optimised naive corner close:", print_descriptive_statistics(optimised_naive_corner_close_csv))
    # print("Optimised naive corner checking:", print_descriptive_statistics(optimised_naive_corner_checking_csv))
    # print("Optimised naive sandwiches:", print_descriptive_statistics(optimised_naive_sandwiches_csv))
    # print("Optimised naive edge pairs:", print_descriptive_statistics(optimised_naive_edge_pairs_csv))
    # print("Optimised naive max black", print_descriptive_statistics(optimised_naive_most_blacks_csv))
    # print("Optimised naive least whites", print_descriptive_statistics(optimised_naive_least_whites_csv))
    # print("Optimised naive pair isolation", print_descriptive_statistics(optimised_naive_pair_isolation_csv))
    # print("Optimised naive all:", print_descriptive_statistics(optimised_naive_all_csv))
    # print()
    # print("Duplicates corner close:", print_descriptive_statistics(duplicates_corner_close_csv))
    # print("Duplicates corner checking:", print_descriptive_statistics(duplicates_corner_checking_csv))
    # print("Duplicates sandwiches:", print_descriptive_statistics(duplicates_sandwiches_csv))
    # print("Duplicates edge pairs:", print_descriptive_statistics(duplicates_edge_pairs_csv))
    # print("Duplicates max black", print_descriptive_statistics(duplicates_most_blacks_csv))
    # print("Duplicates least whites", print_descriptive_statistics(duplicates_least_whites_csv))
    # print("Duplicates pair isolation", print_descriptive_statistics(duplicates_pair_isolation_csv))
    # print("Duplicates all:", print_descriptive_statistics(duplicates_all_csv))


def t_tests():
    ### Base Cases
    print("\n############################## t-test base cases: ###############################")
    # print("Naive, Optimised naive - n = 5", print_t_test(naive_n5_csv, optimised_naive_n5_csv))
    # print("Naive, Duplicates - n = 5", print_t_test(naive_n5_csv, duplicates_n5_csv))
    # print("Optimised naive, Duplicates - n = 5", print_t_test(optimised_naive_n5_csv, duplicates_n5_csv))

    # print("Naive, Optimised naive - n = 10", print_t_test(naive_n10_csv, optimised_naive_n10_csv))
    # print("Naive, Duplicates - n = 10", print_t_test(naive_n10_csv, duplicates_n10_csv))
    # print("Optimised naive, Duplicates - n = 10", print_t_test(optimised_naive_n10_csv, duplicates_n10_csv))
    #
    # ### Naive Heuristics
    # print("\n############################ t-test Naive Heuristics: ############################")
    # print("None, Minimise, n = 5", print_t_test(naive_n5_csv, naive_min_heuristic_n5_csv))
    # print("None, Maximise, n = 5", print_t_test(naive_n5_csv, naive_max_heuristic_n5_csv))
    # print("Minimise, Maximise, n = 5", print_t_test(naive_min_heuristic_n5_csv, naive_max_heuristic_n5_csv))
    #
    # print("None, Minimise, n = 10", print_t_test(naive_n10_csv, naive_min_heuristic_n10_csv))
    #
    # ### Path Checkers (all are n = 10, BFS, min heuristic)
    # print("\n############################## t-test Path checkers: #############################")
    # print("DFS vs cycles", print_t_test(optimised_naive_path_checker_bfs_csv, optimised_naive_path_checker_cycles_csv))
    # print("DFS vs connected component",
    #       print_t_test(optimised_naive_path_checker_bfs_csv, optimised_naive_path_checker_cc_csv))
    # print("cycles vs connected component",
    #       print_t_test(optimised_naive_path_checker_cycles_csv, optimised_naive_path_checker_cc_csv))
    #
    # # Redundant Constraints (all are n = 10, BFS, min heuristic)
    # print("\n########################## t-test Redundant constraints: #########################")
    # print("Optimised Naive: Base vs corner close:",
    #       print_t_test(optimised_naive_n10_csv, optimised_naive_corner_close_csv))
    # print("Optimised Naive: Base vs corner check:",
    #       print_t_test(optimised_naive_n10_csv, optimised_naive_corner_checking_csv))
    # print("Optimised Naive: Base vs sandwiches:", print_t_test(optimised_naive_n10_csv, optimised_naive_sandwiches_csv))
    # print("Optimised Naive: Base vs edge pairs:", print_t_test(optimised_naive_n10_csv, optimised_naive_edge_pairs_csv))
    # print("Optimised Naive: Base vs max black:", print_t_test(optimised_naive_n10_csv, optimised_naive_most_blacks_csv))
    # print("Optimised Naive: Base vs least whites:",
    #       print_t_test(optimised_naive_n10_csv, optimised_naive_least_whites_csv))
    # print("Optimised Naive: Base vs pair isolation:",
    #       print_t_test(optimised_naive_n10_csv, optimised_naive_pair_isolation_csv))
    # # print("Optimised Naive: Base vs all:", print_t_test(optimised_naive_n10_csv, optimised_naive_all_csv))
    #
    # print("Duplicates: Base vs corner close:", print_t_test(duplicates_n10_csv, duplicates_corner_close_csv))
    # print("Duplicates: Base vs corner checking:", print_t_test(duplicates_n10_csv, duplicates_corner_checking_csv))
    # print("Duplicates: Base vs sandwiches:", print_t_test(duplicates_n10_csv, duplicates_sandwiches_csv))
    # print("Duplicates: Base vs edge pairs:", print_t_test(duplicates_n10_csv, duplicates_edge_pairs_csv))
    # print("Duplicates: Base vs max black:", print_t_test(duplicates_n10_csv, duplicates_most_blacks_csv))
    # print("Duplicates: Base vs least whites:", print_t_test(duplicates_n10_csv, duplicates_least_whites_csv))
    # print("Duplicates: Base vs pair isolation:", print_t_test(duplicates_n10_csv, duplicates_pair_isolation_csv))
    # print("Duplicates: Base vs all:", print_t_test(duplicates_n10_csv, duplicates_all_csv))


# def spearman_tests():
#     print("Spearman: Effect of number of cycles on duplicates (n=5)",
#           print_spearman(duplicates_n5_csv, 'number of cycles'))
#     print("Spearman: Effect of number of cycles on duplicates (n=10)",
#           print_spearman(duplicates_n10_csv, 'number of cycles'))
#     print("Spearman: Effect of number of covered tiles on naive (n=5)",
#           print_spearman(naive_min_heuristic_n5_csv, 'covered squares'))
#     print("Spearman: Effect of number of covered tiles on optimised naive (n=5)",
#           print_spearman(optimised_naive_n5_csv, 'covered squares'))
#     print("Spearman: Effect of number of covered tiles on duplicates (n=5)",
#           print_spearman(duplicates_n5_csv, 'covered squares'))
#     print("Spearman: Effect of number of covered tiles on naive (n=10)",
#           print_spearman(naive_n10_csv, 'covered squares'))
#     print("Spearman: Effect of number of covered tiles on optimised naive (n=10)",
#           print_spearman(optimised_naive_n10_csv, 'covered squares'))
#     print("Spearman: Effect of number of covered tiles on duplicates (n=10)",
#           print_spearman(duplicates_n10_csv, 'covered squares'))


if __name__ == "__main__":
    main()
