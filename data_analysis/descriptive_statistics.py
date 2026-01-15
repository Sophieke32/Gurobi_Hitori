import csv

from data_analysis.helper_methods.descriptive_statistics import get_descriptive_statistics
from data_analysis.retrieve_data import naive_files, duplicates_files, path_files


def descriptive_statistics():
    print("Performing descriptive statistics...")

    res = []
    res.append(["naive", "cpu_time"] + [get_descriptive_statistics(naive_files['base'], 'cpu time')])
    res.append(["duplicates", "cpu_time"] + [get_descriptive_statistics(duplicates_files['base'], 'cpu time')])
    res.append(["path", "cpu_time"] + [get_descriptive_statistics(path_files['base'], 'cpu time')])


    with open("results/descriptives.csv", "w", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["model", "property", "mean", "variance"])
        writer.writeheader()

        for i in res:
            writer.writerow({"model": i[0], "property": i[1], "mean": i[2][2], "variance": i[2][3]})
