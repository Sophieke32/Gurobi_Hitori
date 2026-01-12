# import scipy.stats as stats
# import pylab
#
# from data_analysis.helper_methods.bartlett_test import bartlett_test_3, bartlett_test_2
# from data_analysis.helper_methods.descriptive_statistics import print_descriptive_statistics
# from data_analysis.helper_methods.dunnett import dunnett_test
# from data_analysis.helper_methods.kruskal import print_kruskal_wallis
# from data_analysis.helper_methods.process_data import get_csv
# from data_analysis.helper_methods.qq_plot import create_qq_plot
# from data_analysis.helper_methods.shapiro_wilk_test import shapiro_test
# from data_analysis.helper_methods.t_tests import print_t_test
# from data_analysis.helper_methods.wilcoxon_test import print_wilcoxon_test
#
# optimised_naive_path_checker_bfs_file = "data_files/archive/path_checkers/optimised_naive_path_checker_bfs.csv"
# optimised_naive_path_checker_cycles_file = "data_files/archive/path_checkers/optimised_naive_path_checker_cycles.csv"
# optimised_naive_path_checker_cc_file = "data_files/archive/path_checkers/optimised_naive_path_checker_cc.csv"
#
# optimised_naive_path_checker_bfs_csv = get_csv(optimised_naive_path_checker_bfs_file)
# optimised_naive_path_checker_cycles_csv = get_csv(optimised_naive_path_checker_cycles_file)
# optimised_naive_path_checker_cc_csv = get_csv(optimised_naive_path_checker_cc_file)
#
#
# def connected_algorithms_tests():
#     print("\n########################### Describe Naive Heuristics: ###########################")
#     print("Optimised naive BFS:", print_descriptive_statistics(optimised_naive_path_checker_bfs_csv))
#     print("Optimised naive cycles:", print_descriptive_statistics(optimised_naive_path_checker_cycles_csv))
#     print("Optimised naive connected components:", print_descriptive_statistics(optimised_naive_path_checker_cc_csv))
#
#
#     print("\n########################### Shapiro Wilk test optimised naive: ###########################")
#     shapiro_test(optimised_naive_path_checker_bfs_csv)
#     shapiro_test(optimised_naive_path_checker_cycles_csv)
#     shapiro_test(optimised_naive_path_checker_cc_csv)
#
#
#     print("\n########################### QQ plots: ###########################")
#     create_qq_plot(optimised_naive_path_checker_bfs_csv)
#     pylab.savefig("figures/qq-plot3.svg")
#     create_qq_plot(optimised_naive_path_checker_cycles_csv)
#     create_qq_plot(optimised_naive_path_checker_cc_csv)
#     # pylab.show()
#     print("Non-parametric")
#
#     print("\n########################### Compare Variances: ###########################")
#     bartlett_test_3(optimised_naive_path_checker_bfs_csv, optimised_naive_path_checker_cycles_csv, optimised_naive_path_checker_cc_csv)
#     print("So variances the same. Still move to Kruskal-Wallis-H test")
#
#
#
#     print("\n########################### Friedman Chi-squared test: ###########################")
#     print(stats.friedmanchisquare(optimised_naive_path_checker_bfs_csv['cpu time'], optimised_naive_path_checker_cycles_csv['cpu time'],
#                                   optimised_naive_path_checker_cc_csv['cpu time']))
#     print("So there is a difference between the algorithms")
#
#
#     print("\n########################### Pair-wise Wilcoxon: ###########################")
#     # print("BFS vs cycles:", print_wilcoxon_test(optimised_naive_path_checker_bfs_csv, optimised_naive_path_checker_cycles_csv, alternative='greater'))
#     print("BFS vs cycles:", print_wilcoxon_test(optimised_naive_path_checker_bfs_csv, optimised_naive_path_checker_cycles_csv, alternative='less'))
#     print("So BFS values are smaller can cycles values. BFS is faster")
#     # print("BFS vs connected components:", print_wilcoxon_test(optimised_naive_path_checker_bfs_csv, optimised_naive_path_checker_cc_csv, alternative='greater'))
#     print("BFS vs connected components:", print_wilcoxon_test(optimised_naive_path_checker_bfs_csv, optimised_naive_path_checker_cc_csv, alternative='less'))
#     print("So BFS values are smaller than cc values. BFS is faster")
#     print("connected component vs cycles:", print_wilcoxon_test(optimised_naive_path_checker_cc_csv, optimised_naive_path_checker_cycles_csv, alternative='less'))
#     # print("Cycles vs connected components:", print_wilcoxon_test(optimised_naive_path_checker_cycles_csv, optimised_naive_path_checker_cc_csv, alternative='less'))
#     print("So cc values are smaller than cycles values. cc is faster")
#
#     # print("\n########################### Kruskal-Wallis-H test: ###########################")
#     # print(print_kruskal_wallis(optimised_naive_path_checker_bfs_csv, optimised_naive_path_checker_cycles_csv, optimised_naive_path_checker_cc_csv))
#     # print("Hence there is a difference in the groups")
#     #
#     #
#     # print("\n########################### Post-hoc Dunnett test: ###########################")
#     # dunnett_test(optimised_naive_path_checker_bfs_csv, optimised_naive_path_checker_cycles_csv, optimised_naive_path_checker_cc_csv)
