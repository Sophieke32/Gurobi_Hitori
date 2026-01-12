from scipy import stats

from data_analysis.helper_methods.spearman_test import print_spearman
from data_analysis.retrieve_data import naive_files, duplicates_files


def hitori_properties_tests():
    print("Spearman: Effect of number of covered tiles on naive (n=10)",
          print_spearman(naive_files["base"], 'number_of_covered_tiles'))
    print("Spearman: Effect of number of covered tiles on duplicates (n=10)",
          print_spearman(duplicates_files["base"], 'number_of_covered_tiles'))
    print("Spearman: Effect of number of cycles on duplicates (n=10)",
          print_spearman(duplicates_files["base"], 'number_of_cycles'))

    print("Spearman: Effect of graph time on runtime",
          print_spearman(duplicates_files["base"], 'graph time (s)'))
    # print("Spearman: Effect of graph time share on runtime",
    #       print_spearman(duplicates_files["base"], 'graph time share (%)'))
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


def spearman_special(csv):
    attribute_array = csv["sandwich_pairs_hits"] + csv["sandwich_triple_hits"]
    cpu_time = csv['cpu time']

    return stats.spearmanr(attribute_array, cpu_time)

def print_spearman_special(csv):
    res = spearman_special(csv)

    return "\nRho: {}\np-value: {}\n".format(res.statistic, res.pvalue)
