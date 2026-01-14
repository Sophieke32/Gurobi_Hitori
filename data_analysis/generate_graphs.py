from data_analysis.retrieve_data import naive_files, duplicates_files
from data_analysis.visualisation_methods.save_boxplot_two_models import save_boxplot_two_models
from data_analysis.visualisation_methods.save_boxplots_covered_vs_time import save_boxplots_spearman_vs_time
from data_analysis.visualisation_methods.save_graph_ntest import save_graph_ntest
from data_analysis.visualisation_methods.save_plot_naive_vs_duplicates import save_plot_naive_vs_duplicates
from data_analysis.visualisation_methods.save_scatter_cycles_vs_time import save_scatter_cycles_vs_time
from data_analysis.visualisation_methods.save_survival_plot import save_survival_plot


def generate_graphs(generate_for_poster=False):
    save_survival_plot(naive_files["base"], duplicates_files["base"], generate_for_poster)

    save_plot_naive_vs_duplicates(duplicates_files["base"], naive_files["base"], generate_for_poster)
    save_scatter_cycles_vs_time(duplicates_files["base"], generate_for_poster)

    save_boxplots_spearman_vs_time(naive_files["base"], generate_for_poster, "naive", "Influence of number of covered tiles on optimised naive runtime", 'number_of_covered_tiles', 'Number of covered tiles')
    save_boxplots_spearman_vs_time(duplicates_files["base"], generate_for_poster, "duplicates", "Influence of number of covered tiles on duplicates runtime", 'number_of_covered_tiles', 'Number of covered tiles')

    save_boxplots_spearman_vs_time(naive_files["base"], generate_for_poster, "naive", "Influence of number of duplicate tiles on optimised naive runtime", 'number_of_duplicates', 'Number of duplicate tiles')
    save_boxplots_spearman_vs_time(duplicates_files["base"], generate_for_poster, "duplicates", "Influence of number of duplicate tiles on duplicates runtime", 'number_of_duplicates', 'Number of duplicate tiles')

    save_graph_ntest(naive_files["ntest"], duplicates_files["ntest"], generate_for_poster)

    save_boxplot_two_models(naive_files["base"], duplicates_files["base"], generate_for_poster)
