import matplotlib.pyplot as plt

from data_analysis.helper_methods.remove_outliers import remove_outliers_two_arrays


def save_boxplot_two_models(csv1, csv2, generate_for_poster):
    fig, ax = plt.subplots(figsize=(6, 5))

    data1, data2 = remove_outliers_two_arrays(csv1['cpu time'], csv2['cpu time'])
    data = [data1, data2]

    color = "#49c3fb"
    ax.boxplot(data, patch_artist=True,
               boxprops=dict(facecolor=color, color=color),
               capprops=dict(color='white'),
               whiskerprops=dict(color='white'),
               flierprops=dict(color=color, markeredgecolor=color),
               medianprops=dict(color='red'),
               tick_labels=["Naive model", "Duplicates model"]
               )
    ax.set_yscale('log')

    ax.set_ylabel('Time (s)', size=15)
    ax.set_title("Solving time of naive and duplicate model", size=15, color='white')

    # ax.legend()

    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)

    # Only show ticks on the left and bottom spines
    # ax.spines["bottom"].set_bounds(0, 1000)
    # ax.spines["left"].set_bounds(0, 0.8)

    ax.grid()
    ax.grid(which="minor", color="0.5")

    if generate_for_poster:
        # Set axes colours to white
        ax.spines["bottom"].set_color("white")
        ax.spines['left'].set_color('white')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')

        # plt.show()
        plt.savefig('figures/poster/boxplot_plot_two_models_poster.png', transparent=True)

    else:
        plt.savefig('figures/boxplot_plot_two_models.png')
