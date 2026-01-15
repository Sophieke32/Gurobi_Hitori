import csv

from scipy import stats

from data_analysis.helper_methods.spearman_test import print_spearman, spearman_data, spearman_data_special, \
    print_spearman_special
from data_analysis.retrieve_data import naive_files, duplicates_files, path_files


def hitori_properties_tests(verbose=False):
    if verbose:

        print("Spearman: Effect of number of covered tiles on naive (n=10)",
              print_spearman(naive_files["base"], 'number_of_covered_tiles'))
        print("Spearman: Effect of number of covered tiles on duplicates (n=10)",
              print_spearman(duplicates_files["base"], 'number_of_covered_tiles'))
        print("Spearman: Effect of number of cycles on duplicates (n=10)",
              print_spearman(duplicates_files["base"], 'number_of_cycles'))

        print("Spearman: Effect of graph time on runtime",
              print_spearman(duplicates_files["base"], 'graph time (s)'))
        print("Spearman: Effect of num duplicates on runtime duplicates",
              print_spearman(duplicates_files["base"], 'number_of_duplicates'))
        print("Spearman: Effect of num duplicates on runtime naive",
              print_spearman(naive_files["base"], 'number_of_duplicates'))


        print("##################################################################" +
              "\n#      Checking effect of properties without optimisations       #" +
              "\n##################################################################")

        print("Spearman: Effect of corner checks on runtime naive",
              print_spearman(naive_files["base"], 'corner_check_hits'))
        # print("Spearman: Effect of edge pairs on runtime naive",
        #       print_spearman(naive_files["base"], 'edge_pairs_hits')) No edge pairs whatsoever
        print("Spearman: Effect of pair isolations on runtime naive",
              print_spearman(naive_files["base"], 'pairs_isolation_hits'))
        print("Spearman: Effect of sandwich pairs on runtime naive",
              print_spearman(naive_files["base"], 'sandwich_pairs_hits'))
        print("Spearman: Effect of sandwich triples on runtime naive",
              print_spearman(naive_files["base"], 'sandwich_triple_hits'))

        print("Spearman: Effect of corner checks on runtime duplicates",
              print_spearman(duplicates_files["base"], 'corner_check_hits'))
        print("Spearman: Effect of pair isolations on runtime duplicates",
              print_spearman(duplicates_files["base"], 'pairs_isolation_hits'))
        print("Spearman: Effect of sandwich pairs on runtime duplicates",
              print_spearman(duplicates_files["base"], 'sandwich_pairs_hits'))
        print("Spearman: Effect of sandwich triples on runtime duplicates",
              print_spearman(duplicates_files["base"], 'sandwich_triple_hits'))

        print("##################################################################" +
              "\n#       Checking effect of properties WITH optimisations         #" +
              "\n##################################################################")

        print("Spearman: Effect of corner checks on runtime naive cch",
              print_spearman(naive_files["cch"], 'corner_check_hits'))
        print("Spearman: Effect of pair isolations on runtime naive pair isolation",
              print_spearman(naive_files["pair isolation"], 'pairs_isolation_hits'))
        print("Spearman: Effect of sandwich pairs on runtime naive sandwich pairs",
              print_spearman(naive_files["sandwiches"], 'sandwich_pairs_hits'))
        print("Spearman: Effect of sandwich triples on runtime naive sandwich triples",
              print_spearman(naive_files["sandwiches"], 'sandwich_triple_hits'))
        print("Spearman: Effect of sandwich triples on runtime naive sandwiches both",
              print_spearman_special(naive_files["sandwiches"]))

        print("Spearman: Effect of corner checks on runtime duplicates cch",
              print_spearman(duplicates_files["cch"], 'corner_check_hits'))
        print("Spearman: Effect of pair isolations on runtime duplicates pair isolation",
              print_spearman(duplicates_files["pair isolation"], 'pairs_isolation_hits'))
        print("Spearman: Effect of sandwich pairs on runtime duplicates sandwich pairs",
              print_spearman(duplicates_files["sandwiches"], 'sandwich_pairs_hits'))
        print("Spearman: Effect of sandwich triples on runtime duplicates sandwich triples",
              print_spearman(duplicates_files["sandwiches"], 'sandwich_triple_hits'))
        print("Spearman: Effect of sandwich triples on runtime duplicates sandwiches both",
              print_spearman_special(duplicates_files["sandwiches"]))

    res = []
    res.append(["naive"] + spearman_data(naive_files["base"], 'number_of_covered_tiles', 'cpu time'))
    res.append(["duplicates"] + spearman_data(duplicates_files["base"], 'number_of_covered_tiles', 'cpu time'))
    res.append(["path"] + spearman_data(path_files["base"], 'number_of_covered_tiles', 'cpu time'))
    res.append(["naive"] + spearman_data(naive_files["base"], 'number_of_duplicates', 'cpu time'))
    res.append(["duplicates"] + spearman_data(duplicates_files["base"], 'number_of_duplicates', 'cpu time'))
    res.append(["path"] + spearman_data(path_files["base"], 'number_of_duplicates', 'cpu time'))
    res.append(["duplicates"] + spearman_data(duplicates_files["base"], 'number_of_cycles', 'cpu time'))

    res.append(["####", "####", "####", "####", "####"])

    res.append(["naive"] + spearman_data(naive_files["base"], "corner_check_hits", "cpu time"))
    res.append(["duplicates"] + spearman_data(duplicates_files["base"], "corner_check_hits", "cpu time"))
    res.append(["path"] + spearman_data(path_files["base"], "corner_check_hits", "cpu time"))
    res.append(["naive"] + spearman_data(naive_files["base"], "pairs_isolation_hits", "cpu time"))
    res.append(["duplicates"] + spearman_data(duplicates_files["base"], "pairs_isolation_hits", "cpu time"))
    res.append(["path"] + spearman_data(path_files["base"], "pairs_isolation_hits", "cpu time"))
    # res.append(["naive"] + spearman_data(naive_files["base"], "edge_pairs_hits", "cpu time"))
    # res.append(["duplicates"] + spearman_data(duplicates_files["base"], "edge_pairs_hits", "cpu time"))
    # res.append(["path"] + spearman_data(path_files["base"], "edge_pairs_hits", "cpu time"))
    res.append(["naive"] + spearman_data(naive_files["base"], "sandwich_pairs_hits", "cpu time"))
    res.append(["duplicates"] + spearman_data(duplicates_files["base"], "sandwich_pairs_hits", "cpu time"))
    res.append(["path"] + spearman_data(path_files["base"], "sandwich_pairs_hits", "cpu time"))
    res.append(["naive"] + spearman_data(naive_files["base"], "sandwich_triple_hits", "cpu time"))
    res.append(["duplicates"] + spearman_data(duplicates_files["base"], "sandwich_triple_hits", "cpu time"))
    res.append(["path"] + spearman_data(path_files["base"], "sandwich_triple_hits", "cpu time"))

    res.append(["####", "####", "####", "####", "####"])

    res.append(["naive cch"] + spearman_data(naive_files["cch"], "corner_check_hits", "cpu time"))
    res.append(["duplicates cch"] + spearman_data(duplicates_files["cch"], "corner_check_hits", "cpu time"))
    res.append(["path cch"] + spearman_data(path_files["cch"], "corner_check_hits", "cpu time"))
    res.append(["naive pair isolation"] + spearman_data(naive_files["pair isolation"], "pairs_isolation_hits", "cpu time"))
    res.append(["duplicates pair isolation"] + spearman_data(duplicates_files["pair isolation"], "pairs_isolation_hits", "cpu time"))
    res.append(["path pair isolation"] + spearman_data(path_files["pair isolation"], "pairs_isolation_hits", "cpu time"))
    # res.append(["naive"] + spearman_data(naive_files["edge pairs"], "edge_pairs_hits", "cpu time"))
    # res.append(["duplicates"] + spearman_data(duplicates_files["edge pairs"], "edge_pairs_hits", "cpu time"))
    # res.append(["path"] + spearman_data(path_files["edge pairs"], "edge_pairs_hits", "cpu time"))
    res.append(["naive sandwiches"] + spearman_data(naive_files["sandwiches"], "sandwich_pairs_hits", "cpu time"))
    res.append(["duplicates sandwiches"] + spearman_data(duplicates_files["sandwiches"], "sandwich_pairs_hits", "cpu time"))
    res.append(["path sandwiches"] + spearman_data(path_files["sandwiches"], "sandwich_pairs_hits", "cpu time"))
    res.append(["naive sandwiches"] + spearman_data(naive_files["sandwiches"], "sandwich_triple_hits", "cpu time"))
    res.append(["duplicates sandwiches"] + spearman_data(duplicates_files["sandwiches"], "sandwich_triple_hits", "cpu time"))
    res.append(["path sandwiches"] + spearman_data(path_files["sandwiches"], "sandwich_triple_hits", "cpu time"))
    res.append(["naive sandwiches"] + spearman_data_special(naive_files["sandwiches"]))
    res.append(["duplicates sandwiches"] + spearman_data_special(duplicates_files["sandwiches"]))
    res.append(["path sandwiches"] + spearman_data_special(path_files["sandwiches"]))


    with open("results/properties_tests.csv", "w", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["model", "property 1", "property 2", "rho", "p-value"])
        writer.writeheader()

        for i in res:
            writer.writerow({"model": i[0], "property 1": i[1], "property 2": i[2], "rho": i[3][0], "p-value": i[3][1]})
