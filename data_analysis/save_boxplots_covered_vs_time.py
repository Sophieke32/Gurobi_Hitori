import matplotlib.pyplot as plt
import numpy as np

from data_analysis.helper_methods.remove_outliers import remove_outliers_csv


def save_boxplots_covered_vs_time(csv, file_addition, title):
    csv = remove_outliers_csv(csv)

    values = np.unique(csv['covered squares'])
    example_data = [[]]

    for v in values:
        indices = np.where(csv['covered squares'] == v)
        example_data.append(csv['cpu time'][indices])

    fig, ax = plt.subplots(figsize=(6, 5))
    color = "#49c3fb"
    ax.boxplot(example_data, patch_artist=True,
        boxprops=dict(facecolor = color, color = color),
        capprops=dict(color = 'white'),
        whiskerprops=dict(color = 'white'),
        flierprops=dict(color = color, markeredgecolor = color),
        medianprops=dict(color = 'red'),
        )
    ax.set_yscale('log')

    ax.set_ylabel('Time (s)', size=15)
    ax.set_xlabel('Number of covered squares', size=15)
    ax.set_title(title, size=15, color='white')

    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)

    # # Set axes colours to white
    ax.spines["bottom"].set_color("white")
    ax.spines['left'].set_color('white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    ax.grid()
    ax.grid(which="minor", color="0.5")

    plt.savefig('figures/boxplot_covered_vs_time_' + file_addition + '.png', transparent=True)
