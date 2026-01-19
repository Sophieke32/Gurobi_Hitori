from data_analysis.retrieve_data import naive_files, duplicates_files, path_files
from data_analysis.visualisation_methods.save_boxplot_two_models import save_boxplot_two_models
from data_analysis.visualisation_methods.save_boxplots_covered_vs_time import save_boxplots_spearman_vs_time
from data_analysis.visualisation_methods.save_graph_ntest import save_graph_ntest
from data_analysis.visualisation_methods.save_plot_naive_vs_duplicates import save_plot_naive_vs_duplicates
from data_analysis.visualisation_methods.save_qq_plot import save_qq_plot
from data_analysis.visualisation_methods.save_scatter_cycles_vs_time import save_scatter_cycles_vs_time
from data_analysis.visualisation_methods.save_survival_plot import save_survival_plot
from data_analysis.visualisation_methods.show_histogram import save_histogram


def generate_graphs(generate_for_poster=False):
    print("Generating graphs...")

    save_survival_plot(naive_files["base"], duplicates_files["base"], path_files["base"], generate_for_poster)
    save_graph_ntest(naive_files["ntest"], duplicates_files["ntest"], path_files["ntest"], generate_for_poster)

    save_scatter_cycles_vs_time(duplicates_files["base"], generate_for_poster)

    save_boxplots_spearman_vs_time(naive_files["base"], generate_for_poster, "naive", "Influence of number of covered tiles on optimised naive runtime", 'number_of_covered_tiles', 'Number of covered tiles in final solution')
    save_boxplots_spearman_vs_time(duplicates_files["base"], generate_for_poster, "duplicates", "Influence of number of covered tiles on duplicates runtime", 'number_of_covered_tiles', 'Number of covered tiles in final solution')
    save_boxplots_spearman_vs_time(path_files["base"], generate_for_poster, "path", "Influence of number of covered tiles on path runtime", 'number_of_covered_tiles', 'Number of covered tiles in final solution')

    save_boxplots_spearman_vs_time(naive_files["base"], generate_for_poster, "naive", "Influence of number of duplicate tiles on optimised naive runtime", 'number_of_duplicates', 'Number of duplicate tiles in the instance')
    save_boxplots_spearman_vs_time(duplicates_files["base"], generate_for_poster, "duplicates", "Influence of number of duplicate tiles on duplicates runtime", 'number_of_duplicates', 'Number of duplicate tiles in the instance')
    save_boxplots_spearman_vs_time(path_files["base"], generate_for_poster, "path", "Influence of number of duplicate tiles on path runtime", 'number_of_duplicates', 'Number of duplicate tiles in the instance')

    # save_qq_plot(naive_files["no heuristic"], "qq_plot_no_heuristic")
    # save_qq_plot(naive_files["min heuristic"], "qq_plot_min_heuristic")
    # save_qq_plot(duplicates_files["base"], "qq_plot_duplicates")
    # save_qq_plot(duplicates_files["ntest"], "qq_plot_duplicates_ntest")


    ## Unused
    # save_plot_naive_vs_duplicates(duplicates_files["base"], naive_files["base"], generate_for_poster)
    # save_boxplot_two_models(naive_files["base"], duplicates_files["base"], generate_for_poster)

    # save_histogram(naive_files['base']['cpu time'], "histogram_naive")
    # save_histogram(duplicates_files['base']['cpu time'], "histogram_duplicates")

